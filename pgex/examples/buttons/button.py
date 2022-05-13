"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame


class Button:
    def __init__(self, x, y, width, height, text, text_color, bg_color, method=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("Arial", height)
        self.text_surf = self.font.render(text, False, text_color)

        self.color = bg_color
        self.text = text
        self.func = method

        self._is_pressed = False

    def draw(self, surface):
        """Draws the pygame.Rect and font"""
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(
            self.text_surf,
            pygame.Vector2(self.rect.center)
            - pygame.Vector2(self.text_surf.get_size()) / 2,
        )

    def update(self):
        """Must be called every frame."""
        if (
            self.rect.collidepoint(pygame.mouse.get_pos())
            and pygame.mouse.get_pressed()[0]
            and not self._is_pressed
        ):
            self.func()
            self._is_pressed = True

        elif (
            self.rect.collidepoint(pygame.mouse.get_pos())
            and not pygame.mouse.get_pressed()[0]
            and self._is_pressed
        ):
            self._is_pressed = False
