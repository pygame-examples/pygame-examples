import pygame
import random
from typing import Set
from pgex.common import PGEX_DIR
from .utils import Time


class Particle:
    GLOW_IMG = pygame.image.load(PGEX_DIR / "shared_examples/example_selector/light.png").convert_alpha()

    def __init__(self, pos: pygame.Vector2, movement: pygame.Vector2) -> None:
        self.movement = movement
        self.pos = pos
        self.size = random.randrange(5, 20)

        self.fg_surf = pygame.transform.scale(self.GLOW_IMG, (self.size * 2.5, self.size * 2.5))
        self.fg_rect = pygame.Rect(self.pos, (self.size, self.size))

    def update(self, dt: float):
        self.pos -= (self.movement * dt)
        self.size -= 0.15 * dt

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (20, 20, 20), self.pos, self.size)
        self.fg_surf = pygame.transform.scale(self.GLOW_IMG, (self.size * 2.5, self.size * 2.5))
        self.fg_rect = self.fg_surf.get_rect(center=self.pos)
        screen.blit(self.fg_surf, self.fg_rect, special_flags=pygame.BLEND_RGB_ADD)


class ParticleManager:
    def __init__(self):
        self.gen_time = Time(0.025)
        self.particles: Set[Particle] = set()

    def update(self, dt: float):
        if self.gen_time.update():
            self.particles.add(Particle(
                pos=pygame.Vector2(random.randrange(0, 500), 500),
                movement=pygame.Vector2(random.uniform(-2.5, 2.5), 3.5)
            ))

        for particle in set(self.particles):
            particle.update(dt)

            if particle.size <= 0:
                self.particles.remove(particle)

    def draw(self, screen: pygame.Surface):
        for particle in self.particles:
            particle.draw(screen)

