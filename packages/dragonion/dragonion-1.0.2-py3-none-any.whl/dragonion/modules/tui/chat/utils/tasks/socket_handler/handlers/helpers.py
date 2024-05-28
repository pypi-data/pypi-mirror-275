from datetime import datetime


def render_time(time: datetime):
    return f"[#a5abb3][{time.time().strftime('%H:%M:%S')}][/]"
