from typing import Sequence, Tuple, Union

from pygame import Color

# type hint for pygame color
RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]
