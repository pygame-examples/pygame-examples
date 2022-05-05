import pygame


class Projectile(pygame.sprite.Sprite):
    image = pygame.Surface((20, 10), flags=pygame.SRCALPHA)
    pygame.draw.polygon(image, "red", ((0, 0), (15, 0), (20, 5), (15, 10), (0, 10)))
    velocity = 5
    max_distance = 200

    def __init__(self, start_pos, target_pos, to_max=True):
        super().__init__()
        self.start_pos = sp = x0, y0 = pygame.Vector2(start_pos)
        tp = x1, y1 = pygame.Vector2(target_pos)

        self.rect = self.image.get_rect(center=start_pos)
        self.vector = pygame.Vector2(x1 - x0, y1 - y0).normalize()
        angle = self.vector.angle_to(pygame.Vector2(1, 0))
        self.image = pygame.transform.rotate(self.image, angle)
        if not to_max:
            self.max_distance = min(self.max_distance, round(sp.distance_to(tp)))
        self.travelled_distance = 0

    def update(self):
        if self.travelled_distance > self.max_distance:
            self.kill()
        self.travelled_distance += self.velocity
        self.rect.center = self.start_pos + self.vector * self.travelled_distance
