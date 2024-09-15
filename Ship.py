import pygame
import constants as c
from Bullet import Bullet
from hud import HUD

class Ship(pygame.sprite.Sprite):       # inheriting from pygame.sprite.Sprite
    def __init__(self):
        super(Ship,self).__init__()
        self.image = pygame.image.load('ship.png').convert_alpha()  # convert_alpha for smoothness of the game

        self.image = pygame.transform.scale(self.image,(self.image.get_width()//8, self.image.get_height()//8))

        self.rect = self.image.get_rect()                           # get_rect tells about the coordinates and other 
        self.rect.x = c.DISPLAY_WIDTH // 2  - 40                                    # properties about ship
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height*1.5

        self.max_hp = 3
        self.hp = self.max_hp
        self.lives = 3
        self.is_alive = True

        self.hud = HUD(self.hp, self.lives)
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)

        self.is_invincible = False
        self.max_invincible_timer = 60
        self.invincible_timer = self.max_invincible_timer

        self.vel_x = 0                                              
        self.vel_y = 0
        self.speed = 5
        self.bullet_group = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('Shoot1.ogg')

    
    def update(self):
        self.bullet_group.update()                                     # Running update method of Bullet class
        self.hud_group.update()

        for bullet in self.bullet_group:                               # Removing out of screen bullets out of
            if bullet.rect.y < 0:                                      # memory
                self.bullet_group.remove(bullet)

        if self.rect.x > c.DISPLAY_WIDTH-self.rect.width+20:           # Making sure ship cannot move out of 
            self.rect.x = c.DISPLAY_WIDTH-self.rect.width+20           # screen
        if self.rect.x < -20:
            self.rect.x = -20

        self.rect.x += self.vel_x                                      # Updation
        self.rect.y += self.vel_y

        if self.invincible_timer > 0:
            self.invincible_timer -= 1
        else:
            self.is_invincible = False

    def shoot(self):
        if self.is_alive:
            self.snd_shoot.set_volume(.10)
            self.snd_shoot.play()
            self.new_bullet = Bullet()                                     # Bullet being created everytime spacebar
            self.new_bullet.rect.x = self.rect.x + 32                      # is pressed
            self.new_bullet.rect.y = self.rect.y 
            self.new_bullet.vel_y = -self.new_bullet.speed 
            self.bullet_group.add(self.new_bullet)

    def get_hit(self):
        if self.is_alive:
            self.hp -= 1
            self.hud.health_bar.decrease_hp_value()
            if self.hp <= 0:
                self.hp = 0
                self.death()

    def death(self):
        self.lives -= 1
        if self.lives <= 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()
        self.hud.lives.decrement_life()
        self.rect.x = c.DISPLAY_WIDTH // 2  - 40
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer