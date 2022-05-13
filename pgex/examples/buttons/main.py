"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
import random

import pygame

from .button import Button

bg_color = (0, 0, 0)


async def main():
    pygame.init()

    def button_method():
        global bg_color
        bg_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    button = Button(50, 50, 100, 30, "Lol", "black", "white", button_method)

    screen = pygame.display.set_mode((500, 400))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        screen.fill(bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button.draw(screen)
        button.update()
        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
