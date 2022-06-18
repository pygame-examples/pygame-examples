"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

from abc import ABC, abstractmethod
from typing import List

import pygame

pygame.font.init()


class UIElement(ABC):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def handle_events(self, events: list) -> None:
        pass

    @abstractmethod
    def draw(self, display: pygame.Surface) -> None:
        pass


class GuiManager:
    def __init__(self, gui_elements: List[UIElement]) -> None:
        self.gui_elements = gui_elements

    def get_element(self, index: int) -> UIElement:
        """
        Returns the element at the given index
        """

        return self.gui_elements[index]

    def draw_gui_elements(self, display: pygame.Surface, events: list) -> None:
        """
        Draws each ui element
        """

        for element in self.gui_elements:
            element.handle_events(events)
            element.draw(display)


class Text(UIElement):
    def __init__(self, x: int, y: int, text: str, size: int) -> None:
        super().__init__(x, y)
        self.size = size

        self.font = pygame.font.SysFont("monospace.ttf", self.size)
        self.text = self.font.render(text, True, (0, 0, 0))

    def draw(self, display: pygame.Surface) -> None:
        """
        Renders text
        """

        display.blit(self.text, (self.x, self.y))


class Slider(UIElement):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.pointer_x = x
        self.pointer_y = y

        self.clicking = False
        self.clicked_mouse_x = 0

    def handle_events(self, events: list) -> None:
        """
        Handles movement of slider
        """

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.Rect(
                        self.pointer_x - 5, self.pointer_y, 10, 10
                    ).collidepoint(pygame.mouse.get_pos()):
                        self.clicking = True
                        self.clicked_mouse_x = pygame.mouse.get_pos()[0]

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicking = False

    def get_value(self) -> float:
        clamp = lambda smallest, n, largest: sorted([smallest, n, largest])[1]
        return clamp(-1.0, ((self.pointer_x - self.x) / 100) - 1, 1.0)

    def draw(self, display: pygame.Surface) -> None:
        current_mouse_x = pygame.mouse.get_pos()[0]
        if self.clicking:
            if (
                self.pointer_x < self.x + 99
                and self.clicked_mouse_x - current_mouse_x < 0
                or self.pointer_x > self.x - 1
                and self.clicked_mouse_x - current_mouse_x > 0
            ):
                self.pointer_x -= (self.clicked_mouse_x - current_mouse_x) / 25
        pygame.draw.rect(display, (100, 100, 100), (self.x, self.y, 100, 8))
        pygame.draw.circle(
            display, (255, 0, 0), (self.pointer_x, self.pointer_y + 4), 5
        )
