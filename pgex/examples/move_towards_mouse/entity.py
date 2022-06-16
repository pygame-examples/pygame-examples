"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import math
from typing import Tuple

import pygame


class Entity:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        speed: int,
        color: Tuple[int, int, int],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_centered_position(self) -> pygame.Rect:
        """
        Returns the center of the entities rect
        """

        return self.rect.center

    def move_towards(self, x_pos: int, y_pos: int) -> None:
        """
        Moves entity toward a give position
        """

        position_vector = pygame.math.Vector2(*self.get_centered_position())
        dy, dx = y_pos - position_vector.y, x_pos - position_vector.x
        angle = math.atan2(dy, dx)

        self.rect.x += math.cos(angle) * (self.speed * (abs(dx) / 100) + 1.1)
        self.rect.y += math.sin(angle) * (self.speed * (abs(dy) / 100) + 1.1)

    def draw(self, display: pygame.Surface) -> None:
        """
        Render the entity
        """

        pygame.draw.rect(
            display,
            self.color,
            self.rect,
        )
