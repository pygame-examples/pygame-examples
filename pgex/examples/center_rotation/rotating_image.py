"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame

from ._types import PositionLike


class RotatingImage:
    """Class representing a rotating image."""

    def __init__(
        self, image: pygame.Surface, pos: PositionLike, angle: float = 0
    ) -> None:
        """
        Initializes RotatingImage with necessary attributes.
        :param pos: center position of the image, can be changed later using rect attribute
        :param image: the surface to be rotated
        :param angle: starting angle in degrees
        """

        self.image = image
        self.rect = image.get_rect(center=pos)
        self.angle = angle

    def update(self, angle: float) -> None:
        """
        Updates the angle.
        :param angle: new angle in degrees
        :return:
        """

        self.angle = angle

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the rotated image on the given surface.
        :param surface: a pygame surface to draw on
        :return:
        """

        image = pygame.transform.rotate(self.image, self.angle)
        rect = image.get_rect(center=self.rect.center)
        surface.blit(image, rect)
