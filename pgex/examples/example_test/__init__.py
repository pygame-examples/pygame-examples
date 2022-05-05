import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			raise SystemExit
			
	screen.fill("black")
	

