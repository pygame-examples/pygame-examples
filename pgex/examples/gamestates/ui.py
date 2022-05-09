"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame
from pygame.event import Event

from ._types import EventInfo


class AbstractButton:
    def __init__(self) -> None:
        pass


class Button:
    """
    Nice looking minimalistic button.
    """

    FONT = pygame.font.Font(None, 15)

    def __init__(self, pos: pygame.Vector2, title: str) -> None:
        self.pos = pos
        self.size = (170, 30)
        self.title = title
        self.clicked = False
        self.hover = False
        self.rect = pygame.Rect(self.pos, self.size)
        self.text_surf = self.FONT.render(title, True, "white")
        self.text_surf_rect = self.text_surf.get_rect(center=self.pos)
        self.text_surf_rect.center = self.rect.center
        self.hover_surf = pygame.Surface(self.size)
        self.hover_surf.fill((0, 75, 189))
        self.hover_surf.set_alpha(230)
        self.hover_surf_alpha = 0
        self.once = True

    def update(self, event_info: EventInfo):
        self.hover = self.rect.collidepoint(event_info["mouse pos"])
        if self.hover and self.hover_surf_alpha < 230:
            self.hover_surf_alpha += 7.4 * event_info["dt"]

        if not self.hover and self.hover_surf_alpha > 0:
            self.hover_surf_alpha -= 7.4 * event_info["dt"]

        # Cleanup
        if self.hover_surf_alpha > 230:
            self.hover_surf_alpha = 230
        if self.hover_surf_alpha < 0:
            self.hover_surf_alpha = 0

        for event in event_info["events"]:
            if self.hover and event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True

    def draw(self, screen: pygame.Surface):
        # Hover surface
        screen.blit(self.hover_surf, self.rect)
        self.hover_surf.set_alpha(self.hover_surf_alpha)

        if self.hover and self.once:
            self.once = False

        if not self.hover:
            self.once = True

        # Border
        pygame.draw.rect(screen, "white", self.rect, width=3)

        # Actual text
        screen.blit(self.text_surf, self.text_surf_rect)
