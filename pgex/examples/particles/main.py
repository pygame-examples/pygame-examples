import pygame
import time
import particle as p
from typing import List
import random
import asyncio


def create_particles(
		particle_list: list
	):
	"""Function that creates a new particle"""

	particle_list.append(
		p.Particle(
			pygame.mouse.get_pos(), 			   		# pos
			10,		  			   					    # radius
			random.uniform(0.4, 0.5),	 				# radius speed
			pygame.Vector2(random.uniform(-5,5), 7),    # vel
			1 					   						# gravity
		)
	)


def update_particles(
		particle_list: List[p.Particle],
		screen		 : pygame.Surface,
		dt			 : float
	):
	
	"""Function that updates particles"""

	for particle in particle_list:
		if particle.radius <= 0:
			particle_list.remove(particle)

		particle.update(screen, dt)


async def main():
	screen = pygame.display.set_mode((600,500))
	pygame.display.set_caption('Particles!')

	particles = []
	last = time.perf_counter()
	while True:
		dt = (time.perf_counter() - last) * 60
		last = time.perf_counter()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				raise SystemExit

		screen.fill('black')

		create_particles(particles)
		update_particles(particles, screen, dt)


		pygame.display.flip()
		await asyncio.sleep(0)


def run():
	asyncio.run(main())


if __name__ == "__main__":
    run()
