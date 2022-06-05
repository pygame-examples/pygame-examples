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
    Function that creates a new particle
    """

    particle_list.append(
        Particle(
            pygame.mouse.get_pos(),  # pos
            10,  # radius
            random.uniform(0.4, 0.5),  # radius speed
            pygame.Vector2(random.uniform(-5, 5), 7),  # vel
            1,  # gravity
        )
    )


def update_particles(
    particle_list: List[Particle], screen: pygame.Surface, dt: float
):
    """
    Function that updates particles
    """

    for particle in particle_list:
        if particle.radius <= 0:
            particle_list.remove(particle)

        particle.update(screen, dt)


async def main():
    """
    Function that contains game variables and the game loop
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
        update_particles(particles, screen, dt)

        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    """
    Function that runs the example
    """
    asyncio.run(main())


if __name__ == "__main__":
    run()
