
import pygame
from pygame.math import Vector2
from handle_enemies import deal_damage

import load_image

class Projectile(pygame.sprite.Sprite):

    def __init__(self, position, target, tower, velocity, damage, name, image):
        super().__init__()
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.target = target
        self.target.rect = self.target.rect
        self.damage = damage
        self.name = name
        self.image = load_image.load_sprite(image)
        self.rect = self.image.get_rect()
        self.radius = self.image.get_width()/2
        self.is_dead = False
        self.distance_traveled = 0
        self.tower = tower

    def hit_target(self):
        if self.distance_traveled > self.radius:
            if self.rect.colliderect(self.target.rect):
                deal_damage(self.target, self)
                self.is_dead = True
                self.tower.lose_target()
        self.distance_traveled += 1


    def move(self):
        self.position+=self.velocity
    
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.image, blit_position)
