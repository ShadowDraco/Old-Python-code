import pygame
from pygame.math import Vector2
from pygame.image import load

import math
import random

# Initialize pygame
pygame.init()

# Constants / globals
running = True
WIDTH = 500
HEIGHT = 500
DELTA_TIME = 0
	# color
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
PLAYER = (100, 255, 200)
	# enemies
ENEMIES = []
BULLETS = []
    # levels
LEVELS = [[10, 1], [20, 1], [20, 2], [30, 2], [30, 2], [30, 3], [60, 2], [50, 3], [100, 3], [150, 3], [150, 3], [200, 3], [500, 4]]
#LEVEL = 0 - becomes undefined even though it worked for some time --> moved to player.game_level

# Create screen and clock
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
# Set mouse posistion
mouse = pygame.mouse.get_pos()

def renum_enemies():
	for i in range(len(ENEMIES)):
		ENEMIES[i].num = i

def manage_enemies(enemy):
	ENEMIES.pop(enemy.num)
	renum_enemies()
	enemy.kill()
	if len(ENEMIES) < 1:
		new_level()

def renum_bullets():
	for i in range(len(BULLETS)):
		BULLETS[i].num = i

def manage_bullets(bullet):
	BULLETS.pop(bullet.num)
	renum_bullets()
	bullet.kill()

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, vel, sprite_path, xp = 0, game_level = 0):
		super().__init__()
		# Parameters
		self.pos = Vector2(pos)
		self.image = load(sprite_path).convert()
		self.rect = self.image.get_rect()
		self.radius = self.image.get_width() / 2
		self.vel = Vector2(vel)
		# Everything else
		self.speed = 1
		self.health = 2
		self.max_health = 2
		self.xp = xp
		self.max_xp = 10
		self.level = 1

		self.game_level = game_level
			# time between shots
		self.fire_rate = 50
		self.ftime = 0
			# time between getting hit
		self.hit_time = 15
		self.htime = 0
			# if moving
		self.x = False
		self.y = False
		self.friction = 0.1

		self.bullet_damage = 1
		self.bullet_life_time = 20
		self.bullet_piercing = 1
		self.bullet_speed = 5
	
	def level_up(self, xp):
		self.xp += 1 * xp
		if self.xp >= self.max_xp:
			print("level up")
			self.xp -= self.max_xp
			self.max_xp += self.max_xp * 0.5
			self.fire_rate -= 1
			self.hit_time += 1
			self.max_health += 0.1
			self.speed += 0.1
			self.bullet_damage += 0.1
			self.bullet_life_time += 5
			self.bullet_piercing += 0.2
	
	def shoot(self):
		if self.ftime >= self.fire_rate:
			BULLETS.append(Bullet(self.pos[0], self.pos[1], int(len(BULLETS)), self.bullet_damage, self.bullet_life_time, self.bullet_piercing))
			renum_bullets()
			self.ftime = 0
		self.ftime += 1

	def collide_enemy(self):
		self.htime+= 1
		if self.htime > self.hit_time:
			self.htime = 0
			for enemy in ENEMIES:
				if self.rect.colliderect(enemy.rect):
					ENEMIES.pop(enemy.num)
					renum_enemies()
					self.health -= 1
			if self.health < 1:
				pygame.quit()
		

	def take_keys(self):
		keys = pygame.key.get_pressed() 
		# Check if two keys are pressed
		if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_UP] or keys[pygame.K_w]):
			self.vel = [-self.speed, -self.speed]
			self.y = True
			self.x = True
		elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (keys[pygame.K_UP] or keys[pygame.K_w]):
			self.vel = [self.speed, -self.speed]
			self.y = True
			self.x = True
		elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
			self.vel = [-self.speed, self.speed]
			self.y = True
			self.x = True
		elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
			self.vel = [self.speed, self.speed]
			self.y = True
			self.x = True
		else:
			# Check if only one key is pressed (and held)
			if keys[pygame.K_LEFT] or keys[pygame.K_a]:
				self.vel = [-self.speed, 0]
				self.x = True
			elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
				self.vel = [+self.speed, 0]
				self.x = True
			else:
				self.x = False
			if keys[pygame.K_UP] or keys[pygame.K_w]:
				self.vel = [0, -self.speed]
				self.y = True
			elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
				self.vel = [0, self.speed]
				self.y = True
			else:
				self.y = False

	def move(self):
		# move if a movement key is pressed
		if self.y or self.x:
			self.pos += self.vel
		
		#move while deccelerate if a movement key is not pressed
		if not self.x:
			if self.vel[0] > self.friction:
				self.vel[0] -= self.friction
			elif self.vel[0] < -self.friction:
				self.vel[0] += self.friction
			self.pos += self.vel
		if not self.y:
			if self.vel[1] > self.friction:
				self.vel[1] -= self.friction
			elif self.vel[1] < -self.friction:
				self.vel[1] += self.friction
			self.pos += self.vel
		
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

	def draw(self, surface):
		blit_pos = self.pos - Vector2(self.radius)
		surface.blit(self.image, blit_pos)




		

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, num, damage, life_time, piercing, speed = 5):
		super().__init__()
		# Parameters
		self.num = num
		# Player influence
		self.pos = Vector2((x, y))
		self.damage = damage
		self.life_time = life_time
		self.piercing = piercing
		self.alive_time = 0
		# Default
		self.speed = speed
		# Image
		self.image = pygame.image.load("FirstTopDownShooter/WhiteCube.png").convert()
		self.image = pygame.transform.scale(self.image, (5, 5))
		self.radius = self.image.get_width() / 2
		self.rect = self.image.get_rect()
		#Target position
		self.target = Vector2(mouse)
		self.dx = self.target[0] - self.pos[0]
		self.dy = self.target[1] - self.pos[1]
		self.angle = math.atan2(self.dy, self.dx)
		self.vel = Vector2(self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))


	def move(self):
		if (self.alive_time >= self.life_time) or (self.piercing < 1):
			manage_bullets(self)
		else:
			self.pos += self.vel
			self.rect.x = self.pos.x
			self.rect.y = self.pos.y

			for enemy in ENEMIES:
				if self.rect.colliderect(enemy):
					enemy.take_damage(self)
					self.piercing -= 1
		self.alive_time += 1
		
	def draw(self, surface):
		blit_pos = self.pos - Vector2(self.radius)
		surface.blit(self.image, blit_pos)








		
