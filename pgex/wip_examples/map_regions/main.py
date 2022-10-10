import pygame
 
 
pygame.init()
 
WIDTH, HEIGHT = 640, 360
FPS = 60
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
 
map_image = pygame.transform.scale(
    pygame.image.load("us_map.png").convert(), (WIDTH, HEIGHT)
)
 
 
def find_shape(pos, array):
    directions = ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))
    value = array[pos[1]][pos[0]]
    positions = {pos}
    border = {pos}
 
    while True:
        temp_borders = set()
        for pos in border:
            for dx, dy in directions:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos in positions:
                    continue
                try:
                    new_value = array[new_pos[1]][new_pos[0]]
                except IndexError:
                    continue
                if new_value == value:
                    temp_borders.add(new_pos)
        if not border:
            x_positions, y_positions = [], []
            for x, y in positions:
                x_positions.append(x)
                y_positions.append(y)
            origin_x, origin_y = min(x_positions), min(y_positions)
            width = max(x_positions) - origin_x
            height = max(y_positions) - origin_y
            new_array = [
                [
                    1 if (x + origin_x, y + origin_y) in positions else 0
                    for x in range(width)
                ]
                for y in range(height)
            ]
            return new_array, (origin_x, origin_y)
 
        border = temp_borders
        positions |= temp_borders
 
 
class Region:
    def __init__(self, pos, array, color):
        self.pos = pos
        self.original_image = pygame.Surface(
            (len(array[0]), len(array)), pygame.SRCALPHA
        )
        for y, row in enumerate(array):
            for x, value in enumerate(row):
                if value == 1:
                    self.original_image.set_at((x, y), color)
 
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)
 
    def update(self):
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.rect.collidepoint(ev.pos) and self.mask.overlap(
                    pygame.mask.Mask((1, 1), fill=True),
                    (ev.pos[0] - self.pos[0], ev.pos[1] - self.pos[1]),
                ):
                    print(f"Clicked on {id(self)}")
 
    def draw(self, surf):
        surf.blit(self.image, self.rect)
 
 
def get_regions():
    regions = []
    array = pygame.surfarray.array2d(map_image).transpose()
    for y, row in enumerate(array):
        for x, value in enumerate(row):
            if value != 0:
                shape, (origin_x, origin_y) = find_shape((x, y), array)
                if not shape:
                    continue
                array[
                    origin_y : origin_y + len(shape),  # NOQA
                    origin_x : origin_x + len(shape[0]),  # NOQA
                ] = [
                    [
                        0 if shape[y][x] else array[origin_y + y][origin_x + x]
                        for x in range(len(shape[0]))
                    ]
                    for y in range(len(shape))
                ]
                color = pygame.Color("black")
                color.hsva = (y % 360, 70, 100, 100)
                region = Region(
                    (origin_x, origin_y), shape, (color.r, color.g, color.b, 255),
                )
                regions.append(region)
    return regions
 
 
all_regions = get_regions()
 
running = True
while running:
    clock.tick(FPS)
    screen.fill("black")
 
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
 
    for r in all_regions:
        r.update()
        r.draw(screen)
 
    pygame.display.flip()
  
