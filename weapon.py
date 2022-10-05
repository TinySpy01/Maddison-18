class Weapon:
    def __init__(self, ammunition: int, range: int):
        self.ammuntion = ammunition
        self.range = range

    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            raise Exception("NoAmmunitionError")


class Antisurface(Weapon):
    def __init__(self, ammunition: int, range: int):
        super().__init__(ammunition, range)

    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            raise Exception("NoAmmunitionError")
        if z != 0:
            self.ammunition -= 1
            raise Exception("OutOfRangeError")


class AntiAir(Weapon):
    def __init__(self, ammunition: int, range: int):
        super().__init__(ammunition, range)

    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            raise Exception("NoAmmunitionError")
        if z= < 0:
            self.ammunition -= 1
            raise Exception("OutOfRangeError")


class Lance_Torpilles(Weapon):
    def __init__(self, ammunition: int, range: int):
        super().__init__(ammunition, range)

    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition == 0:
            raise Exception("NoAmmunitionError")
        if z > 0:
            self.ammunition -= 1
            raise Exception("OutOfRangeError")
