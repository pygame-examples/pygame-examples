"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
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
    rows = int(sheet.get_height() / size[1])
    columns = int(sheet.get_width() / size[0])

    # loop through all sprites in the sprite sheet
    for row in range(rows):
        for col in range(columns):
            # get the image
            image = sheet.subsurface(
                pygame.Rect((col * size[0]), (row * size[1]), size[0], size[1])
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
    sheet = pygame.image.load("sheet.png").convert_alpha()
    # getting the frames of the sprite sheet
    frames = get_images(sheet, sprite_size)
    # frame index
    _index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.fill("black")

        # increase the frame index
        _index += 0.1

        # if the frame index is too high, reset it to 0
        # this makes the animation loop
        if _index >= len(frames):
            _index = 0

        # draw the current frame
        screen.blit(frames[int(_index)], (250, 150))

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
