"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
import os

import pygame

from .horizontal_slider import HorizontalSlider

WIDTH, HEIGHT = 500, 400


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    horizontal_slider = HorizontalSlider(
        pygame.Rect(50, 180, 400, 40),
        step=10,
        callback=lambda val: pygame.mixer.music.set_volume(val / 100),
    )
    horizontal_slider.value = 10

    pygame.mixer.music.load(
        os.path.join(
            os.path.dirname(__file__), "assets/Hooky with Sloane - Bird Creek.mp3"
        )
    )
    pygame.mixer.music.play(loops=-1)

    running = True
    while running:
        clock.tick(60)
        screen.fill("black")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        horizontal_slider.update(events)
        horizontal_slider.draw(screen)

        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
