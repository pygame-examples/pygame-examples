"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Module that contains the Entity, Particle classes
"""

from typing import List

import pygame
from pygame import Vector2


class Particle:
    def __init__(
        self,
        pos: Vector2,
        vel: Vector2,
        radius: int = 10,
        radius_speed: int = 0.5,
        gravity: float = 1,
    ):
        """
        Parameters:
            pos: Spawn position of the particle
            vel: How far does the particle move every frame (x, y)
            radius: Radius of the particle
            radius_speed: Decreasing speed of the particle's radius
            gravity: Fall speed of the particle
        """

        self.pos = pos
        self.radius = radius
        self.radius_speed = radius_speed
        self.vel = vel
        # flip the y velocity so the particle goes up and then fall
        self.vel.y = -self.vel.y
        self.gravity = gravity

    def draw(self, display: pygame.Surface):
        """
        Draws particles on a pygame.Surface
        Parameters:
            display: the surface the particle is drawn on
        """

        pygame.draw.circle(display, "white", self.pos, self.radius)

    def update(self, dt: float):
        """
        Updates the particle
        Parameters:
            dt: delta time (between frames)
        """

        # increase vel.y so particle goes down exponentially
        self.vel.y += self.gravity * dt

        # update particle position
        self.pos.x += self.vel.x * dt
        self.pos.y += self.vel.y * dt

        # decrease the radius
        self.radius -= self.radius_speed * dt
