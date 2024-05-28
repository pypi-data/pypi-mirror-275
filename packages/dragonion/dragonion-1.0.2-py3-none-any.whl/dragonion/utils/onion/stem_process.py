"""
Rewritten from stem sources to work with dragonion
"""

import asyncio
import os
import platform
import re
import signal
import tempfile
import threading
from asyncio import subprocess

import stem.prereq
import stem.util.str_tools
import stem.util.system
import stem.version

NO_TORRC = "<no torrc>"
DEFAULT_INIT_TIMEOUT = 90


async def launch_tor(
    tor_cmd="tor",
    args=None,
    torrc_path=None,
    completion_percent=100,
    init_msg_handler=None,
    timeout=DEFAULT_INIT_TIMEOUT,
    take_ownership=False,
    close_output=True,
    stdin=None,
):
    """
    Initializes a tor process. This blocks until initialization completes or we
    error out.

    If tor's data directory is missing or stale then bootstrapping will include
    making several requests to the directory authorities which can take a little
    while. Usually this is done in 50 seconds or so, but occasionally calls seem
    to get stuck, taking well over the default timeout.

    **To work to must log at NOTICE runlevel to stdout.** It does this by
    default, but if you have a 'Log' entry in your torrc then you'll also need
    'Log NOTICE stdout'.

    Note: The timeout argument does not work on Windows or when outside the
    main thread, and relies on the global state of the signal module.

    .. versionchanged:: 1.6.0
       Allowing the timeout argument to be a float.

    .. versionchanged:: 1.7.0
       Added the **close_output** argument.

    :param str tor_cmd: command for starting tor
    :param list args: additional arguments for tor
    :param str torrc_path: location of the torrc for us to use
    :param int completion_percent: percent of bootstrap completion at which
      this will return
    :param functor init_msg_handler: optional functor that will be provided with
      tor's initialization stdout as we get it
    :param int timeout: time after which the attempt to start tor is aborted, no
      timeouts are applied if **None**
    :param bool take_ownership: asserts ownership over the tor process, so it
      aborts if this python process terminates or a :class:`~stem.control.Controller`
      we establish to it disconnects
    :param bool close_output: closes tor's stdout and stderr streams when
      bootstrapping is complete if true
    :param str stdin: content to provide on stdin

    :returns: **subprocess.Popen** instance for the tor subprocess

    :raises: **OSError** if we either fail to create the tor process or reached a
      timeout without success
    """

    assert close_output

    if stem.util.system.is_windows():
        if timeout is not None and timeout != DEFAULT_INIT_TIMEOUT:
            raise OSError("You cannot launch tor with a timeout on Windows")

        timeout = None
    elif threading.current_thread().__class__.__name__ != "_MainThread":
        if timeout is not None and timeout != DEFAULT_INIT_TIMEOUT:
            raise OSError(
                "Launching tor with a timeout can only be done in the main thread"
            )

        timeout = None

    # sanity check that we got a tor binary

    if os.path.sep in tor_cmd:
        # got a path (either relative or absolute), check what it leads to

        if os.path.isdir(tor_cmd):
            raise OSError("'%s' is a directory, not the tor executable" % tor_cmd)
        elif not os.path.isfile(tor_cmd):
            raise OSError("'%s' doesn't exist" % tor_cmd)
    elif not stem.util.system.is_available(tor_cmd):
        raise OSError(
            f"{tor_cmd} isn't available on your system. "
            f"Maybe it's not in your PATH?"
        )

    # double check that we have a torrc to work with
    if torrc_path not in (None, NO_TORRC) and not os.path.exists(torrc_path):
        raise OSError("torrc doesn't exist (%s)" % torrc_path)

    # starts a tor subprocess, raising an OSError if it fails
    runtime_args, temp_file = [tor_cmd], None

    if args:
        runtime_args += args

    if torrc_path:
        if torrc_path == NO_TORRC:
            temp_file = tempfile.mkstemp(prefix="empty-torrc-", text=True)[1]
            runtime_args += ["-f", temp_file]
        else:
            runtime_args += ["-f", torrc_path]

    if take_ownership:
        runtime_args += ["__OwningControllerProcess", str(os.getpid())]

    tor_process = None

    try:
        tor_process = await asyncio.create_subprocess_shell(
            " ".join(runtime_args),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=None
            if platform.system() == "Windows"
            else {"LD_LIBRARY_PATH": os.path.dirname(tor_cmd)},
        )

        if stdin:
            # noinspection PyProtectedMember
            tor_process.stdin.write(stem.util.str_tools._to_bytes(stdin))
            tor_process.stdin.close()

        if timeout:

            def timeout_handler(*_):
                raise OSError("reached a %i second timeout without success" % timeout)

            signal.signal(signal.SIGALRM, timeout_handler)
            signal.setitimer(signal.ITIMER_REAL, timeout)

        bootstrap_line = re.compile("Bootstrapped ([0-9]+)%")
        problem_line = re.compile("\\[(warn|err)] (.*)$")
        last_problem = "Timed out"

        while True:
            # Tor's stdout will be read as ASCII bytes. This is fine for python 2, but
            # in python 3 that means it'll mismatch with other operations (for instance
            # the bootstrap_line.search() call later will fail).
            #
            # It seems like python 2.x is perfectly happy for this to be unicode, so
            # normalizing to that.

            init_line = (
                (await tor_process.stdout.readline()).decode("utf-8", "replace").strip()
            )

            # this will provide empty results if the process is terminated

            if not init_line:
                raise OSError("Process terminated: %s" % last_problem)

            # provide the caller with the initialization message if they want it

            if init_msg_handler:
                init_msg_handler(init_line)

            # return the process if we're done with bootstrapping

            bootstrap_match = bootstrap_line.search(init_line)
            problem_match = problem_line.search(init_line)

            if bootstrap_match and int(bootstrap_match.group(1)) >= completion_percent:
                return tor_process
            elif problem_match:
                runlevel, msg = problem_match.groups()

                if "see warnings above" not in msg:
                    if ": " in msg:
                        msg = msg.split(": ")[-1].strip()

                    last_problem = msg
    except Exception as e:
        print(e)
        if tor_process:
            tor_process.kill()  # don't leave a lingering process
            await tor_process.wait()

        raise
    finally:
        if timeout:
            signal.alarm(0)  # stop alarm

        if temp_file:
            try:
                os.remove(temp_file)
            except Exception as e:
                assert e


