"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame
from _types import _ColorValue
from darkener import Darkener


def draw_stripes(bg: pygame.Surface, color: _ColorValue, thickness: int):
    width, height = bg.get_size()

    stripe_rect = pygame.Rect((0, 0), (thickness, height))

    for i in range(width // thickness):
        if i % 2:
            stripe_rect.left = thickness * i
            pygame.draw.rect(bg, color, stripe_rect)


async def main() -> None:
    pygame.init()

    width, height = 400, 500

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    bg = pygame.Surface((width, height))
    bg.fill("red")
    draw_stripes(bg, "green", 5)

    radius = 30
    darken_ratio = 0.4

    bg_darkener = Darkener(bg, radius, darken_ratio)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mousepos = pygame.mouse.get_pos()
        bg_darkener.update(mousepos)

        screen.fill((0, 0, 0))
        bg_darkener.draw(screen, bg.get_rect())
        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
