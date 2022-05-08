"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import pygame

from .characters import characters
from .enums import GameStates
from .player import player
from .UI import Button, CarouselMenu, Text, UIGroup


class Scene:
    def __init__(self, *groups):
        self.groups = groups

    def show(self, surface: pygame.Surface) -> None:
        self.update()
        for group in self.groups:
            group.draw(surface)

    def update(self) -> None:
        for group in self.groups:
            group.update()


class MainMenu(Scene):
    def __init__(self, set_state: callable) -> None:
        btn_config = [
            {
                "pos": (250, 125),
                "size": (300, 100),
                "bg": "navy",
                "text": "Play",
                "callback": lambda: set_state(GameStates.GAMEPLAY),
            },
            {
                "pos": (250, 275),
                "size": (300, 100),
                "bg": "brown",
                "text": "Characters",
                "callback": lambda: set_state(GameStates.CHARACTER_MENU),
            },
        ]
        buttons = UIGroup(btn_config, Button)

        txt_config = [
            {
                "pos": (400, 75),
                "angle": -30,
                "fg": "yellow",
                "text_var": lambda: player.character.name,
            }
        ]
        texts = UIGroup(txt_config, Text)

        super().__init__(buttons, texts)


class CharacterMenu(Scene):
    def __init__(self, set_state: callable) -> None:
        menu = CarouselMenu((250, 200), characters, (128, 128))
        menu_group = pygame.sprite.GroupSingle()
        menu_group.add(menu)

        btn_config = [
            {
                "pos": (50, 200),
                "size": (50, 30),
                "bg": "grey50",
                "text": "<<<",
                "callback": lambda: menu.prev(),
            },
            {
                "pos": (450, 200),
                "size": (50, 30),
                "bg": "grey50",
                "text": ">>>",
                "callback": lambda: menu.next(),
            },
            {
                "pos": (250, 350),
                "size": (100, 50),
                "bg": "darkgreen",
                "text": "Select",
                "callback": lambda: (
                    player.set_character(menu.current_item),
                    set_state(GameStates.MAIN_MENU),
                ),
            },
        ]
        buttons = UIGroup(btn_config, Button)

        txt_config = [
            {
                "pos": (250, 50),
                "fg": "yellow",
                "text_var": lambda: menu.current_item.name,
            }
        ]
        texts = UIGroup(txt_config, Text)
        super().__init__(buttons, texts, menu_group)


class GamePlay(Scene):
    def __init__(self, set_state: callable) -> None:
        self.set_state = set_state
        player_group = pygame.sprite.GroupSingle()
        player_group.add(player)
        super().__init__(player_group)

    def show(self, surface: pygame.Surface):
        super().show(surface)
        if not player.alive:
            player.reset()
            self.set_state(GameStates.MAIN_MENU)
