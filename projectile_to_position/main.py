import pygame


pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    image = pygame.Surface((10, 10))
    image.fill('red')
    velocity = 5
    max_distance = 200

    def __init__(self, start_pos, target_pos, to_max=True):
        super().__init__()
        self.start_pos = sp = x0, y0 = pygame.Vector2(start_pos)
        tp = x1, y1 = pygame.Vector2(target_pos)

        self.rect = self.image.get_rect(center=start_pos)
        self.vector = pygame.Vector2(x1 - x0, y1 - y0).normalize()
        if not to_max:
            self.max_distance = min(self.max_distance, round(sp.distance_to(tp)))
        self.travelled_distance = 0

    def update(self):
        if self.travelled_distance > self.max_distance:
            self.kill()
        self.travelled_distance += self.velocity
        self.rect.center = self.start_pos + self.vector*self.travelled_distance


bullet_group = pygame.sprite.Group()

running = True
while running:
    clock.tick(60)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = Bullet((250, 200), event.pos)
                bullet_group.add(bullet)

    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.flip()
