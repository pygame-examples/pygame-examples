import math
from os import path

import pygame


class Image:
    """
    This class contains and handles all the processes related to rotating an image around any given axis.
    """
    FILE_NAME = "image.png"
    IMAGE_RECT_POS = (0, 0)  # Position of the topleft of the original image

    def __init__(self, screenw, screenh, font):
        self.screenw, self.screenh = screenw, screenh

        self.font = font

        self.load_image()

        self.center_pos = pygame.Vector2(self.screenw / 2, self.screenh / 2)
        self.pivot_pos = pygame.Vector2(self.image_rect.w / 2, self.image_rect.h / 2)

        self.angle = 0
        self.is_dragged = False

    def load_image(self):
        """
        Loads the main image and creates a rectangle from it.
        """
        self.image = pygame.image.load(
            path.join(path.abspath("."), "Assets", self.FILE_NAME)
        )
        self.image_rect = self.image.get_rect(topleft=self.IMAGE_RECT_POS)

    def events(self, event):
        """
        This function checks for mouse events and if the mouse is pressed inside the source rectangle position of the pivot is changed according to it.
        """
        mpos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.image_rect.collidepoint(mpos):
            self.pivot_pos = pygame.Vector2(mpos)

    def physics(self):
        self.calc_angle()
        self.transform()

        vec = pygame.Vector2(
            self.pivot_pos.x - self.image_rect.centerx,
            self.pivot_pos.y - self.image_rect.centery,
        )
        vec.rotate_ip(self.angle)
        self.transformed_rect.center = self.center_pos - vec

        self.create_text()

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        pygame.draw.circle(screen, "Grey", self.pivot_pos, 5)
        pygame.draw.rect(screen, "Red", self.image_rect, 1)
        screen.blit(self.transformed_image, self.transformed_rect)
        pygame.draw.circle(screen, "Brown", self.center_pos, 5)
        pygame.draw.rect(screen, "Red", self.transformed_rect, 1)

        self.draw_text(screen)

    def calc_angle(self):
        mpos = pygame.Vector2(pygame.mouse.get_pos()) 
        self.vec = mpos - self.center_pos # The vector joining the axis of rotation and the current position of the mouse
        if self.vec.x == 0:
            if self.vec.y < 0:
                self.angle = 270
            else:
                self.angle = 90
        else:
            # The angle made between the vector and the x-axis
            self.angle = math.degrees(math.atan(self.vec.y / self.vec.x))
        if self.vec.x < 0:
            self.angle += 180
        elif self.vec.y < 0:
            self.angle += 360

    def transform(self):
        self.transformed_image = pygame.transform.rotate(self.image, -self.angle)
        self.transformed_rect = self.transformed_image.get_rect()

    def create_text(self):
        self.text_pivot_pos = self.font.render(
            f"Origin: {self.pivot_pos.x}, {self.pivot_pos.y}", True, "Magenta"
        )
        self.text_pivot_pos_rect = self.text_pivot_pos.get_rect(
            topright=(self.screenw, 0)
        )

        self.text_angle = self.font.render(f"Angle: {int(self.angle)}", True, "Magenta")
        self.text_angle_rect = self.text_angle.get_rect(
            topright=(self.screenw, self.text_pivot_pos_rect.bottom)
        )

    def draw_text(self, screen):
        screen.blit(self.text_pivot_pos, self.text_pivot_pos_rect)
        screen.blit(self.text_angle, self.text_angle_rect)
