from os import kill
from pygame import Vector2
import math

PROJECTILES = []
PROJECTILE_SPEED = 6

def renum_projectiles():
	for i in range(len(PROJECTILES)):
		PROJECTILES[i].number = i

def kill_projectile(projectile):
    renum_projectiles()
    projectile.kill()
    PROJECTILES.pop(projectile.number)
    renum_projectiles()

def create_projectile(tower, projectile_type, target):

    dx = target.position.x - tower.position.x
    dy = target.position.y - tower.position.y
    angle = math.atan2(dy, dx)
    velocity = Vector2((PROJECTILE_SPEED - target.speed) * math.cos(angle), (PROJECTILE_SPEED - target.speed) * math.sin(angle))
    
    PROJECTILES.append(projectile_type(len(PROJECTILES), tower.position, target, tower, velocity))

def update_projectiles(surface):
    for projectile in PROJECTILES:
        if projectile.is_dead:
            kill_projectile(projectile)
        else:
            projectile.move()
            projectile.hit_target()
            projectile.draw(surface)