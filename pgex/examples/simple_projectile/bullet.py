"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame

from ._types import Position, Velocity
from .settings import HEIGHT, WIDTH


class Bullet(pygame.sprite.Sprite):
    image = pygame.Surface((16, 16))
    image.fill("red")

    bounding_box = pygame.Rect(0, 0, WIDTH, HEIGHT)

    def __init__(self, start_pos: Position, velocity: Velocity) -> None:
        """Initializes bullet."""

        super().__init__()
        self.start_pos = pygame.Vector2(start_pos)
        self.velocity = pygame.Vector2(velocity)
        self.rect = Bullet.image.get_rect(center=start_pos)

    def update(self) -> None:
        """Adds bullet's velocity to position, thus moving it."""

        self.rect.move_ip(self.velocity)

        if not self.rect.colliderect(
            Bullet.bounding_box
        ):  # if bullet gets out of the bounding box, in this case the window, kill it
            self.kill()
