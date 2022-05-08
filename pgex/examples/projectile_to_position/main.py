"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from .projectile import Projectile


async def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    clock = pygame.time.Clock()

    projectile_group = pygame.sprite.Group()

    running = True
    while running:
        clock.tick(60)
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    projectile = Projectile((250, 200), event.pos)
                    projectile_group.add(projectile)

        projectile_group.update()
        projectile_group.draw(screen)
        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
