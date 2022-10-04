class Weapon:
    def __init__(self, ammunition: int, range:int):
        self.ammuntion=ammunition
        self.range=range

    def _fire_at(self,x: int,y:int,z:int):
        self.x=x
        self.y=y
        self.z=z
