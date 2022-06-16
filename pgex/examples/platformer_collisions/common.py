"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""
import json
import os

from .tile import Tile

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
TILE_COLOR = (60, 255, 100)
FPS = 60

with open(os.path.join(os.path.dirname(__file__), "assets/map.json"), "rb") as file:
    map_data = json.load(file)

tiles = []
for rect in map_data["map"]:
    tiles.append(Tile(rect=rect, color=TILE_COLOR))