class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos, level, num):
		super().__init__()
		self.pos = Vector2(pos)
		self.level = level
		self.num = num

		if self.level == 1:
			self.speed = 0.25
			self.health = 1
			self.sprite_path = "FirstTopDownShooter/level1.png"

		elif self.level == 2:
			self.speed = 0.4
			self.health = 2
			self.sprite_path = "FirstTopDownShooter/level2.png"

		elif self.level == 3:
			self.speed = 0.3
			self.health = 5
			self.sprite_path = "FirstTopDownShooter/level3.png"

		elif self.level == 4:
			self.speed = 1
			self.health = 11
			self.sprite_path = "FirstTopDownShooter/level4.png"
		
		self.image = load(self.sprite_path).convert()
		self.rect = self.image.get_rect()
		self.radius = self.image.get_width() / 2
	
	def move(self, ppos):
		if self.pos[0] > ppos[0]:
			self.pos[0] -= self.speed
		if self.pos[0] < ppos[0]:
			self.pos[0] += self.speed
		if self.pos[1] > ppos[1]:
			self.pos[1] -= self.speed
		if self.pos[1] < ppos[1]:
			self.pos[1] += self.speed
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]
		
	def take_damage(self, bullet):
		self.health -= bullet.damage
		if self.health < 1:
			player.level_up(self.level)
			manage_enemies(self)
	
	def draw(self, surface):
		blit_pos = self.pos - Vector2(self.radius)
		surface.blit(self.image, blit_pos)

def create_enemies(ppos, amount, level):
	# Previous time for delaying enemy spawning
	ptime = 0
	enemies_spawned = 0
	# spawn "amount" enemies
	while enemies_spawned < amount:
		if ptime >= 60:
			# set a random posistion (with some room for extra space) but then check if its within 100 units of the player
			cx = random.randrange(0, WIDTH*1.75)
			cy = random.randrange(0, HEIGHT*1.75)
			el = random.randint(1, level)

			if math.sqrt( (cx - ppos[0])**2 + (cy - ppos[1])**2 ) > WIDTH/5:
				ENEMIES.append(Enemy([cx, cy], el, enemies_spawned))
			ptime = 0
			enemies_spawned += 1
		ptime += 1

def new_level():
	create_enemies(player.pos, LEVELS[player.game_level][0], LEVELS[player.game_level][1])
	player.health = player.max_health
	player.game_level+=1
				
player = Player([200, 200], [0, 0], "FirstTopDownShooter/player.png")
new_level()

while running:

	# Get events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("quit")
			running = False
			pygame.quit
		if event.type == pygame.MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
		

	#Draw on the screen
	screen.fill((120, 0, 255))

	# Update player
	player.take_keys()
	player.move()
	player.shoot()
	player.draw(screen)
	player.collide_enemy()

	# Update everything else
	for enemy in ENEMIES:
		enemy.move(player.pos)
		enemy.draw(screen)

	for bullet in BULLETS:
		bullet.move()
		bullet.draw(screen)

	pygame.display.flip()

	clock.tick(100)

pygame.quit()

