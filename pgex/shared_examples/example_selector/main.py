"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame
import pygame_gui
from pgex.common import PGEX_DIR

pygame.init()


class Game:
    """
    Handle flow in pygame application
    """

    SCREEN_SIZE = (500, 500)
    FPS_CAP = 120
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font(None, 40)

    def __init__(self):
        pygame.display.set_caption("Example Selector")
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE, pygame.SCALED)
        from .particles import ParticleManager
        self.ui_manager = pygame_gui.UIManager(self.SCREEN_SIZE, theme_path=PGEX_DIR / "shared_examples"
                                                                                       "/example_selector/theme.json")

        self.background = pygame.Surface(self.SCREEN_SIZE)
        self.background_rect = self.background.get_rect()
        self.background.fill(self.ui_manager.ui_theme.get_colour('dark_bg'))

        button_layout_rect = pygame.Rect(0, 250, 150, 40)
        button_layout_rect.centerx = self.background_rect.centerx
        self.run_btn = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                    text='Run',
                                                    manager=self.ui_manager)
        self.run_btn = pygame_gui.elements.UIButton(relative_rect=button_layout_rect.move(0, 60),
                                                    text='View',
                                                    manager=self.ui_manager)

        rect = pygame.Rect(100, 100, 140, 50)
        rect.centerx = self.background_rect.centerx
        self.text_box = pygame_gui.elements.UITextBox(
            html_text="PYGAME EXAMPLES",
            relative_rect=rect,
            manager=self.ui_manager)
        self.text_box.set_active_effect(pygame_gui.TEXT_EFFECT_BOUNCE, effect_tag='test')
        self.main_menu_particles = ParticleManager()

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
        asyncio.run(self._run())

    async def _run(self) -> None:
        while True:
            event_info = self.get_events()
            for event in event_info["events"]:
                if event.type == pygame.QUIT:
                    raise SystemExit

                self.ui_manager.process_events(event)

            self.main_menu_particles.update(event_info["dt"])
            self.ui_manager.update(event_info["dt"])
            self.screen.blit(self.background, (0, 0))
            self.main_menu_particles.draw(self.screen)
            self.ui_manager.draw_ui(self.screen)

            self.CLOCK.tick(self.FPS_CAP)
            pygame.display.flip()
            await asyncio.sleep(0)
