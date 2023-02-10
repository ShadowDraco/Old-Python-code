import pygame
from pygame.math import Vector2

import load_image

class Block(pygame.sprite.Sprite):

    def __init__(self, position, name, image):
        super().__init__()
        self.position = Vector2(position)
        self.name = name
        self.image = load_image.load_sprite(image)
        self.rect = self.image.get_rect()
        self.radius = self.image.get_width()/2

        self.tower = None

    def get_clicked(self, player_money, price):
        if player_money >= price:
            self.place_tower()

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.image, blit_position)
    
    def update(self, surface):
        self.draw(surface)
        if self.tower != None:
            self.tower.update()
            self.tower.draw(surface)
