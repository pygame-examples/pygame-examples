from enum import Enum
import itertools
from colorama import Fore
import random


# TODO: Fill in
class OutputStyle:
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
    RANDOM_BOX = "[n]"
    PLAIN_BOX = "[n]"

    RAINBOW_PERIOD = "."
    RANDOM_PERIOD = (
        "n.",
        itertools.cycle(
            random.sample(list(Fore.__dict__.values()), len(Fore.__dict__))
        ),
    )
    PLAIN_PERIOD = "."
