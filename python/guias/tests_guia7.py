import unittest 
from guia7 import *#el * importa todas las funciones

class Test_pertenece(unittest.TestCase):
    def test_pertenece(self):
        self.assertFalse(pertenece2([],2))
        self.assertFalse(pertenece2([1,2,3],4))
        self.assertTrue(pertenece2([1,2,3],3))

class Test_divide_a_todos(unittest.TestCase):
    def test_divide(self):
        self.assertTrue(divide_a_todos([],2))
        self.assertFalse(divide_a_todos([1,2,3,4],2))
        self.assertTrue(divide_a_todos([1,2,3,4,5],1))
        self.assertTrue(divide_a_todos([2,4,6,8],2))

class Test_suma_todos(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma_total([1,2,3]),6)
        self.assertEqual(suma_total([1,3]),4)
        self.assertEqual(suma_total([]),0)

class Test_max_y_min(unittest.TestCase):
    def test_max(self):
        self.assertEqual(maximo([1,2,3]),3)
        self.assertEqual(maximo([13,3]),13)
        self.assertEqual(maximo([-2]),-2)
    def test_min(self):
        self.assertEqual(minimo([1,2,3]),1)
        self.assertEqual(minimo([1,2,-1]),-1)
        self.assertEqual(minimo([4,31]),4)
        self.assertEqual(minimo([0,1,2,3]),0)
class Test_ordenados(unittest.TestCase):
    def test_lista_ordenada(self):
        self.assertFalse(ordenados([1,2,2,3]))
        self.assertFalse(ordenados([1,6,2,3]))
        self.assertTrue(ordenados([1,2,3]))

class Test_pos_max_y_min(unittest.TestCase):
    def test_pos_max(self):
        self.assertEqual(pos_maximo([0,2,0]),1)
        self.assertEqual(pos_maximo([2,2,2]),0)
        self.assertEqual(pos_maximo([22,2,0]),0)
        self.assertEqual(pos_maximo([]),-1)
    def test_pos_min(self):
        self.assertEqual(pos_minimo([10,-2,20]),1)
        self.assertEqual(pos_minimo([-2,-2,-2]),0)
        self.assertEqual(pos_minimo([-22,2,0]),0)
        self.assertEqual(pos_minimo([]),-1)

class Test_mayor7(unittest.TestCase):
    def test_mayor7(self):
        self.assertTrue(long_mayorASiete(["ana","aaaahjsj"]))
        self.assertFalse(long_mayorASiete(["adf"]))

class Test_palindroma(unittest.TestCase):
    def test_pal(self):
        self.assertTrue(es_palindroma("ana"))
        self.assertFalse(es_palindroma("adf"))
        self.assertTrue(es_palindroma(""))
        self.assertTrue(es_palindroma("a"))
class Test_iguales_consecutivos(unittest.TestCase):
    def test_iguales_consecutivos(self):
        self.assertTrue(iguales_consecutivos([1,1,1,1]))
        self.assertTrue(iguales_consecutivos([1,1,1]))
        self.assertFalse(iguales_consecutivos([]))
        self.assertFalse(iguales_consecutivos([2]))
        self.assertFalse(iguales_consecutivos([2,2]))

class Test_vocales_distintas(unittest.TestCase):
    def test_vocales(self):
        self.assertFalse(vocales_distintas("hola"))
        self.assertFalse(vocales_distintas(""))
        self.assertTrue(vocales_distintas("ehola"))
        self.assertTrue(vocales_distintas("eholauoa"))
        self.assertTrue(vocales_distintas("eholai"))
        self.assertFalse(vocales_distintas("aaaaa"))

class Test_sub_sec_ordenadas(unittest.TestCase):
    def test_pos_secuencia_ordenada_mas_larga(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([1,0,-3]),0)
        self.assertEqual(pos_secuencia_ordenada_mas_larga([2]),0)
        self.assertEqual(pos_secuencia_ordenada_mas_larga([1,0,2,3,4,5,6]),1)
        self.assertEqual(pos_secuencia_ordenada_mas_larga([1,2,3,4,5,6]),0)

class Test_sub_sec_ordenadas(unittest.TestCase):
    def test_cantidad_de_impares(self):
        self.assertEqual(cantidad_digitos_impares([4,20,2]),0)
        self.assertEqual(cantidad_digitos_impares([4233,20,2]),2)
        self.assertEqual(cantidad_digitos_impares([14,120,12]),3)
        self.assertEqual(cantidad_digitos_impares([77]),2)


if __name__ == '__main__':
    unittest.main(verbosity=2)