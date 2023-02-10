import tower
import projectile_types as PT

class Bullet_Tower(tower.Tower):
    def __init__(self, position):
        super().__init__(position, 100, 30, "Grog", PT.Bullet, "towers/WhiteCube")

    

