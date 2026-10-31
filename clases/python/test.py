import unittest 
from clase7_10 import *#el * importa todas las funciones

class Test_suma_total(unittest.TestCase):
    def test_suma_total(self):
        self.assertEqual(suma_total([1,2,3]),6)
        self.assertEqual(suma_total([]),0)

class Test_pertenece(unittest.TestCase):
    def test_pertenece(self):
        self.assertFalse(pertenece([],2))
        self.assertFalse(pertenece([1,2,3],4))
        self.assertTrue(pertenece([1,2,3],3))


if __name__ == '__main__':
    unittest.main(verbosity=2)