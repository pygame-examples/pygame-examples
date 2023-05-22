"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

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

    def move_towards(self, x_pos: int, y_pos: int) -> None:
        """
        Moves entity toward a give position
        """

        position_vector = pygame.Vector2(self.rect.center)
        update_position = position_vector.move_towards((x_pos, y_pos), self.speed)
        self.rect.center = update_position

    def draw(self, display: pygame.Surface) -> None:
        """
        Render the entity
        """
        pygame.draw.rect(
            display,
            self.color,
            self.rect,
        )
