import projectile

class Bullet(projectile.Projectile):
    def __init__(self, number, position, target, tower, velocity):
        super().__init__(position, target, tower, velocity, 2, "Bullet", "towers/WhiteCube")
        self.number = number

    

