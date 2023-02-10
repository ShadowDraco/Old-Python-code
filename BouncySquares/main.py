import pygame
from pygame.locals import QUIT

import cube
import constants as C

pygame.init()


screen = pygame.display.set_mode([C.WIDTH, C.HEIGHT])
clock = pygame.time.Clock()

running = True

cube.create_cubes(10)

while running:

    # Check for all user events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    #Fill the screen
    screen.fill(C.COLORS["Gray"])

    # Update game objects
    for cube in C.CUBES:
        cube.update(screen)

    clock.tick(60)


    # Update the screen
    pygame.display.flip()
# END GAME LOOP
pygame.quit()