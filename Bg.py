import pygame
import constants as c
import random
from Star import Star

class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super(Bg,self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE)          # Making Surface
        self.color = (0,0,15)                                # Black-Bluish Background
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.group_star = pygame.sprite.Group()              # Group of stars in bg
        self.time = random.randrange(1,7)                    # Initialization of time

    def update(self):
        self.group_star.update()                             # Running update method of Star class

        for stars in self.group_star:                        # Removing out of screen stars out of
            if stars.rect.y > c.DISPLAY_HEIGHT:              # memory
                self.group_star.remove(stars)
        
        if self.time == 0:
            new_star = Star()
            self.group_star.add(new_star)                    # Addition of more stars in group when time = 0
            self.time = random.randrange(1,7)                # Resetting of time
        self.image.fill(self.color)                          # No overlapping problem takes place in stars and enemy
        self.group_star.draw(self.image)                     # Drawing of stars
        self.time-=1
