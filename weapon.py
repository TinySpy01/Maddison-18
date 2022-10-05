class Weapon:
    def __init__(self, ammunition: int, range: int):
        self.ammuntion = ammunition
        self.range = range

    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition==0 : 
            raise NoAmmunitionError("No Ammunition!")
            

class Antisurface(Weapon):
    def __init__(self, ammunition: int, range: int):
        super().__init__(ammunition,range)
        
        
        
    
    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition==0 : 
            raise NoAmmunitionError("No Ammunition!")
        if z!=0 : 
            self.ammunition-=1
            raise OutOfRangeError("L'Antisurface ne marche qu'altitude nulle!")
            
          
class AntiAir(Weapon):
    def __init__(self, ammunition: int, range: int):
        super().__init__(ammunition,range)
        
        
        
    
    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition==0 : 
            raise NoAmmunitionError("No Ammunition!")
        if z=<0 : 
            self.ammunition-=1
            raise OutOfRangeError("L'Antiair ne marche qu'altitude strictement positive!")
            
            
class Lance-Torpilles(Weapon):
    def __init__(self, ammunition: int, range: int):
        super().__init__(ammunition,range)
       
        
        
    
    def _fire_at(self, x: int, y: int, z: int):
        if self.ammunition==0 : 
            raise NoAmmunitionError("No Ammunition!")
        if z>0 : 
            self.ammunition-=1
            raise OutOfRangeError("Le Lance-Torpilles ne marche qu'altitude négative!")
                        
            
     
                        

