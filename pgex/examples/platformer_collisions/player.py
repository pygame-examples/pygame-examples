"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

from typing import List

import pygame

from . import common
from .tile import Tile


class Player:
    SPEED = 4
    JUMP_HEIGHT = 16

    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.y_velocity = 3
        self.is_on_ground = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_colliding_tiles(
        self, tiles: List[Tile], player_rect: pygame.Rect
    ) -> List[Tile]:
        """
        Returns a list of tiles the player is currently colliding with
        """
        return_tiles = []
        for tile in tiles:
            if tile.collision(player_rect):
                return_tiles.append(tile)

        return tiles

    def calculate_rect(
        self, movement: dict, player_rect: pygame.Rect, map_tiles: List[Tile]
    ) -> pygame.Rect:
        """
        Calculates the Rect of the player based on their movement and the surrounding tiles
        """
        player_rect.x += movement["horizontal"]
        tiles = self.get_colliding_tiles(map_tiles, player_rect)
        for tile in tiles:
            if tile.collision(player_rect):
                if movement["horizontal"] > 0:
                    player_rect.right = tile.rect.left
                if movement["horizontal"] < 0:
                    player_rect.left = tile.rect.right

        self.is_on_ground = False
        player_rect.y += movement["vertical"]
        tiles = self.get_colliding_tiles(map_tiles, player_rect)
        for tile in tiles:
            if tile.collision(player_rect):
                if movement["vertical"] > 0:
                    player_rect.bottom = tile.rect.top
                    self.is_on_ground = True
                    self.y_velocity = 3
                if movement["vertical"] < 0:
                    player_rect.top = tile.rect.bottom

        return player_rect

    def handle_movement(self, key_presses: dict) -> pygame.Rect:
        """
        Handles all code relating to the movement of the player
        """

        player_movement = {"horizontal": 0, "vertical": self.y_velocity}

        if key_presses["a"]:
            player_movement["horizontal"] -= self.SPEED
        if key_presses["d"]:
            player_movement["horizontal"] += self.SPEED

        if self.y_velocity < 10:
            self.y_velocity += 0.5

        self.rect = self.calculate_rect(player_movement, self.rect, common.tiles)

    def draw(self, display) -> None:
        """
        Draws the player at the rect position
        """

        pygame.draw.rect(display, self.color, self.rect)
