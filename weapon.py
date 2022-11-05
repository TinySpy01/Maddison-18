from math import sqrt

#Définir les exceptions

class NoAmmunitionError(Exception):
    pass
class OutOfRangeError(Exception):
    pass


class Weapon:
    def __init__(self, ammunition: int, range: int):
        self.ammunition = ammunition
        self.range = range

    def fire_at(self, x, y, z):
        if self.ammunition == 0:
            raise NoAmmunitionError
        self.ammunition -= 1
        if sqrt(x ** 2 + y ** 2) > self.range:
            raise OutOfRangeError



# Définir les armes

class Antisurface(Weapon):
    def __init__(self) -> None:
        super().__init__(40, 30)
    def fire_at(self,x, y, z):
        super().fire_at(x,y,z)
        if z != 0:
            raise OutOfRangeError


class AntiAir(Weapon):

    def __init__(self) -> None:
        super().__init__(50, 40)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z <= 0:
            raise OutOfRangeError



class Lance_Torpilles(Weapon):
    def __init__(self) -> None:
        super().__init__(15, 20)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z > 0:
            raise OutOfRangeError


# Test unitaire:
if __name__ == "__main__":
    AntiAir = AntiAir()
    Antisurface = Antisurface()
    Lance_Torpilles= Lance_Torpilles()
    Antisurface.fire_at(0,0,0)
    assert Antisurface.ammunition == 39
    try:
        Antisurface.fire_at(0,0,1)
    except:
        assert Antisurface.ammunition == 38
    AntiAir.fire_at(0,0,1)
    assert AntiAir.ammunition == 49
    try:
        AntiAir.fire_at(0,0,0)
    except:
        assert AntiAir.ammunition == 48
    Lance_Torpilles.fire_at(0,0,0)
    assert Lance_Torpilles.ammunition == 14
    Lance_Torpilles.fire_at(0,0,-1)
    assert Lance_Torpilles.ammunition == 13
    try:
        Lance_Torpilles.fire_at(0,0,1)
    except:
        assert Lance_Torpilles.ammunition == 12
