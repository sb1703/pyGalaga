import pygame
import random
import constants as c
from Enemy import Enemy

class Enemy_spwaner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(40,60)
    
    def update(self):
        self.enemy_group.update()

        for enemy in self.enemy_group:                        # Removing out of screen enemy out of
            if enemy.rect.y > c.DISPLAY_HEIGHT:               # memory
                self.enemy_group.remove(enemy)

        if self.spawn_timer == 0:
            self.new_enemy = Enemy()
            self.enemy_group.add(self.new_enemy)
            self.spawn_timer = random.randrange(40,60)
        self.spawn_timer -= 1

    def clear_enemies(self):
        self.enemy_group.empty()
