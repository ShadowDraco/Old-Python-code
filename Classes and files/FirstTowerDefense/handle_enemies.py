import game_levels as GL
import enemy_types as ET



ENEMIES = []
timer = 0
enemies_spawned_this_round = 0
total_enemies_spawned = 0

def kill_enemy(enemy):
    print("Killed enemy", enemy.number)
    GL.PLAYER_MONEY += enemy.worth
    GL.ENEMIES_KILLED += 1
    print(GL.PLAYER_MONEY)

    renum_enemies()
    enemy.kill()
    ENEMIES.pop(enemy.number)
    renum_enemies()


def renum_enemies():
    for i in range(len(ENEMIES)):
        ENEMIES[i].number = i

def deal_damage(enemy, bullet):
    enemy.health -= bullet.damage


def create_enemies():
    global timer, enemies_spawned_this_round, spawn_time, total_enemies_spawned

    if enemies_spawned_this_round <= GL.ENEMY_COUNTS[GL.LEVEL][GL.ROUND]:
        if timer >= GL.SPAWN_TIMES[GL.LEVEL][GL.ROUND]:
            ENEMIES.append(ET.Grog(total_enemies_spawned))
            timer = 0
            enemies_spawned_this_round += 1
            total_enemies_spawned += 1
        else:
            timer+=1
    else:
        if GL.ROUND <= 5:
            GL.next_round()
            enemies_spawned_this_round = 0
        else:
            GL.next_level()

def update_enemies(surface):
    for enemy in ENEMIES:
        if enemy.health < 1:
            kill_enemy(enemy)

        # Create next Spots
        spot =  GL.LEVELS[GL.LEVEL][enemy.spot_num]
        # Check if the index will be out of bounds because there are no more positions to go to
        if enemy.spot_num < len(GL.LEVELS[GL.LEVEL])-1:
            next_spot =  GL.LEVELS[GL.LEVEL][enemy.spot_num+1]
            next_direction =  GL.DIRECTIONS[GL.LEVEL][enemy.spot_num+1]
        else:
            next_spot = "END"
            next_direction = "END"

        #Update the enemy
        enemy.move(spot)
        enemy.arrive_at_spot(spot, next_spot, next_direction)

        # Check if the enemy is at the end
        if enemy.spot == "END":

            kill_enemy(enemy)
    
            GL.PLAYER_HEALTH -= 1
            if GL.PLAYER_HEALTH < 1:
                 GL.RUNNING = False

        enemy.draw(surface)