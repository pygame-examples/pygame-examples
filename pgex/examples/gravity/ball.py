"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Module that contains the Ball class
"""

import pygame

from ._types import ColorValue


class Ball:
    """
    A Ball class to demonstrate implementation of gravity in Pygame.
    """

    def __init__(
        self,
        pos: pygame.Vector2,
        gravity: float = 0.25,
        radius: int = 20,
        color: ColorValue = "red",
    ):
        """
        Parameters:
                pos: A pygame.Vector2 containing the starting position of the ball
                gravity: Falling speed of the ball
                radius: Radius of the ball
                color: Color of the ball
        """

        self.pos = pos
        self.gravity = gravity
        self.radius = radius
        self.fall_speed = 0
        self.color = color

    def draw(self, screen: pygame.Surface):
        """
        Draw the ball on the screen
        """
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def update(self, screen: pygame.Surface, dt: float):
        """
        Update ball's position, draw it on the screen
        """
        # increase fall_speed so the ball falls exponentially
        self.fall_speed += self.gravity * dt
        self.pos.y += self.fall_speed * dt

        self.draw(screen)