async def launch_tor_with_config(
    config,
    tor_cmd="tor",
    completion_percent=100,
    init_msg_handler=None,
    timeout=DEFAULT_INIT_TIMEOUT,
    take_ownership=False,
    close_output=True,
):
    """
    Initializes a tor process, like :func:`~stem.process.launch_tor`, but with a
    customized configuration. This writes a temporary torrc to disk, launches
    tor, then deletes the torrc.

    For example...

    ::

      tor_process = stem.process.launch_tor_with_config(
        config = {
          'ControlPort': '2778',
          'Log': [
            'NOTICE stdout',
            'ERR file /tmp/tor_error_log',
          ],
        },
      )

    .. versionchanged:: 1.7.0
       Added the **close_output** argument.

    :param dict config: configuration options, such as "{'ControlPort': '9051'}",
      values can either be a **str** or **list of str** if for multiple values
    :param str tor_cmd: command for starting tor
    :param int completion_percent: percent of bootstrap completion at which
      this will return
    :param functor init_msg_handler: optional functor that will be provided with
      tor's initialization stdout as we get it
    :param int timeout: time after which the attempt to start tor is aborted, no
      timeouts are applied if **None**
    :param bool take_ownership: asserts ownership over the tor process, so it
      aborts if this python process terminates or a :class:`~stem.control.Controller`
      we establish to it disconnects
    :param bool close_output: closes tor's stdout and stderr streams when
      bootstrapping is complete if true

    :returns: **subprocess.Popen** instance for the tor subprocess

    :raises: **OSError** if we either fail to create the tor process or reached a
      timeout without success
    """

    try:
        use_stdin = (
            stem.version.get_system_tor_version(tor_cmd)
            >= stem.version.Requirement.TORRC_VIA_STDIN
        )
    except IOError:
        use_stdin = False

    # we need to be sure that we're logging to stdout to figure out when we're
    # done bootstrapping

    if "Log" in config:
        stdout_options = ["DEBUG stdout", "INFO stdout", "NOTICE stdout"]

        if isinstance(config["Log"], str):
            config["Log"] = [config["Log"]]

        has_stdout = False

        for log_config in config["Log"]:
            if log_config in stdout_options:
                has_stdout = True
                break

        if not has_stdout:
            config["Log"].append("NOTICE stdout")

    config_str = ""

    for key, values in list(config.items()):
        if isinstance(values, str):
            config_str += "%s %s\n" % (key, values)
        else:
            for value in values:
                config_str += "%s %s\n" % (key, value)

    if use_stdin:
        return await launch_tor(
            tor_cmd=tor_cmd,
            args=["-f", "-"],
            completion_percent=completion_percent,
            init_msg_handler=init_msg_handler,
            timeout=timeout,
            take_ownership=take_ownership,
            close_output=close_output,
            stdin=config_str,
        )
    else:
        torrc_descriptor, torrc_path = tempfile.mkstemp(prefix="torrc-", text=True)

        try:
            with open(torrc_path, "w") as torrc_file:
                torrc_file.write(config_str)

            # prevents tor from error-ing out due to a missing torrc if it gets a sighup
            args = ["__ReloadTorrcOnSIGHUP", "0"]

            return await launch_tor(
                tor_cmd,
                args,
                torrc_path,
                completion_percent,
                init_msg_handler,
                timeout,
                take_ownership,
            )
        finally:
            try:
                os.close(torrc_descriptor)
                os.remove(torrc_path)
            except Exception as e:
                assert e
