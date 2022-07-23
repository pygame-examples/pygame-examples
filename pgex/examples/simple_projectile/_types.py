"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import typing as t

import pygame

PositionLike: t.TypeAlias = t.Union[
    t.Tuple[float, float], t.List[float], pygame.Vector2
]
VelocityLike: t.TypeAlias = PositionLike
