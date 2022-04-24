import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self._run()

    def _run(self):
        self.screen.fill('black')

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        pygame.display.flip()

