import pygame
from circleshape import *
from shot import *
from constants import *
from containers import updatable, drawable

class Player(CircleShape):
    containers = (updatable, drawable)
    
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.bullet_timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white_color = pygame.Color((255,255,255))
        pygame.draw.polygon(surface=screen,color=white_color,points=self.triangle(),width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(dt * -1)
            
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        
        if self.bullet_timer > 0:
            self.bullet_timer -= dt
            
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self, dt):
        if self.bullet_timer <= 0:
            shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
            self.bullet_timer = PLAYER_SHOOT_COOLDOWN



