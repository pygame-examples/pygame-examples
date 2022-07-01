"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame
from ._types import Point


class Darkener:
    def __init__(
        self,
        base_surf: pygame.Surface,
        radius: int,
        darken_ratio: float,
    ) -> None:

        if darken_ratio > 1 or darken_ratio < 0:
            raise ValueError("darken_ratio must be between 0 and 1")

        self.radius = radius
        self.darken_ratio = darken_ratio

        self.base = base_surf
        self.size = base_surf.get_size()
        self.rect = base_surf.get_rect()

    def get_dark_surface(self, center: Point) -> pygame.Surface:
        if not isinstance(center, pygame.Vector2):
            center = pygame.Vector2(center)

        dark_color = (0, 0, 0, 255 * self.darken_ratio)

        dark_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        dark_surface.fill(dark_color)

        important_rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        important_rect.center = center

        try:
            self.subsurface = dark_surface.subsurface(important_rect)
        except ValueError:
            return dark_surface

        self.get_bright_pixels()
        return dark_surface

    def get_bright_pixels(self):
        pixels = pygame.surfarray.pixels_alpha(self.subsurface)
        central_point = pygame.Vector2(self.radius, self.radius)
        for row in range(self.radius * 2):
            for col in range(self.radius * 2):
                dest = pygame.Vector2(row, col)
                distance = central_point.distance_to(dest)
                if distance <= self.radius:
                    gradient = self.darken_ratio / self.radius
                    pixels[row][col] = 255 * gradient * distance

    def update(self, center: Point):
        self.dark_surf = self.get_dark_surface(center)

    def draw(self, screen: pygame.Surface, dest_rect: pygame.Rect):
        self.surface = self.base.copy()
        self.surface.blit(self.dark_surf, self.rect)
        screen.blit(self.surface, dest_rect)
