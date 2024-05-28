from bisect import bisect
from itertools import accumulate
from random import randrange


def random_emoji():
    emoji_ranges = [
        ("\U0001F300", "\U0001F579"),
        ("\U0001F57B", "\U0001F5A3"),
        ("\U0001F5A5", "\U0001F5FF"),
    ]

    count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
    weight_distr = list(accumulate(count))

    point = randrange(weight_distr[-1])

    emoji_range_idx = bisect(weight_distr, point)
    emoji_range = emoji_ranges[emoji_range_idx]

    point_in_range = point
    if emoji_range_idx != 0:
        point_in_range = point - weight_distr[emoji_range_idx - 1]

    emoji = str(chr(ord(emoji_range[0]) + point_in_range))

    return emoji
