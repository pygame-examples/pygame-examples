from typing import Tuple, Union, Sequence
from pygame import Color

# type hint for pygame color
RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]
