"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""
import json
import os

with open(os.path.join(os.path.dirname(__file__), "maps/map.json"), "rb") as file:
    map_data = json.load(file)

y_velocity = 3

is_on_ground = False

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
