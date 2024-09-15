import pygame
import constants as c
import random

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star,self).__init__()
        self.star_width = random.randrange(1,4)                     # Square stars with random size
        self.star_height = self.star_width
        self.star_size = (self.star_width, self.star_height)

        self.image = pygame.Surface(self.star_size)                 # Making Surface
        self.color = (255,255,255)                                  # White Stars
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,c.DISPLAY_WIDTH)           # Random Spawning of stars in x direction
        self.rect.y = 0
        self.vel_x = 0
        self.vel_y = random.randrange(5,15)                         # Random falling speed of stars in y direction

    def update(self):
        self.rect.x += self.vel_x                                   # Updation
        self.rect.y += self.vel_y
