"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

from typing import List, Sequence, Tuple, TypeAlias, Union

import pygame

Array: TypeAlias = Union[Tuple[int, int], List[int], pygame.Vector2, Sequence[int]]
_SeedValue: TypeAlias = int | float | str | bytes | bytearray | None
_RgbaOutput: TypeAlias = Tuple[int, int, int, int]
_ColorValue: TypeAlias = Union[
    pygame.Color, int, str, Tuple[int, int, int], List[int], _RgbaOutput
]
