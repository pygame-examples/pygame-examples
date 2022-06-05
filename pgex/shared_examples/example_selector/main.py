"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame
import pygame_gui

from pgex.common import EXAMPLES_DIR, PGEX_DIR

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

        self.ui_manager = pygame_gui.UIManager(
            self.SCREEN_SIZE,
            theme_path=PGEX_DIR / "shared_examples"
            "/example_selector/theme.json",
        )

        self.background = pygame.Surface(self.SCREEN_SIZE)
        self.background_rect = self.background.get_rect()
        self.background.fill(self.ui_manager.ui_theme.get_colour("dark_bg"))

        self.title_surf = self.FONT.render("PYGAME EXAMPLES", True, (200, 200, 200))
        self.t_rect = self.title_surf.get_rect(center=(self.background_rect.centerx, 140))

        self.main_menu_particles = ParticleManager()
        self.example_buttons = []
        self.create_ui()

    def create_ui(self):
        example_names = [i.name for i in EXAMPLES_DIR.iterdir()]

        for index, name in enumerate(example_names):
            btn_size = 150, 40
            btn_pad_y = 10
            btn_rect = pygame.Rect(
                (0, 0),
                btn_size,
            )
            btn_rect.center = (
                    self.background_rect.centerx,
                    ((btn_size[1] + btn_pad_y) * index)
                    + self.background_rect.centery - 30,
                )
            btn = pygame_gui.elements.UIButton(
                relative_rect=btn_rect, text=name, manager=self.ui_manager
            )
            self.example_buttons.append(btn)

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

                elif event.type == pygame.MOUSEWHEEL:
                    for btn in self.example_buttons:
                        change = (event.y * 30) * event_info["dt"]
                        btn.set_position((btn.rect.x, btn.rect.y + change))

                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    for btn in self.example_buttons:
                        if event.ui_element == btn:
                            print(btn.text)

                self.ui_manager.process_events(event)

            self.main_menu_particles.update(event_info["dt"])
            self.ui_manager.update(event_info["dt"])

            # Rendering
            self.screen.blit(self.background, (0, 0))
            self.main_menu_particles.draw(self.screen)
            self.screen.blit(self.title_surf, self.t_rect)
            self.ui_manager.draw_ui(self.screen)

            self.CLOCK.tick(self.FPS_CAP)
            pygame.display.flip()
            await asyncio.sleep(0)
