import asyncio

import pygame

from .enums import GameStates
from .scenes import CharacterMenu, GamePlay, MainMenu


class Game:
    current_state: GameStates

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.clock = pygame.time.Clock()
        self.running = True
        self.set_state(GameStates.MAIN_MENU)
        self.states = {
            GameStates.MAIN_MENU: MainMenu(self.set_state),
            GameStates.CHARACTER_MENU: CharacterMenu(self.set_state),
            GameStates.GAMEPLAY: GamePlay(self.set_state),
        }

    def run(self):
        asyncio.run(self._run())

    async def _run(self):
        while self.running:
            self._process()
            await asyncio.sleep(0)

    def _process(self):
        self.clock.tick(60)
        self.screen.fill("grey10")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        scene = self.states.get(self.current_state, None)
        if scene is not None:
            scene.show(self.screen)

        pygame.display.flip()

    @classmethod
    def set_state(cls, state: GameStates) -> None:
        cls.current_state = state
