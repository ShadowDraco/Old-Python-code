from pygame import Vector2
import tower_types as TT

PLAYER_HEALTH = 3
PLAYER_MONEY = 5
ENEMIES_KILLED = 0
RUNNING = True
LEVEL = 0
ROUND = 0
END = "END"

TOWER_PRICES = [5, 25, 50, 100]
TOWER_TYPES = [TT.Bullet_Tower]

# Defines the posisitons and directions 
# As well as
# Enemy counts for specific rounds per level and time between spawns per round
LEVEL_1_Positions = [Vector2(150, 300), Vector2(150, 400), Vector2(50, 400), Vector2(50, 500), Vector2(300, 500),
                     Vector2(300, 200), Vector2(200, 200), Vector2(200, 350), Vector2(500, 350), Vector2(850, 350), "END"]
LEVEL_1_Directions = ["Right", "Down", "Left", "Down", "Right",
                      "Up", "Left", "Down", "Right", "Right", "END"]
LEVEL_1_Enemy_Counts = [1, 5, 10, 20, 30, 30]

# First time is a delay between levels, each time is a delay betwen spawns in a round
# This means "Round 0" is a grace period
LEVEL_1_Spawn_Times = [150, 150, 150, 100, 100, 100]

#Unfinished Level
LEVEL_2_Positions = [Vector2(100, 100), Vector2(200, 100), Vector2(200, 150), Vector2(200, 200), Vector2(500, 200)]
LEVEL_2_Directions = ["Right", "Right", "Down", "Down", "Right"]
LEVEL_2_Enemy_Counts = [10, 20, 40, 50, 60]
LEVEL_2_Spawn_Times = [500, 150, 150, 100, 100, 90]

# Contains all posistions and directions and enemy counts per level and spawn times to be accessed
LEVELS = [LEVEL_1_Positions, LEVEL_2_Positions]
DIRECTIONS = [LEVEL_1_Directions, LEVEL_2_Directions]
ENEMY_COUNTS = [LEVEL_1_Enemy_Counts, LEVEL_2_Enemy_Counts]
SPAWN_TIMES = [LEVEL_1_Spawn_Times, LEVEL_2_Spawn_Times]

def next_round():
    global ROUND
    ROUND += 1
    print("Round", ROUND)
def next_level():
    global ROUND, LEVEL
    ROUND = 0
    LEVEL += 1
    print("Level", LEVEL)