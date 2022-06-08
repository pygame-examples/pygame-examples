"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import time

import pygame


def float_scale(surf: pygame.Surface, scale: float) -> pygame.Surface:
    w, h = surf.get_size()
    return pygame.transform.scale(surf, (w * scale, h * scale))


class Time:
    """
    Class to check if time has passed.
    """

    def __init__(self, time_to_pass: float):
        self.time_to_pass = time_to_pass
        self.start = time.perf_counter()

    def update(self) -> bool:
        if time.perf_counter() - self.start > self.time_to_pass:
            self.start = time.perf_counter()
            return True
        return False
