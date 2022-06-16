"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
from typing import Tuple

import pygame

from .entity import Entity


class Game:
    FPS = 60
    DIMENSIONS = (600, 600)
    CAPTION = "Move Towards Mouse Example"

    def __init__(self) -> None:
        self.display = pygame.display.set_mode(self.DIMENSIONS)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(self.CAPTION)

        self.running = True

        self.entity = Entity(
            x=100, y=100, width=64, height=64, speed=7, color=(255, 0, 0)
        )

    def get_mouse_position(self) -> Tuple[int, int]:
        """
        Returns mouse position
        """

        return pygame.mouse.get_pos()

    async def main(self) -> None:
        """
        Game main loop. Handles events, rendering etc
        """

        while self.running:
            self.display.fill(pygame.Color("black"))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.entity.move_towards(*self.get_mouse_position())
            self.entity.draw(self.display)

            pygame.display.flip()
            self.clock.tick(self.FPS)
            await asyncio.sleep(0)

    def run(self) -> None:
        """
        Run the main loop
        """

        asyncio.run(self.main())
