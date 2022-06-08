"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

# import asyncio

from dataclasses import dataclass

import pygame

from .pg_init import screen
from .states import ExampleState, GameStates, MainMenu


@dataclass
class CovalentInfo:
    screen: pygame.Surface
    event_info: dict
    example_picture: pygame.Surface = pygame.Surface((217, 217))
    example_name: str = ""


class Game:
    """
    Handle flow in pygame application
    """

    SCREEN_SIZE = (500, 500)
    FPS_CAP = 120
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font(None, 40)

    def __init__(self):
        self.screen = screen
        self.covalent_info = CovalentInfo(screen, self.get_events())
        self.states = {
            GameStates.MAIN_MENU: MainMenu(self.covalent_info),
            GameStates.EXAMPLE_STATE: ExampleState(self.covalent_info),
        }
        self.current_state = GameStates.MAIN_MENU

    def get_events(self) -> dict:
        """
        Returns necessary events for application. Packed in a dictionary.
        """

        events = pygame.event.get()
        mouse_press = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        raw_dt = self.CLOCK.get_time() / 1000
        dt = raw_dt * 100

        return {
            "events": events,
            "mouse press": mouse_press,
            "keys": keys,
            "mouse pos": mouse_pos,
            "raw dt": raw_dt,
            "dt": dt,
        }

    def run(self) -> None:
        while True:
            event_info = self.get_events()
            for event in event_info["events"]:
                if event.type == pygame.QUIT:
                    raise SystemExit

            self.covalent_info.event_info = event_info

            self.states[self.current_state].update()
            self.screen.fill("black")
            self.states[self.current_state].draw()

            if (
                state := self.states[self.current_state].next_state
            ) is not None:
                self.current_state = state
                for g in self.states.values():
                    if g == self.states[self.current_state]:
                        continue

                    g.next_state = None

            self.CLOCK.tick(self.FPS_CAP)
            pygame.display.flip()
