import unittest

def triangle ( a : int , b : int , c : int ) -> int :
    if ( a <= 0 or b <= 0 or c <= 0):
        return 4 # invalido
    if ( not (( a + b > c ) and ( a + c > b ) and ( b + c > a ))):
        return 4 # invalido
    if ( a == b and b == c ):
        return 1 # equilatero
    if ( a == b or b == c or a == c ):
        return 2 # isosceles
    return 3 # escaleno

class Test_triangulo(unittest.TestCase):
    def test_invalido(self):
        self.assertEqual(triangle(-1,-1,1),4)

    def test_invalido2(self):
        self.assertEqual(triangle(1,2,3),4)

    def test_isoseles(self):
        self.assertEqual(triangle(4,4,7),2)

    def test_equilatero(self):
        self.assertEqual(triangle(3,3,3),1)

    def test_escaleno(self):
        self.assertEqual(triangle(3,4,5),3)



