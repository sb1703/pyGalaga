import pygame
import constants as c

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        bullet_width = 3
        bullet_height = 16
        bullet_size = (bullet_width, bullet_height)           # Bullet Size

        self.image = pygame.Surface(bullet_size)              # Making Surface
        self.color = (255,255,255)                            # White Bullets
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 20

    def update(self):
        self.rect.x += self.vel_x                             # Updation
        self.rect.y += self.vel_y
