import pygame
from pygame import Vector2
from pygame.locals import QUIT

import game_levels as GL
import handle_enemies as HE
import handle_projectiles as HP
import handle_blocks as HB


#Initialize pygame
WIDTH = 860
HEIGHT = 650
pygame.init()
#Create screen and time manager things
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

HB.create_block(Vector2(90, 250))
HB.create_block(Vector2(200, 250))


while GL.RUNNING:

    # Check for all user events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            HB.check_tower_blocks(Vector2(mouse_pos))


    #Fill the screen
    screen.fill((100, 100, 200))

    #Update Game objects
    HE.create_enemies()
    HE.update_enemies(screen)
    HP.update_projectiles(screen)
    HB.update_blocks(screen)

    clock.tick(60)

    # Update the screen
    pygame.display.flip()
    
# END GAME LOOP
pygame.quit()