"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

An example that showcases how different states
can be handled in your pygame application.
Compatible with WASM.

Contains states of:
	- Main Menu
	- Game
"""
import asyncio

import pygame

from ._types import EventInfo
from .states import MainMenu


class Game:
    """
    Handle flow in pygame application
    """

    SCREEN_SIZE = (700, 330)
    FPS_CAP = 120
    CLOCK = pygame.time.Clock()

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.current_game_state = MainMenu(self.screen)

    def get_events(self) -> EventInfo:
        """
        Returns necessary events for application. Packed in a dictionary.
        """

        events = pygame.event.get()
        mouse_press = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        raw_dt = self.CLOCK.get_time()
        dt = raw_dt * self.FPS_CAP

        return {
            "events": events,
            "mouse press": mouse_press,
            "keys": keys,
            "mouse pos": mouse_pos,
            "raw dt": raw_dt,
            "dt": dt,
        }

    def run(self) -> None:
        asyncio.run(self._run())

    async def _run(self) -> None:
        while True:
            event_info = self.get_events()
            for event in event_info["events"]:
                if event.type == pygame.QUIT:
                    raise SystemExit

            self.current_game_state.update(event_info)
            if self.current_game_state.is_over:
                self.current_game_state = (
                    self.current_game_state.next_game_state()(self.screen)
                )

            self.screen.fill("black")
            self.current_game_state.draw()

            self.CLOCK.tick(self.FPS_CAP)
            pygame.display.flip()
            await asyncio.sleep(0)


if __name__ == "__main__":
    game = Game()
    game.run()
