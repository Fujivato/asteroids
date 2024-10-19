import pygame
from circleshape import *
from containers import asteroids, updatable, drawable

class Asteroid(CircleShape):
    containers = (asteroids, updatable, drawable)
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        white_color = pygame.Color((255,255,255))
        pygame.draw.circle(surface=screen,color=white_color,center=self.position,radius=self.radius,width=2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)