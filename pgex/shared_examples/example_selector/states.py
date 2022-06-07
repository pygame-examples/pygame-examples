import pygame
from .particles import ParticleManager

import pygame_gui

import importlib
from pgex.common import EXAMPLES_DIR, PGEX_DIR
from .pg_init import SCREEN_SIZE
from enum import Enum, auto


class GameStates:
    MAIN_MENU = auto()
    EXAMPLE_STATE = auto()


class MainMenu:
    FONT = pygame.font.Font(None, 40)

    def __init__(self, covalent_info) -> None:
        self.screen = covalent_info.screen
        self.covalent_info = covalent_info
        self.ui_manager = pygame_gui.UIManager(
            SCREEN_SIZE,
            theme_path=PGEX_DIR / "shared_examples"
            "/example_selector/assets/theme.json",
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
        self.next_state = None
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
            if event.type == pygame.MOUSEWHEEL:
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
                        self.next_state = GameStates.EXAMPLE_STATE
                        self.covalent_info.example_name = btn.text

                        try:
                            stub = pygame.image.load(PGEX_DIR / "shared_examples"
                                    f"/example_selector/assets/{btn.text}.png").convert()

                            rect = pygame.Rect(0, 0, 217, 217)
                            rect.center = stub.get_rect().center 
                            self.covalent_info.example_picture = stub.subsurface(rect)
                        except Exception as e:
                            print(e)

            self.ui_manager.process_events(event)

        self.main_menu_particles.update(event_info["dt"])
        self.ui_manager.update(event_info["dt"])

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.main_menu_particles.draw(self.screen)
        self.screen.blit(self.title_surf, self.t_rect)
        self.ui_manager.draw_ui(self.screen)


class ExampleState:
    FONT = pygame.font.Font(None, 45)

    def __init__(self, covalent_info):
        self.covalent_info = covalent_info
        self.screen = self.covalent_info.screen
        self.next_state = None 
        self.ui_manager = pygame_gui.UIManager(
            SCREEN_SIZE,
            theme_path=PGEX_DIR / "shared_examples"
            "/example_selector/assets/theme.json",
        )

        self.background = pygame.Surface(SCREEN_SIZE)
        self.background_rect = self.background.get_rect()
        self.background.fill(self.ui_manager.ui_theme.get_colour("dark_bg"))

        btn_pos = 310, 60
        btn_size = 150, 40
        self.run_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(btn_pos, btn_size),
            text="Run",
            manager=self.ui_manager
        )
        self.view_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(btn_pos[0], btn_pos[1] + 10 + 40, *btn_size),
            text="View",
            manager=self.ui_manager
        )
        self.back_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(btn_pos[0] + 20, btn_pos[1] + 10 + 370,
             100, 30),
            text="Back",
            manager=self.ui_manager
        )

    def update(self):
        event_info = self.covalent_info.event_info
        for event in event_info["events"]:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.run_btn:
                    importlib.import_module(f"pgex.examples.{self.covalent_info.example_name}")
                    self.covalent_info.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.SCALED)
                if event.ui_element == self.back_btn:
                    self.next_state = GameStates.MAIN_MENU

            self.ui_manager.process_events(event)

        self.ui_manager.update(event_info["dt"])

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        text = self.FONT.render(self.covalent_info.example_name, True, (200, 200, 200))
        rect = text.get_rect()
        rect.centerx = self.background_rect.centerx
        rect.y = 10
        self.screen.blit(text, rect)
        self.screen.blit(self.covalent_info.example_picture, (20, 40))
        self.ui_manager.draw_ui(self.screen)

