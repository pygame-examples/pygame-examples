"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
import math
from typing import Tuple

import pygame

Point = Tuple[int, int]

def distance(p1: Point, p2: Point) -> float:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    radicand = dx ** 2 + dy ** 2
    return math.sqrt(radicand)

def darken(
    radius: int,
    center: Point,
    base_surface: pygame.surface.Surface,
    darken_percent: float
) -> pygame.surface.Surface:

    surf_size = base_surface.get_size()

    dark_surface = pygame.Surface(surf_size, pygame.SRCALPHA)
    dark_surface.fill((0, 0, 0, darken_percent * 255))

    important_rect = pygame.Rect(0, 0, radius * 2, radius * 2)
    important_rect.center = center

    try:
        subsurface = dark_surface.subsurface(important_rect)
    except ValueError:
        base_surface.blit(dark_surface, dark_surface.get_rect())
        return base_surface

    pixels = pygame.surfarray.pixels_alpha(subsurface)

    central_point = (radius, radius)
    for row in range(radius * 2):
        for col in range(radius * 2):
            if distance((row, col), central_point) <= radius:
                pixels[row][col] = 0

    del pixels
    base_surface.blit(dark_surface, dark_surface.get_rect())

    return base_surface

async def main() -> None:
    pygame.init()

    width, height = 400, 500

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    radius = 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = pygame.Surface((width, height))
        bg.fill("red")

        mousepos = pygame.mouse.get_pos()
        bg = darken(radius, mousepos, bg, 0.58)

        screen.fill((0, 0, 0))
        screen.blit(bg, bg.get_rect())
        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
