import pygame
import random

from circleshape import *
from containers import asteroids, updatable, drawable
from constants import *

class Asteroid(CircleShape):
    containers = (asteroids, updatable, drawable)
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        white_color = pygame.Color((255,255,255))
        pygame.draw.circle(surface=screen,color=white_color,center=self.position,radius=self.radius,width=2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        # remove the current asteroid
        self.kill()
        
        # this was a small asteroid so no need to spawn more
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        # generate new asteroids
        spawn_angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(spawn_angle)
        new_vector2 = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_1.velocity = new_vector1 * 1.2
        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_2.velocity = new_vector2 * 1.2
