import pygame
from pygame.math import Vector2
from pygame.image import load

import random
import collision
import constants as C



class Cube(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image, number):
        super().__init__()
        # Parameters
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.number = number
        self.image = load(image).convert()
        # Others
        self.rect = self.image.get_rect()
        self.radius = self.image.get_width() / 2
        self.size = 10
        self.speed = 2
    
    def bounce(self, x, y):
        if x:
            self.vel.x = -self.vel.x
        if y: 
            self.vel.y = -self.vel.y

    def move(self):
        self.pos += self.vel
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
    def draw(self, surface):
        blit_pos = self.pos - Vector2(self.radius)
        surface.blit(self.image, blit_pos)

    def update(self, surface):
        self.move()
        collision.collide_cubes(self)
        collision.collide_walls(self)
        self.draw(surface)

def create_cubes(amount):

    for i in range(amount):
        pos = [random.randrange(0, C.XBOUND), random.randrange(0, C.YBOUND)]
        vel = [random.randrange(-2,2), random.randrange(-2, 2)]
        # Cubesprite dict key
        k = random.sample(C.CUBESPRITES.keys(), 1)
        image = 'BouncySquares/' + C.CUBESPRITES[k[0]] + '.png'

        C.CUBES.append(Cube(pos, vel, image, i))
