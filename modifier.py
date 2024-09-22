from enum import Enum


class Modifier(str, Enum):
    bold = "b"
    blink_slow = "blink"
    blink_fast = "blink2"
    conceal = "conceal"
    italic = "i"
    reverse = "r"
    strike = "s"
    underline = "u"

    double_underline = "uu"
    frame = "frame"
    encircle = "encircle"
    overline = "o"
