"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import random
from typing import Tuple

import pygame
from noise import snoise2, snoise3

from . import colors


class World:
    def __init__(self, freq: float, width: int, height: int, tile_size: int) -> None:
        self.freq = freq
        self.width = width
        self.height = height
        self.tile_size = tile_size

        self.map_data = []
        self.biome_data = []

        self.seed = random.randrange(-100000, 1000000)

        self.offset_x = 0
        self.offset_y = 0

        self.beach_amount = 0.3
        self.ocean_amount = -1
        self.mountains = 0.7
        self.snow = 0.3

    def generate_map(self) -> None:
        """
        Generates the map with the specified parameters. Also used ot regerate the map
        """

        self.map_data = []
        self.biome_data = []
        for index_x, x in enumerate(range(0, self.width, self.tile_size)):
            for index_y, y in enumerate(range(0, self.height, self.tile_size)):
                height_map = snoise3(
                    (x / self.freq) + self.offset_x,
                    (y / self.freq) + self.offset_y,
                    self.seed,
                )
                self.map_data.append(height_map)
                self.biome_data.append(
                    snoise3(
                        (x / 1000) + self.offset_x / 4,
                        (y / 1000) + self.offset_y / 4,
                        self.seed,
                    )
                )

    def determine_block_type(
        self, height_map: int, biome_height_map: int
    ) -> Tuple[int, int, int]:
        """
        Determines the color of the block at a specified position
        """

        color: Tuple[int, int, int] = None
        if height_map > self.ocean_amount:
            if height_map > self.mountains:
                color = colors.MOUNTAIN_COLOR
                if (
                    height_map > self.mountains + self.snow
                    and biome_height_map > -self.beach_amount
                ):
                    color = colors.SNOW_COLOR
            elif biome_height_map > -self.beach_amount:
                color = colors.GRASS_COLOR
            else:
                color = colors.BEACH_COLOR
        else:
            color = colors.WATER_COLOR

        return color

    def render_map(self, display: pygame.Surface) -> None:
        """
        Renders the map data
        """

        i = 0
        for x in range(0, self.width, self.tile_size):
            for y in range(0, self.height, self.tile_size):
                height = self.map_data[i]
                biome_height_map = self.biome_data[i]
                color = self.determine_block_type(height, biome_height_map)
                pygame.draw.rect(display, color, (x, y, self.tile_size, self.tile_size))
                i += 1
