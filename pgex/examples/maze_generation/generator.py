"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""


import random

import numpy
import pygame

from ._types import Array, _SeedValue
from .tile import Tile


class Generator:
    def __init__(self, size: Array, tilesize: int, seed: _SeedValue = None) -> None:
        random.seed(seed)  # sets the seed for the random number generator

        if not isinstance(size, pygame.Vector2):
            size = pygame.Vector2(size)
        self.size = size

        self.surface = None
        self.rect = pygame.Rect(0, 0, *size)

        self.pixel_size = size
        self.tilesize = tilesize

        self.width = int(self.pixel_size[0] / self.tilesize)
        self.height = int(self.pixel_size[1] / self.tilesize)

        self.map = numpy.zeros((self.height, self.width))
        self.tiles = [
            [
                Tile(tilesize, pygame.Vector2(c, r) * tilesize, "black")
                for c in range(self.width)
            ]
            for r in range(self.height)
        ]

        self.unvisited = [
            pygame.Vector2(c, r) for r in range(self.height) for c in range(self.width)
        ]
        self.definite_walls = []
        # 0 means wall, 1 means floor
        self.walls = []
        self.offsets = [
            pygame.Vector2(1, 0),
            pygame.Vector2(-1, 0),
            pygame.Vector2(0, 1),
            pygame.Vector2(0, -1),
        ]

        self.start()

    def start(self) -> None:
        start_point = (
            random.randint(0, self.height - 1),
            random.randint(0, self.width - 1),
        )
        self.map[start_point[0]][start_point[1]] = 1
        self.unvisited.remove(pygame.Vector2(start_point[1], start_point[0]))

        self.add_walls(pygame.Vector2(start_point[1], start_point[0]))
        while len(self.walls):
            self.iterate()
        self.update_tiles()

    def add_walls(self, point: pygame.Vector2) -> None:
        candidates = [point + offset for offset in self.offsets]
        for candidate in candidates:
            if candidate.x < 0 or candidate.y < 0:
                continue

            elif candidate.x >= self.width:
                continue

            elif candidate.y >= self.height:
                continue

            elif candidate not in self.walls and candidate in self.unvisited:
                self.walls.append(candidate)

    def iterate(self) -> None:
        point = random.choice(self.walls)

        self.walls.remove(point)
        visited_neighbors = self.get_visited_neighbors(point)
        if visited_neighbors == 1 and not self.is_last_wall(point):
            self.map[int(point.y)][int(point.x)] = 1
            self.unvisited.remove(point)

            self.add_walls(point)
        else:
            self.definite_walls.append(point)

        return point

    def is_last_wall(self, point: pygame.Vector2) -> bool:
        all_walls = self.unvisited

        neighbors = [point + offset for offset in self.offsets]

        for neighbor in neighbors:
            count = 0
            adjacents = [neighbor + offset for offset in self.offsets]

            for adjacent in adjacents:
                if adjacent in all_walls:
                    count += 1

            if count <= 1:
                return True

        return False

    def get_visited_neighbors(self, point: pygame.Vector2):
        visited = 0
        candidates = [point + offset for offset in self.offsets]
        for candidate in candidates:
            if (
                0 <= candidate.x < self.width
                and 0 <= candidate.y < self.height
                and candidate not in self.unvisited
            ):
                visited += 1

        return visited

    def update_tiles(self) -> None:
        for i, row in enumerate(self.map):
            for j, val in enumerate(row):
                color = "white" if val else "black"
                self.tiles[i][j].change_color(color)

        self.surface = None

    def draw(self, screen) -> None:
        if self.surface is None:
            size = (int(self.size.x), int(self.size.y))
            self.surface = pygame.Surface(size)
            for row in self.tiles:
                for tile in row:
                    tile.draw(self.surface)

        screen.blit(self.surface, self.rect)
