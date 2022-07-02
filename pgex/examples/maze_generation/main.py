"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

# from ._types import _ColorValue


async def main() -> None:
    pygame.init()

    width, height = 400, 500

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))
        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()