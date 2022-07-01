"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import typing as t

import pygame

PositionLike: t.TypeAlias = t.Union[
    t.List[float], t.Tuple[float, float], pygame.Vector2
]
