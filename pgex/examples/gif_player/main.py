import pygame
from .gif_player import GIFPlayer


WIDTH, HEIGHT = 500, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background_gif = GIFPlayer("./gif_player/image.gif", size=(WIDTH, HEIGHT), exclude=(0,))

running = True
while running:
    clock.tick(60)
    screen.fill("black")

    background_gif.play(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
