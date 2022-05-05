import functools
from typing import List, Optional, Tuple, Union
import pygame


@functools.lru_cache(maxsize=32)
def _font_loader(name, size):
    return pygame.font.Font(name, size)


class Button(pygame.sprite.Sprite):
    def __init__(self, dct: dict) -> None:
        super().__init__()
        size = dct.get("size", (1, 1))
        pos = dct.get("pos", (0, 0))
        font = _font_loader(*dct.get("font", (None, 32)))
        bg = dct.get("bg", "black")
        fg = dct.get("fg", "white")
        text = dct.get("text", "")
        self.callback = dct.get("callback", lambda: None)
        self.clicked = False
        self.ready = False

        self.image = pygame.Surface(size)
        self.image.fill(bg)
        self.rect = self.image.get_rect()

        text_surf = font.render(text, True, fg)
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.image.blit(text_surf, text_rect)
        self.rect.center = pos

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        left, *_ = pygame.mouse.get_pressed()
        collision = self.rect.collidepoint(mouse_pos)
        if left and not self.clicked:
            self.clicked = True
            if collision:
                self.ready = True
            elif not collision:
                self.ready = False
        if not left:
            self.clicked = False
            if collision and self.ready:
                self.callback()
            self.ready = False


class Text(pygame.sprite.Sprite):
    def __init__(self, dct: dict) -> None:
        super().__init__()
        self.pos = dct.get("pos", (0, 0))
        self.font = _font_loader(*dct.get("font", (None, 32)))
        self.fg = dct.get("fg", "white")
        text = dct.get("text", "aaaaaaaaaa")
        self.angle = dct.get("angle", 0)
        self.text_var = dct.get("text_var", None)

        text_surf = self.font.render(text, True, self.fg)
        self.image = pygame.transform.rotate(text_surf, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        if self.text_var is not None:
            text_surf = self.font.render(self.text_var(), True, self.fg)
            self.image = pygame.transform.rotate(text_surf, self.angle)
            self.rect = self.image.get_rect(center=self.pos)


class UIGroup(pygame.sprite.Group):
    def __init__(self, config: List[dict], element) -> None:
        super().__init__()
        self.element = element
        self.parse_config(config)

    def parse_config(self, config: List[dict]) -> None:
        for dct in config:
            element = self.element(dct)
            self.add(element)


class CarouselMenu(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: Union[Tuple[int, int], List[int]],
        lst: List,
        size: Optional[Union[Tuple[int, int], List[int]]] = None,
    ) -> None:
        super().__init__()
        self.pos = pos
        self.size = size
        self.lst = lst
        self.index = 0
        self.image = self.lst[self.index].image
        if self.size is not None:
            self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=self.pos)

    @property
    def current_item(self):
        return self[self.index]

    def __getitem__(self, index):
        return self.lst[index]

    def next(self) -> None:
        self.index += 1
        if self.index >= len(self.lst):
            self.index = 0

    def prev(self) -> None:
        self.index -= 1
        if self.index < 0:
            self.index = len(self.lst) - 1

    def update(self) -> None:
        self.image = self.current_item.image
        if self.size is not None:
            self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=self.pos)
