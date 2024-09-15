import pygame
import random
import constants as c
from Particle import Particle 

class Particle_spawner:
    def __init__(self):
        self.particle_group = pygame.sprite.Group()

    def update(self):
        self.particle_group.update()
        

    def spawn_particles(self,pos):
        for num_particle in range(random.randrange(3,20)):
                self.new_particle = Particle()
                self.new_particle.rect.x = pos[0]
                self.new_particle.rect.y = pos[1]
                self.particle_group.add(self.new_particle)