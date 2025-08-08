import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Logic to split the asteroid into smaller ones
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50) # Randomize the split angle
            for angle in [-random_angle, random_angle]:
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid.velocity = self.velocity.rotate(angle) * 1.2 # Slightly increase speed