import pygame
from pygame.math import Vector2

import handle_projectiles as HP
import handle_enemies as HE
import load_image

class Tower(pygame.sprite.Sprite):

    def __init__(self, position, fire_rate, range, name, projectile_type, image):
        super().__init__()
        self.position = Vector2(position)
        self.range = range
        self.fire_rate = fire_rate
        self.fire_time = 0
        self.name = name
        self.projectile_type = projectile_type
        self.image = load_image.load_sprite(image)
        self.rect = self.image.get_rect()
        self.radius = self.image.get_width()/2

        self.targets = []
        self.current_target = None
        self.current_target_number = None

    # Add an enemy to targets
    def target_enemy(self, enemies):
            for enemy in enemies:
                if enemy not in self.targets:
                    if self.position.distance_to(enemy.position) <= self.range:
                        self.targets.append(enemy)
                    # If there is no current target make the target whatever comes up first
                    if self.current_target is None:
                        self.current_target = enemy
                        

    # Check if enemies are stil in range witout looping through every enemy again
    def check_targets_in_range(self, targets):
        lost_target = False
        for target in targets:
            if self.position.distance_to(target.position) > self.range:
               lost_target = True
               break
        if lost_target:
            self.lose_target()

    # Drop a target out of range
    def lose_target(self):
        if self.targets:
            self.targets.pop(0)
        if self.targets:
            self.current_target = self.targets[0]
        else:
            self.current_target = None
       
         

    # Fire a shot 
    def fire_projectile(self, target):
        if target is not None:
            if self.fire_time >= self.fire_rate:
                HP.create_projectile(self, self.projectile_type, self.current_target)
                self.fire_time = 0
            else:
                self.fire_time += 1

    def rotate(self, target):
        pass

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.image, blit_position)
    
    def update(self):
        self.target_enemy(HE.ENEMIES)
        if self.current_target is not None:
            self.check_targets_in_range(self.targets)
            self.rotate(self.current_target)
            self.fire_projectile(self.current_target)
