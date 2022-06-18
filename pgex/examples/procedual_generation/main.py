"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from .gui import GuiManager, Slider, Text
from .world import World


class Game:
    FPS = 60

    def __init__(self) -> None:
        self.display = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Procedual Generation Example")

        self.running = True

        self.offset_x = 0
        self.offset_y = 0

        self.mouse_x = 0
        self.mouse_y = 0

        self.clicking = False

        self.world = World(freq=250, width=600, height=600, tile_size=8)

        self.gui_manager = GuiManager(
            [
                Slider(x=10, y=30),
                Text(x=5, y=5, text="Beach Amount", size=32),
                Slider(x=10, y=65),
                Text(x=5, y=40, text="Water Amount", size=32),
                Slider(x=10, y=100),
                Text(x=5, y=75, text="Mountains", size=32),
                Slider(x=10, y=135),
                Text(x=5, y=110, text="Snow", size=32),
            ]
        )

        self.events: list = None

    def handle_gui(self) -> None:
        """
        Handles gui rendering and passes slider values to World
        """

        pygame.draw.rect(self.display, (50, 50, 50), (0, 0, 180, 160))
        self.gui_manager.draw_gui_elements(self.display, self.events)

        self.world.beach_amount = -self.gui_manager.get_element(0).get_value()
        self.world.ocean_amount = self.gui_manager.get_element(2).get_value()
        self.world.mountains = -self.gui_manager.get_element(4).get_value()
        self.world.snow = -self.gui_manager.get_element(6).get_value()

    def mouse_drag(self) -> None:
        """
        Handle mouse dragging
        """

        if self.clicking:
            if abs(pygame.mouse.get_pos()[0] - self.mouse_x) and abs(
                pygame.mouse.get_pos()[1] - self.mouse_y
            ):
                self.world.offset_x -= (pygame.mouse.get_pos()[0] - self.mouse_x) / 5000
                self.world.offset_y -= (pygame.mouse.get_pos()[1] - self.mouse_y) / 5000

                self.world.generate_map()

    async def main(self) -> None:
        """
        Main function, handles rendering, events, etc
        """

        while self.running:
            self.display.fill(pygame.Color("black"))

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False

            self.mouse_drag()
            self.world.render_map(self.display)
            self.handle_gui()

            pygame.display.flip()
            await asyncio.sleep(0)
            self.clock.tick(60)

    def run(self) -> None:
        """
        Runs the main loop
        """

        self.world.generate_map()
        asyncio.run(self.main())
