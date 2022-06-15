"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from . import common


def get_colliding_tiles(tiles: list, player_rect: pygame.Rect) -> list:
    """
    Returns a list of tiles the player is currently colliding with
    """
    return_tiles = []
    for tile in tiles:
        if player_rect.colliderect(tile):
            return_tiles.append(tile)

    return tiles


def calculate_rect(
    movement: list, player_rect: pygame.Rect, map_tiles: list
) -> pygame.Rect:
    """
    Calculates the Rect of the player based on their movement and the surrounding tiles
    """
    player_rect.x += movement[0]
    tiles = get_colliding_tiles(map_tiles, player_rect)
    for tile in tiles:
        if player_rect.colliderect(tile):
            if movement[0] > 0:
                player_rect.right = pygame.Rect(tile[0], tile[1], tile[2], tile[3]).left
            if movement[0] < 0:
                player_rect.left = pygame.Rect(tile[0], tile[1], tile[2], tile[3]).right

    common.is_on_ground = False
    player_rect.y += movement[1]
    tiles = get_colliding_tiles(map_tiles, player_rect)
    for tile in tiles:
        if player_rect.colliderect(tile):
            if movement[1] > 0:
                player_rect.bottom = pygame.Rect(tile[0], tile[1], tile[2], tile[3]).top
                common.is_on_ground = True
                common.y_velocity = 3
            if movement[1] < 0:
                player_rect.top = pygame.Rect(tile[0], tile[1], tile[2], tile[3]).bottom

    return player_rect


def player_movement(key_presses: dict, player_rect: pygame.Rect) -> pygame.Rect:
    """
    Handles all code realting to the movement of the player
    """

    player_movement = [0, common.y_velocity]
    if key_presses["a"]:
        player_movement[0] -= 4
    if key_presses["d"]:
        player_movement[0] += 4

    if common.y_velocity < 10:
        common.y_velocity += 0.5

    player_rect = calculate_rect(player_movement, player_rect, common.map_data["map"])
    return player_rect


def render_map(display: pygame.Surface, tiles: list) -> None:
    """
    Renders the games tiles
    """

    for tile in tiles:
        pygame.draw.rect(display, (60, 255, 100), tile)


def render_player(display: pygame.Surface, player_rect: pygame.Rect) -> None:
    """
    Render the player
    """

    pygame.draw.rect(display, (255, 255, 255), player_rect)


async def main() -> None:
    pygame.init()

    display = pygame.display.set_mode(common.DIMENSIONS)
    clock = pygame.time.Clock()

    key_presses = {"a": False, "d": False}
    player_rect = pygame.Rect(100, 100, 64, 45)

    while True:
        display.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if common.is_on_ground:
                        common.y_velocity -= 16

        key_presses["a"] = pygame.key.get_pressed()[pygame.K_a]
        key_presses["d"] = pygame.key.get_pressed()[pygame.K_d]

        player_rect = player_movement(key_presses, player_rect)

        render_player(display, player_rect)
        render_map(display, common.map_data["map"])

        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)


def run() -> None:
    asyncio.run(main())
