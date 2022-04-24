import pygame
import random


pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

(RED_SURF := pygame.Surface((10, 10))).fill('red')
(GREEN_SURF := pygame.Surface((10, 10))).fill('green')


class Reddy(pygame.sprite.Sprite):

    vector = pygame.Vector2(1, 0)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = RED_SURF
        self.rect = self.image.get_rect(center=(250, 200))
        self.angle = random.randint(-180, 180)

    def update(self):
        collided = False
        self.rect.move_ip(self.vector.rotate(self.angle) * 3)
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
            self.image = GREEN_SURF
        elif not collided:
            self.image = RED_SURF


group = pygame.sprite.Group()

entity_count = 200
for _ in range(entity_count):
    Reddy(group)

font = pygame.font.Font(None, 16)
check_text = font.render(f'{entity_count ** 2:,}', True, 'white')

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    group.update()
    group.draw(screen)

    fps_text = font.render(f'FPS: {clock.get_fps():.0f}', True, 'white')
    fps_rect = fps_text.get_rect()
    screen.blits(((fps_text, fps_rect), (check_text, check_text.get_rect(top=fps_rect.bottom))))

    pygame.display.flip()

pygame.quit()
