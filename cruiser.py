from weapon import *
from math import dist
from vessel import Vessel

class Cruiser(Vessel):
    def __init__(self, coordinates,max_hits,weapon:Weapon):
        super().__init__(coordinates,max_hits)
        self.max_hits=6
        self.weapon=weapon.AntiAir

    def _go_to(self,x,y,z,):
        if self.coordinates[2]==0:
            self.coordinates=(x,y,z)
        else: raise Exception ("Out of Cruiser range")    
   
    def _fire_at(self,x,y,z):
        if self.max_hits==0:
            raise Exception ("DestroyedError")
        if dist((x,y,z),self.coordinates)>self.weapon.range:
            self.weapon.ammunition-=1
            raise Exception ("OutOfRangeError")