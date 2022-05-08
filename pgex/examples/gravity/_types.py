"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Module that contains type hints
"""

from typing import Sequence, Tuple, Union

from pygame import Color

# type hint for pygame color
RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]
