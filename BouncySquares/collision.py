import constants as C

def collide_walls(cube):
    # Collide with walls
    if (cube.pos.x >= C.WIDTH - cube.size) or (cube.pos.x <= 0 + cube.size):
        cube.bounce(True, False)
            
    if (cube.pos.y >= C.HEIGHT - cube.size) or (cube.pos.y <= 0 + cube.size):
        cube.bounce(False, True)
    
def collide_cubes(current):
    for cube in C.CUBES:
        if current.rect.colliderect(cube.rect):
            if current != cube:
                current.bounce(True, True)