import pygame
from constants import *
from circleshape import CircleShape
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown = 0
    
    def rotate(self, dt): 
        self.rotation += (PLAYER_TURN_SPEED * dt)
        print(f"rotation: {self.rotation}")
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_s] and not keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.cooldown <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.cooldown = PLAYER_SHOOT_COOLDOWN
   
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255,255), self.triangle(), width=2)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    