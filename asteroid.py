from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        split_1 = self.velocity.rotate(new_angle)
        split_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_1.velocity = split_1 * 1.2
        new_2.velocity = split_2 * 1.2