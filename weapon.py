class Weapon:
    def __init__(self, ammunition: int, range: int):
        self.ammuntion = ammunition
        self.range = range

    def _fire_at(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z



Lance_missiles_antisurface = Weapon(40,30)
Lance_missiles_anti_air = Weapon(50,40)
Lance_torpilles = Weapon(15,20)