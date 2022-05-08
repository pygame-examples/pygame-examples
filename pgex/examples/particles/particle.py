"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Module that contains the Entity, Particle classes
"""

import abc
import random
from typing import List

import pygame
from pygame import Vector2


class Entity(abc.ABC):
    """
    Simple Entity class.
    """

    def __init__(self, pos: List[int]):
        """
        Parameters:
            pos: Position of the entity
        """
        self.pos = pygame.Vector2(pos)


class Particle(Entity):
    """
    Customizable particle class.
    """

    def __init__(
        self,
        pos: List[int],
        radius: int = 10,
        radius_speed: int = 0.5,
        vel: Vector2 = Vector2(random.randrange(-5, 5), 7),
        gravity: float = 1,
    ):
        """
        Parameters:
            pos: Position of the particle
            radius: Radius of the particle
            radius_speed: Decreasing speed of the particle's radius
            vel: How far does the particle move (x, y)
            gravity: Fall speed of the particle
        """

        super().__init__(pos)
        self.radius = radius
        self.radius_speed = radius_speed
        self.vel = vel
        # flip the y velocity so the particle goes up and then fall
        self.vel.y = -self.vel.y
        self.gravity = gravity

    def draw(self, display: pygame.Surface):
        """
        Function that draws particles on a pygame.Surface.
        """

        pygame.draw.circle(display, "white", self.pos, self.radius)

    def update(self, display: pygame.Surface, dt: float):
        """
        Function that updates the particle.
        """

        # increase vel.y so particle goes down exponentially
        self.vel.y += self.gravity * dt

        # update particle position
        self.pos.x += self.vel.x * dt
        self.pos.y += self.vel.y * dt

        # decrease the radius
        self.radius -= self.radius_speed * dt

        # draw the particle
        self.draw(display)
