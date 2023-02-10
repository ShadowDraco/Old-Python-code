import enemy

class Grog(enemy.Enemy):
    def __init__(self, number):
        super().__init__(1, 1, 2,"Grog", "enemies/RedCube")
        self.number = number

    

