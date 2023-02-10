import block

class Tower_Block(block.Block):
    def __init__(self, number, position):
        super().__init__(position, "Tower", "blocks/tower_block")
        self.number = number
    

    

