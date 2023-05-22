"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

The main module
"""

import asyncio
import random
import time
from typing import List

import pygame

from .particle import Particle


def create_particles(particle_list: list):
    """
    Adds a new particle to a list
    """

    particle_list.append(
        Particle(
            pos=pygame.Vector2(pygame.mouse.get_pos()),
            vel=pygame.Vector2(random.uniform(-5, 5), 7),
            radius=10,
            radius_speed=random.uniform(0.4, 0.5),
            gravity=1,
        )
    )


def update_particles(particle_list: List[Particle], dt: float):
    """
    Updates particles from a list
    """

    for particle in particle_list:
        if particle.radius <= 0:
            particle_list.remove(particle)

        particle.update(dt)


def draw_particles(particle_list: List[Particle], screen: pygame.Surface):
    for particle in particle_list:
        particle.draw(screen)


async def main():
    """
    Contains game variables and the game loop
    """
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Particles!")

    particles = []
    last = time.perf_counter()
    while True:
        dt = (time.perf_counter() - last) * 60
        last = time.perf_counter()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.fill("black")

        create_particles(particles)
        update_particles(particles, dt)
        draw_particles(particles, screen)

        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    """
    Function that runs the example
    """
    asyncio.run(main())


if __name__ == "__main__":
    run()
