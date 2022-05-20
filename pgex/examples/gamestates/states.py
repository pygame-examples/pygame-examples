"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

from abc import ABC, abstractmethod
from typing import Any

import pygame

from ._types import EventInfo
from .ui import Button


class GameState(ABC):
    """
    Abstract Base Class for Game States.
    """

    # You pass in `None` to use the default font
    FONT = pygame.font.Font(None, 50)

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.is_over = False

    @abstractmethod
    def update(self, event_info: EventInfo) -> None:
        pass

    @abstractmethod
    def next_game_state(self) -> Any:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


class MainGame(GameState):
    """
    Main Game play for the game. Includes a button to go back to the
    main menu.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.text = self.FONT.render("MAIN GAME", False, "white")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen.get_rect().center
        self.main_menu_btn = Button(pygame.Vector2(260, 200), "MAIN MENU")

    def update(self, event_info: EventInfo) -> None:
        self.main_menu_btn.update(event_info)
        if self.main_menu_btn.clicked:
            self.is_over = True

    def next_game_state(self) -> Any:
        return MainMenu

    def draw(self) -> None:
        self.screen.blit(self.text, (self.text_rect.x, 100))
        self.main_menu_btn.draw(self.screen)


class MainMenu(GameState):
    """
    Main Menu for game.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.text = self.FONT.render("MAIN MENU", False, "white")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen.get_rect().center
        self.start_btn = Button(pygame.Vector2(260, 200), "START")

    def update(self, event_info: EventInfo) -> None:
        self.start_btn.update(event_info)
        if self.start_btn.clicked:
            self.is_over = True

    def next_game_state(self):
        return MainGame

    def draw(self) -> None:
        self.screen.blit(self.text, (self.text_rect.x, 100))
        self.start_btn.draw(self.screen)
