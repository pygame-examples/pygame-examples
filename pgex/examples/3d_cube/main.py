"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

The main script
"""

import asyncio
from typing import List

import pygame
from pygame.color import Color
from pygame.math import Vector2, Vector3

from .renderer import Renderer


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.renderer = Renderer(self.screen, 90)

        self.cube_position = Vector3(0, 0, 4)
        self.cube_rotation = Vector3(0, 0, 0)
        self.cube_scale = Vector3(1, 1, 1)

    def run(self):
        # For WASM compatibility.
        asyncio.run(self._run())

    async def _run(self):
        while self.running:
            self.loop()
            await asyncio.sleep(0)

    def loop(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        self.cube_rotation += (0.6, 1.3, 2)

        self.screen.fill("black")
        self.render_cube()

        pygame.display.flip()
        self.clock.tick(60)

        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")

    def render_cube(self):
        polys = [
            [Vector3(vertex) for vertex in poly]
            for poly in [
                [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)],  # Bottom
                [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)],  # Left
                [(1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1)],  # Right
                [(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1)],  # Top
                [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1)],  # Back
                [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)],  # Front
            ]
        ]

        for poly in polys:
            # By-vertex transformations given by rotation, scale, and position.
            for vertex in poly:
                vertex.rotate_x_ip(self.cube_rotation.x)
                vertex.rotate_y_ip(self.cube_rotation.y)
                vertex.rotate_z_ip(self.cube_rotation.z)

                # We can't do `vertex *= self.cube_scale`, as it would do a dot product.
                vertex.x *= self.cube_scale.x
                vertex.y *= self.cube_scale.y
                vertex.z *= self.cube_scale.z

                vertex += self.cube_position

            # Draw the wireframe. (Separate loop as it is post-all-vertices-transformation)
            for i, vertex in enumerate(poly):
                begin = vertex
                end = poly[(i + 1) % len(poly)]  # Loop back.
                self.renderer.draw_line(
                    begin,
                    end,
                    [
                        int(i) % 256 for i in self.cube_rotation
                    ],  # Having fun with the colors
                )
