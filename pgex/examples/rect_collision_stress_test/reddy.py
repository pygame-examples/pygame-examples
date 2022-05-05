import random

import pygame


class Reddy(pygame.sprite.Sprite):
    RED_SURF = pygame.Surface((10, 10))
    RED_SURF.fill("red")
    GREEN_SURF = pygame.Surface((10, 10))
    GREEN_SURF.fill("green")

    VECTOR = pygame.Vector2(1, 0)

    def __init__(self):
        super().__init__()
        self.image = self.RED_SURF
        self.rect = self.image.get_rect(center=(250, 200))
        self.angle = random.randint(-180, 180)

    def update(self):
        collided = False
        self.rect.move_ip(self.VECTOR.rotate(self.angle) * 3)
        for gr in self.groups():
            for sprite in gr:
                if self is sprite:
                    continue
                if self.rect.colliderect(sprite.rect):
                    collided = True

        if self.rect.top < 0:
            self.angle = random.randint(0, 180)
        elif self.rect.bottom > 400:
            self.angle = random.randint(-180, 0)
        elif self.rect.left < 0:
            self.angle = random.randint(-90, 90)
        elif self.rect.right > 500:
            self.angle = random.randint(90, 270)

        if collided:
            self.image = self.GREEN_SURF
        elif not collided:
            self.image = self.RED_SURF
