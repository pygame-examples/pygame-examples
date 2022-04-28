import pygame

from .characters import DefaultCharacter


class Player(pygame.sprite.Sprite):
    _instance = None
    boundary = pygame.Rect(0, 0, 500, 400)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, character=DefaultCharacter):
        super().__init__()
        self.alive = True
        self.character = character

        self.name = self.character.name
        self.velocity = self.character.velocity
        self.image = self.character.image
        self.rect = self.image.get_rect(center=(250, 200))

    def update(self):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            dy -= self.velocity
        if keys[pygame.K_s]:
            dy += self.velocity
        if keys[pygame.K_d]:
            dx += self.velocity
        if keys[pygame.K_a]:
            dx -= self.velocity

        self.rect.move_ip(dx, dy)
        if not self.rect.colliderect(self.boundary):
            self.kill()

    def set_character(self, character) -> None:
        self.__init__(character)

    def reset(self) -> None:
        self.__init__(self.character)

    def kill(self):
        self.alive = False


player = Player()
