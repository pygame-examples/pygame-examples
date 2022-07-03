"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""


import pygame
from ._types import Array, _ColorValue


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_size: int, pos: Array, color: _ColorValue) -> None:
        super().__init__()

        if not isinstance(pos, pygame.Vector2):
            pos = pygame.Vector2(pos)

        self.tile_size = tile_size
        self.color = color
        self.pos = pos

        self.set_rect()

    def set_rect(self):
        self.rect = pygame.Rect(
            self.pos.x, self.pos.y, self.tile_size, self.tile_size
        )

    def change_color(self, new_color: _ColorValue) -> None:
        self.color = new_color

    def change_pos(self, new_pos: Array) -> None:
        if not isinstance(new_pos, pygame.Vector2):
            self.pos = pygame.Vector2(new_pos)
            return

        self.pos = new_pos
        self.set_rect()

    def change_size(self, new_tile_size: int):
        self.tile_size = new_tile_size
        self.set_rect()

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
