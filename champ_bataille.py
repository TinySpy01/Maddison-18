from weapon import *
from math import dist
from vessel import Vessel
from cruiser import Cruiser
from submarine import Submarine
from fregate import Fregate
from destroyer import Destroyer
from aircraft import Aircraft

class Champ_bataille():
    def __init__(self):
        #L'idée est de représenter le champ de bataille par une grande liste contenant toutes les positions dans l'espace 3d, et on l'initie avec des 0
        Lz=3*[0] #On décale les z de 1 vu l'impossibilité d'ordonner les éléments d'une liste à partir de -1
        Ly_z=[Lz for i in range (100)]
        self.champ_bataille=[Ly_z for i in range (100)] #Par exemple Champ_bataille[23][42][0] donnerait le vaisseau se trouvant à x=23, y=42 et z=-1 (décalage), ou 0 si la position est vide
        self.C=0 #capacité du champ de bataille

    def Add_vessel(self,vessel:Vessel,x:int,y:int,z:int):
        if x>=0 and x<=100 and y>=0 and y<=100 and z in [-1,0,1]:
            if self.champ_bataille[x][y][z+1]==0 and (self.C)+vessel.max_hits<=22:
                self.champ_bataille[x][y][z+1]=vessel

        else: raise Exception ("OutOfSpace")

    def Recieve_hit(self,x:int,y:int,z:int):
        if x>=0 and x<=100 and y>=0 and y<=100 and z in [-1,0,1]:
            if self.champ_bataille[x][y][z+1]==0: return False
            else: return True
        else: raise Exception ("OutOfSpace")






                
                



        



        
        




