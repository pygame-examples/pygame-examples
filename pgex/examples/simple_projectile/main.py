"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from .bullet import Bullet

WIDTH, HEIGHT = 640, 360
FPS = 60


async def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    bullet_group = pygame.sprite.Group()

    running = True
    while running:
        clock.tick(FPS)
        screen.fill("black")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_bullet = Bullet(pygame.Vector2(0, 180), pygame.Vector2(5, 0))
                    bullet_group.add(new_bullet)

        bullet_group.update()
        bullet_group.draw(screen)

        pygame.display.flip()
        await asyncio.sleep(0)


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
