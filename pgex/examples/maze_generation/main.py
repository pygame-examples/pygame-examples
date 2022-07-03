"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from .generator import Generator


async def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((640, 320))
    clock = pygame.time.Clock()

    # seed is an optional argument to get the same maze
    maze = Generator(screen.get_size(), 8)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("red")
        maze.draw(screen)
        pygame.display.flip()
        clock.tick()

        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
