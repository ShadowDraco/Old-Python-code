import pygame
from pygame.math import Vector2

import load_image

class Enemy(pygame.sprite.Sprite):

    def __init__(self, speed, health, worth, name, image):
        super().__init__()
        self.position = Vector2(0, 300)
        self.speed = speed
        self.velocity = Vector2(0)
        self.health = health
        self.worth = worth
        self.name = name
        self.image = load_image.load_sprite(image)
        self.rect = self.image.get_rect()
        self.radius = self.image.get_width()/2

        self.spot = Vector2()
        self.spot_num = 0
        self.direction = "Right"

    def arrive_at_spot(self, spot, next_spot, next_direction):
            if self.direction == "Right":
                if self.position.x >= spot.x:
                    self.spot = next_spot
                    self.direction = next_direction
                    self.spot_num += 1
                    

            if self.direction == "Left":
                if self.position.x <= spot.x:
                    self.spot = next_spot
                    self.direction = next_direction
                    self.spot_num += 1
                    

            if self.direction == "Up":
                if self.position.y <= spot.y:
                    self.spot = next_spot
                    self.direction = next_direction
                    self.spot_num += 1
                    

            if self.direction == "Down":
                if self.position.y >= spot.y:
                    self.spot = next_spot
                    self.direction = next_direction
                    self.spot_num += 1
                    
            
    def set_velocity(self, spot):
        # Enemy can move in one direction towards the next spot
        if self.direction == "Right":
            if self.position.x < spot.x:
                self.velocity = [self.speed, 0]
        if self.direction == "Left":
            if self.position.x > spot.x:
                self.velocity = [-self.speed, 0]
        if self.direction == "Up":
            if self.position.y > spot.y:
                self.velocity = [0, -self.speed]
        if self.direction == "Down":
            if self.position.y < spot.y:
                self.velocity = [0, self.speed]

    def move(self, spot):
        self.set_velocity(spot)
        self.position+=self.velocity

    
    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.image, blit_position)
