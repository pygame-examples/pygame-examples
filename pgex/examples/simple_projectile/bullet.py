"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame

from ._types import PositionLike, VelocityLike


class Bullet(pygame.sprite.Sprite):
    image = pygame.Surface((16, 16))
    image.fill("red")

    bounding_box = pygame.Rect(0, 0, 640, 360)

    def __init__(self, start_pos: PositionLike, velocity: VelocityLike) -> None:
        """Initializes bullet."""

        super().__init__()
        self.start_pos = pygame.Vector2(start_pos)
        self.velocity = pygame.Vector2(velocity)
        self.rect = self.image.get_rect(center=start_pos)

    def update(self) -> None:
        """Adds bullet's velocity to position, thus moving it."""

        self.rect.topleft += self.velocity
        if not self.rect.colliderect(
            self.bounding_box
        ):  # if bullet gets out of the bounding box, in this case the window, kill it, but the bounding box can be any size, it doesn't even necessarily have to exist, but for this example it exists.
            self.kill()
