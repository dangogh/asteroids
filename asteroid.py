import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2) 

    def update(self, dt):
        # self.position = pygame.Vector2(x, y)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        newangle = random.uniform(20, 50)
        newradius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, newradius)
        a1.velocity = self.velocity.rotate(newangle) * 1.2
        a2 = Asteroid(self.position.x, self.position.y, newradius)
        a2.velocity = self.velocity.rotate(-newangle) * 1.2