import pygame
from ._types import *


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
        self.color = "red"

    def draw(self, display: pygame.Surface):
        pygame.draw.circle(display, self.color, self.pos, self.radius)

    def update(self, display: pygame.Surface, dt: float):
        # increase fall_speed so the ball falls exponentially
        self.fall_speed += self.gravity * dt
        self.pos.y += self.fall_speed * dt

        self.draw(display)
