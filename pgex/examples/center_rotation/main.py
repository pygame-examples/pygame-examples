"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
import os

import pygame

from .rotating_image import RotatingImage

WIDTH, HEIGHT = 640, 360
FPS = 60


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    image = pygame.transform.rotozoom(
        pygame.image.load(os.path.join(os.path.dirname(__file__), "assets/image.png")),
        angle=0,
        scale=0.2,
    )
    rotating_image = RotatingImage(image, (WIDTH / 2, HEIGHT / 2))
    angle = 0

    running = True
    while running:
        clock.tick(FPS)
        screen.fill("black")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        rotating_image.update(angle)
        rotating_image.draw(screen)

        angle += 1
        if angle >= 360:
            angle = 0

        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
