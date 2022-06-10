"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
import os
from typing import List, Tuple

import pygame


def get_images(
    sheet: pygame.Surface, size: Tuple[int], bound=False
) -> List[pygame.Surface]:
    """
    Get images from a sprite sheet
    Parameters:
                    sheet: pygame.Surface with the sprite sheet
                    size: Size of a sprite in the sprite sheet
                    bound: Optional
    """
    images = []

    # get the amount of rows and columns in the sprite sheet
    width, height = size
    rows = int(sheet.get_height() / height)
    columns = int(sheet.get_width() / width)

    # loop through all sprites in the sprite sheet
    for row in range(rows):
        for col in range(columns):
            # get the image
            image = sheet.subsurface(
                pygame.Rect((col * width), (row * height), width, height)
            )

            if bound:
                rect = image.get_bounding_rect()
                image = image.subsurface(rect)

            # add it to the image list
            images.append(image)

    return images


async def main():
    """
    Contains game variables and the game loop
    """
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Sprite sheet!")
    clock = pygame.time.Clock()

    sprite_size = (96, 102)
    # loading the sprite sheet
    # art made by https://0x72.itch.io
    sheet = pygame.image.load(
        os.path.join(os.path.dirname(__file__), "sheet.png")
    ).convert_alpha()
    # getting the frames of the sprite sheet
    frames = get_images(sheet, sprite_size)
    # frame index
    index = 0
    animation_speed = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.fill("black")

        # increase the frame index
        index += 1

        # if the frame index is too high, reset it to 0
        # this makes the animation loop
        if index >= len(frames) * animation_speed:
            index = 0

        # draw the current frame
        screen.blit(frames[index // animation_speed], (250, 150))

        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    """
    Runs the example
    """
    asyncio.run(main())


if __name__ == "__main__":
    run()
