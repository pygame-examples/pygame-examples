"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import math
import typing as t

import pygame


class HorizontalSlider:
    def __init__(
        self,
        rect: pygame.Rect,
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        callback: callable = lambda _: None,
    ):
        self.min_value = min_value
        self.max_value = max_value
        self.range = max_value - min_value
        self.step = min(self.range, max(step, self.range // rect.width))
        self.callback = callback
        self.rail = rect.inflate(0, -0.8 * rect.height)
        # here the button will be a circle so circle collision detection will be done
        # but the concept applies to rectangles as well, just use `colliderect`
        # and a `pygame.Rect` here, you can inflate it as above to be a fraction of the length
        # you also wouldn't need `self.x` and `self.y`
        self.x, self.y = rect.center
        self.radius = int(rect.width * 0.05)
        # self.button = (rect.center, self.radius)  # (center, radius)
        self.clicked = False
        self.prev_value = 0

    def update(self, events: list) -> None:
        for event in events:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.collision(event.pos)
            ):
                self.clicked = True
            elif (
                event.type == pygame.MOUSEBUTTONUP
                and event.button == 1
                and self.clicked
            ):
                self.clicked = False
                value = self.value
                if self.prev_value != value:
                    self.prev_value = value

            elif event.type == pygame.MOUSEMOTION and self.clicked:
                self.x, self.y = self.clamp_rail(event.pos)
                self.value = round(self.value / self.step) * self.step

    def collision(self, pos: t.Tuple[int, int]) -> bool:
        """This is to detect point-circle collision, not needed for doing rect collisions."""
        mx, my = pos
        dx, dy = abs(self.x - mx), abs(self.y - my)
        if math.sqrt(dx**2 + dy**2) <= self.radius:
            return True
        return False

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, "grey50", self.rail)
        pygame.draw.circle(surface, "grey75", (self.x, self.y), self.radius)

    def clamp_rail(self, pos: t.Tuple[int, int]) -> t.Tuple[int, int]:
        x, y = pos
        new_x = max(self.rail.left + self.radius, min(x, self.rail.right - self.radius))
        return new_x, self.rail.centery

    @property
    def value(self) -> int:
        distance = self.x - (
            self.rail.left + self.radius
        )  # self.button.centerx in case of a rectangle
        rel_val = distance / (
            self.rail.width - 2 * self.radius
        )  # self.button.width instead of diameter for a rectangle
        value = self.min_value + round((self.range * rel_val) / self.step) * self.step
        return value

    @value.setter
    def value(self, value: int) -> None:
        value = value and round(value / self.step) * self.step - self.min_value
        rel_val = value / self.range
        new_rel_pos = round(
            rel_val * (self.rail.width - 2 * self.radius)
        )  # look at value property `rel_val`
        self.x = new_rel_pos + self.rail.left + self.radius
        value += self.min_value
        self.prev_value = value
        self.callback(value)
