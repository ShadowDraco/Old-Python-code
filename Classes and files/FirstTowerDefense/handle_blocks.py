import block_types as BT
import game_levels as GL

BLOCKS = []

def create_block(position):
    BLOCKS.append(BT.Tower_Block(len(BLOCKS), position))

def create_tower(block, tower_type):
    if tower_type == 0:
        if GL.PLAYER_MONEY >= GL.TOWER_PRICES[tower_type]:
            block.tower = GL.TOWER_TYPES[tower_type](block.position)
            GL.PLAYER_MONEY -= GL.TOWER_PRICES[tower_type]

def check_tower_blocks(mouse_pos):
    for block in BLOCKS:
        if block.position.distance_to(mouse_pos) <= 15:
            create_tower(block, 0)

def update_blocks(surface):
    for block in BLOCKS:
        block.update(surface)
