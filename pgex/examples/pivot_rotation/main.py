"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from .image import Image

# Initialize pygame
pygame.init()

# Constants
SCREENW = 800
SCREENH = 600
CAPTION = "Pivot Rotation"
FPS = 60


async def main():
    screen = pygame.display.set_mode((SCREENW, SCREENH))
    pygame.display.set_caption(CAPTION)

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 30)

    running = True
    image = Image(SCREENW, SCREENH, font)

    while running:
        dt = clock.tick(FPS) / 1000  # Clamp the fps at 60 and get the delta time

        # The event loop for processing the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            image.events(event)

        # All the physics goes here
        image.physics()

        # Finally draw everything
        screen.fill("White")  # Clear the screen before drawing
        image.draw(screen)
        pygame.display.update()

        await asyncio.sleep(0)

    pygame.quit()


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
