from vessel import *
import unittest
from weapon import *


class ChaineDeCaractereTest(unittest.TestCase):

    def test_cordinate(self):
        a=Vessel((2,4,-1),1,AntiAir())
        self.assertEqual((2,4,-1),a._get_coordinates())
        
   
    def test_to_go(self):
        a=Vessel((2,4,-1),3,AntiAir())
        a._go_to(0,2,3)
        self.assertEqual((0,2,3), a._get_coordinates())

if __name__ == '__main__':
    unittest.main()  