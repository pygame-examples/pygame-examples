import pygame
from pygame import Vector2
import abc
import random
from typing import List


class Entity(abc.ABC):
    def __init__(self, pos: List[int]):

        """Simple Entity class."""

        self.pos = pygame.Vector2(pos)


class Particle(Entity):
    """Customizable particle class."""

    def __init__(
        self,
        pos: List[int],
        radius: int = 10,
        radius_speed: int = 0.5,
        vel: Vector2 = Vector2(random.randrange(-5, 5), 7),
        gravity: float = 1,
    ):

        super().__init__(pos)
        self.radius = radius
        self.radius_speed = radius_speed
        self.vel = vel
        # flip the y velocity so the particle goes up and then fall
        self.vel.y = -self.vel.y
        self.gravity = gravity

    def draw(self, display: pygame.Surface):

        """Function that draws particles on a pygame.Surface."""

        pygame.draw.circle(display, "white", self.pos, self.radius)

    def update(self, display: pygame.Surface, dt: float):

        """Function to update the particle."""

        # increase vel.y so particle goes down exponentially
        self.vel.y += self.gravity * dt

        # update particle position
        self.pos.x += self.vel.x * dt
        self.pos.y += self.vel.y * dt

        # decrease the radius
        self.radius -= self.radius_speed * dt

        # draw the particle
        self.draw(display)
