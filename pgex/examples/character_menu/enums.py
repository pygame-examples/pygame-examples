"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import enum


class GameStates(enum.Enum):
    MAIN_MENU = enum.auto()
    CHARACTER_MENU = enum.auto()
    GAMEPLAY = enum.auto()
