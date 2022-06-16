"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio
from typing import List

import pygame

from . import common
from .player import Player
from .tile import Tile


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.display = pygame.display.set_mode(common.DIMENSIONS)
        pygame.display.set_caption("Platformer Collisions Example")

        self.clock = pygame.time.Clock()
        self.key_presses = {"a": False, "d": False}
        self.player = Player(x=100, y=100, width=64, height=45, color=(255, 0, 0))

        self.running = True

    def render_map(self, display: pygame.Surface, tiles: List[Tile]) -> None:
        """
        Renders the games tiles
        """

        for tile in tiles:
            pygame.draw.rect(self.display, (60, 255, 100), tile.rect)

    async def main(self) -> None:
        """
        Game main function. Handles key presses, map and player rendering
        """
        while self.running:
            self.display.fill(pygame.Color("black"))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player.is_on_ground:
                            self.player.y_velocity -= self.player.JUMP_HEIGHT

            keys = pygame.key.get_pressed()
            self.key_presses["a"] = keys[pygame.K_a]
            self.key_presses["d"] = keys[pygame.K_d]

            self.player.handle_movement(self.key_presses)
            self.player.draw(self.display)

            self.render_map(self.display, common.tiles)

            pygame.display.flip()
            await asyncio.sleep(0)
            self.clock.tick(common.FPS)

    def run(self) -> None:
        """
        Run the main loop; using asyncio for WASM compatibility
        """

        asyncio.run(self.main())
