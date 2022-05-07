from enum import Enum
import itertools
from colorama import Fore
import random


del Fore.__dict__["BLACK"]


class OutputStyle(Enum):
    """
    Enum containing different output styles
    to output text to the console.
    """

    RAINBOW_BOX = (
        "[n]",
        itertools.cycle(
            (
                Fore.WHITE,
                Fore.LIGHTWHITE_EX,
                Fore.LIGHTYELLOW_EX,
                Fore.YELLOW,
                Fore.LIGHTGREEN_EX,
                Fore.GREEN,
                Fore.LIGHTCYAN_EX,
                Fore.CYAN,
                Fore.LIGHTMAGENTA_EX,
                Fore.MAGENTA,
            )
        ),
    )
    RANDOM_BOX = (
        "[n]",
        itertools.cycle(
            random.sample(list(Fore.__dict__.values()), len(Fore.__dict__))
        ),
    )
    PLAIN_BOX = ("[n]", "")

    RAINBOW_PERIOD = ("n.", RAINBOW_BOX[1])
    RANDOM_PERIOD = (
        "n.",
        RANDOM_BOX[1],
    )
    PLAIN_PERIOD = ("n.", "")
