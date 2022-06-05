"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Module that contains the ColoredRect class
"""
import itertools
from typing import Iterable

import pygame

from ._types import ColorValue


class ColoredRect:
    """
    A colored rectangle class to demonstrate the usage of pygame timers
    """

    def __init__(
        self,
        pos: Iterable[int],
        size: Iterable[int],
        colors: Iterable[ColorValue],
    ):
        """
        Parameters:
                pos: The position of the rectangle
                size: The size of the rectangle
                colors: An iterable containing rectangle's colors
        """

        self.rect = pygame.Rect(pos, size)
        # Create a cycle so the colors change infinitely
        self.color_cycle = itertools.cycle(colors)
        self.color = next(self.color_cycle)

    def change_color(self):
        """
        Change the color to the next one in the self.color_cycle
        """
        self.color = next(self.color_cycle)

    def draw(self, screen: pygame.Surface):
        """
        Draw the rectangle on the screen
        """
        pygame.draw.rect(screen, self.color, self.rect)
