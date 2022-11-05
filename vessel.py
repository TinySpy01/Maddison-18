from weapon import *
from math import dist

class Vessel:
    def __init__(self,coordinates:tuple,max_hits:int,weapon:Weapon):
        self.coordinates=coordinates
        self.max_hits=max_hits
        self.weapon=weapon
    def _go_to(self,x,y,z,):
        self.coordinates=(x,y,z)
    def _get_coordinates(self):
        return self.coordinates
    def _fire_at(self,x,y,z):
        return None

