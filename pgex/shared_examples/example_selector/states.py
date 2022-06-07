import pygame
from .particles import ParticleManager

import pygame_gui

from pgex.common import EXAMPLES_DIR, PGEX_DIR
from .pg_init import SCREEN_SIZE


class MainMenu:
    FONT = pygame.font.Font(None, 40)

    def __init__(self, covalent_info) -> None:
        self.screen = covalent_info.screen
        self.covalent_info = covalent_info
        self.ui_manager = pygame_gui.UIManager(
            SCREEN_SIZE,
            theme_path=PGEX_DIR / "shared_examples"
            "/example_selector/theme.json",
        )

        self.background = pygame.Surface(SCREEN_SIZE)
        self.background_rect = self.background.get_rect()
        self.background.fill(self.ui_manager.ui_theme.get_colour("dark_bg"))

        self.title_surf = self.FONT.render(
            "PYGAME EXAMPLES", True, (200, 200, 200)
        )
        self.t_rect = self.title_surf.get_rect(
            center=(self.background_rect.centerx, 140)
        )

        self.main_menu_particles = ParticleManager()
        self.example_buttons = []
        self.title_surf_alpha = 255
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
                + self.background_rect.centery
                - 30,
            )
            btn = pygame_gui.elements.UIButton(
                relative_rect=btn_rect, text=name, manager=self.ui_manager
            )
            self.example_buttons.append(btn)

    def update(self):
        event_info = self.covalent_info.event_info
        for event in event_info["events"]:
            if event.type == pygame.VIDEORESIZE:
                print(event.type)
                # 8192
            if event.type == pygame.QUIT:
                raise SystemExit

            elif event.type == pygame.MOUSEWHEEL:
                if 0 <= self.title_surf_alpha <= 256:
                    self.title_surf_alpha += (event.y * 20) * event_info["dt"]
                elif self.title_surf_alpha < 0:
                    self.title_surf_alpha = 0
                elif self.title_surf_alpha > 256:
                    self.title_surf_alpha = 255
                self.title_surf.set_alpha(self.title_surf_alpha)

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

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.main_menu_particles.draw(self.screen)
        self.screen.blit(self.title_surf, self.t_rect)
        self.ui_manager.draw_ui(self.screen)


