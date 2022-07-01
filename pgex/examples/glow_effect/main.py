"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
import math
from typing import Tuple

import pygame

Point = Tuple[float, float]

def distance(p1: Point, p2: Point) -> float:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    radicand = dx ** 2 + dy ** 2
    return math.sqrt(radicand)

async def main() -> None:
    pygame.init()

    brighten_radius = 10

