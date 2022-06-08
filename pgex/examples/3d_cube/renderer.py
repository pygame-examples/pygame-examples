"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Implements the Renderer class, responsible for 3D rendering to a surface
"""

import math
from typing import Tuple

import pygame
from pygame.color import Color
from pygame.math import Vector3


class Renderer:
    def __init__(self, target: pygame.Surface, fov: float):
        self.target = target
        self.fov = fov

    def translate(self, vector: Vector3) -> Tuple[int, int]:
        """
        Translates 3D space into target surface space.
        """

        # Apply the rules of perspective: 1/Z.
        try:
            translated_x = vector.x / vector.z
            translated_y = -vector.y / vector.z  # Remember that pygame uses "Y-down."
        except ZeroDivisionError:
            translated_x = 0
            translated_y = 0

        # Determines the screen space scale factor based on the given widest width
        # or height of the target surface, and the tangent of the FOV.
        screen_factor = max(self.target.get_size()) / 2
        screen_factor *= math.tan(math.radians((180 - self.fov) / 2))

        translated_x *= screen_factor
        translated_y *= screen_factor

        # Offset to the center of the surface for (0, 0).
        translated_x += self.target.get_width() / 2
        translated_y += self.target.get_height() / 2

        # Don't forget that we were handling with true div float maths.
        return int(translated_x), int(translated_y)

    def draw_point(self, point: Vector3, color: Color):
        """
        Draws a point in 3D space.
        """

        translated_point = self.translate(point)

        # Surface bound checking, as `pygame.Surface.set_at` needs the given pixel
        # to be inside the surface.
        if (
            0 <= translated_point.x < self.target.get_width()
            and 0 <= translated_point.y < self.target.get_height()
        ):
            self.target.set_at(translated_point, color)

    def draw_line(self, begin: Vector3, end: Vector3, color: Color):
        """
        Draws a line in 3D space.
        """

        # Anti-aliased lines are nice!
        pygame.draw.aaline(
            self.target, color, self.translate(begin), self.translate(end)
        )
