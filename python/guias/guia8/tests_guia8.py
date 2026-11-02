import unittest 
from guia8 import *

class Test_Pilas(unittest.TestCase):
    def test_cantidad_elementos(self):
        p=generar_nros_al_azar(3,1,2)
        p1=generar_nros_al_azar(0,1,2)
        self.assertEqual(cantidad_elementos(p),3)
        self.assertEqual(cantidad_elementos(p1),0)
    def test_bucar_el_max(self):
        p=Pila()
        p.put(1)
        p.put(2)
        p.put(3)
        p.put(4)
        p.put(5)
        self.assertEqual(buscar_el_maximo(p),5)
    def test_buscar_nota_max(self):
        p=Pila()
        p.put(("a",10))
        self.assertEqual(buscar_nota_maxima(p),("a",10))
        p.put(("b",11))
        self.assertEqual(buscar_nota_maxima(p),("b",11))
    def test_balance_de_ecuacion(self):
        self.assertFalse(esta_bien_balanceada("2+)-3*4("))
        self.assertFalse(esta_bien_balanceada("((2+)-3*4("))
        self.assertTrue(esta_bien_balanceada("()"))
        self.assertTrue(esta_bien_balanceada("(1+2+3)*(3)"))
        self.assertTrue(esta_bien_balanceada("(())"))
    def test_evaluar_expresion(self):
        self.assertEqual(evaluar_expresion("3 4 + 5 * 2 -"),33)
        self.assertEqual(evaluar_expresion("7"), 7)
        self.assertEqual(evaluar_expresion("7"), 7)
        self.assertAlmostEqual(evaluar_expresion("1 3 /"), 1 / 3)
    def test_intercalar(self):
        p1, p2 = Pila(), Pila()
        for x in [1, 2, 3]: p1.put(x)
        for x in [4, 5, 6]: p2.put(x)

        res = intercalar(p1, p2)

        salida = []
        while not res.empty():
            salida.append(res.get())
        self.assertEqual(salida, [3, 6, 2, 5, 1, 4])
        self.assertEqual(p1.qsize(), 3)   # p1 y p2 se restauran
        self.assertEqual(p2.qsize(), 3)

class Test_Colas(unittest.TestCase):
    def test_cantidad_elementos_cola(self):
        self.assertEqual(cantidad_elementos_cola(generar_nros_al_azar_cola(3,1,3)),3)
        self.assertEqual(cantidad_elementos_cola(generar_nros_al_azar_cola(6,1,3)),6)
        self.assertEqual(cantidad_elementos_cola(generar_nros_al_azar_cola(0,1,3)),0)
    def test_buscar_max_cola(self):
        p=Cola()
        p.put(1)
        p.put(2)
        p.put(3)
        p.put(4)
        p.put(5)
        self.assertEqual(buscar_el_maximo(p),5)

    def test_buscar_nota_minima(self):
        p=Cola()
        p.put(("a",10))
        self.assertEqual(buscar_nota_minima(p),("a",10))
        p.put(("b",11))
        self.assertEqual(buscar_nota_minima(p),("a",10))
        p.put(("c",1))
        self.assertEqual(buscar_nota_minima(p),("c",1))
def armar_cola(elementos: list) -> Cola:
    c: Cola = Cola()
    for x in elementos:
        c.put(x)
    return c

def cola_a_lista(c: Cola) -> list:
    res = []
    while not c.empty():
        res.append(c.get())
    return res


class TestArmarSecuenciaDeBingo(unittest.TestCase):

    def test_tiene_100_elementos(self):
        self.assertEqual(len(cola_a_lista(armar_secuencia_de_bingo())), 100)

    def test_contiene_todos_los_numeros_sin_repetir(self):
        elementos = cola_a_lista(armar_secuencia_de_bingo())
        self.assertEqual(sorted(elementos), list(range(0, 100)))

    def test_todos_son_enteros_en_rango(self):
        for x in cola_a_lista(armar_secuencia_de_bingo()):
            self.assertIsInstance(x, int)
            self.assertTrue(0 <= x <= 99)

    def test_no_queda_ordenada(self):
        # La probabilidad de que salga ordenada por azar es 1/100!
        elementos = cola_a_lista(armar_secuencia_de_bingo())
        self.assertNotEqual(elementos, list(range(0, 100)))

    def test_dos_llamadas_dan_secuencias_distintas(self):
        a = cola_a_lista(armar_secuencia_de_bingo())
        b = cola_a_lista(armar_secuencia_de_bingo())
        self.assertNotEqual(a, b)


class TestJugarCartonDeBingo(unittest.TestCase):

    def test_carton_vacio(self):
        self.assertEqual(jugar_carton_de_bingo([], armar_cola([1, 2, 3])), 0)

    def test_un_numero_que_sale_primero(self):
        self.assertEqual(jugar_carton_de_bingo([1], armar_cola([1, 2, 3])), 1)

    def test_un_numero_que_sale_ultimo(self):
        self.assertEqual(jugar_carton_de_bingo([3], armar_cola([1, 2, 3])), 3)

    def test_dos_numeros(self):
        # Se completa cuando sale el 3 (tercera bola)
        self.assertEqual(jugar_carton_de_bingo([3, 1], armar_cola([1, 2, 3, 4, 5])), 3)

    def test_el_orden_del_carton_no_importa(self):
        self.assertEqual(
            jugar_carton_de_bingo([5, 4, 3, 2, 1], armar_cola([1, 2, 3, 4, 5])), 5)
        self.assertEqual(
            jugar_carton_de_bingo([1, 2, 3, 4, 5], armar_cola([1, 2, 3, 4, 5])), 5)

    def test_numeros_que_salen_salteados(self):
        # Completa con el 9, que es la quinta bola
        self.assertEqual(jugar_carton_de_bingo([9, 2], armar_cola([2, 7, 8, 1, 9, 4])), 5)

    def test_carton_completo_con_secuencia_aleatoria(self):
        carton = list(range(0, 100))
        self.assertEqual(jugar_carton_de_bingo(carton, armar_secuencia_de_bingo()), 100)

    def test_jugadas_dentro_de_los_limites(self):
        jugadas = jugar_carton_de_bingo([10, 20, 30], armar_secuencia_de_bingo())
        self.assertTrue(3 <= jugadas <= 100)

    def test_el_carton_no_se_modifica(self):
        carton = [3, 1]
        jugar_carton_de_bingo(carton, armar_cola([1, 2, 3, 4, 5]))
        self.assertEqual(carton, [3, 1])

    def test_el_bolillero_se_restaura_completo_y_en_orden(self):
        bolillero = armar_cola([1, 2, 3, 4, 5])
        jugar_carton_de_bingo([3, 1], bolillero)
        self.assertEqual(cola_a_lista(bolillero), [1, 2, 3, 4, 5])

    def test_bolillero_se_restaura_con_carton_vacio(self):
        bolillero = armar_cola([1, 2, 3])
        jugar_carton_de_bingo([], bolillero)
        self.assertEqual(cola_a_lista(bolillero), [1, 2, 3])

    def test_bolillero_se_restaura_si_se_usa_todo(self):
        bolillero = armar_cola([1, 2, 3])
        jugar_carton_de_bingo([1, 2, 3], bolillero)
        self.assertEqual(cola_a_lista(bolillero), [1, 2, 3])
class TestPacientesUrgentes(unittest.TestCase):
    def test_pacientes_urgentes(self):
        p=Cola()
        self.assertEqual(pacientes_urgentes(p),0)
        p.put((2,"a","b"))
        self.assertEqual(pacientes_urgentes(p),1)

class TestAtencionAClientes(unittest.TestCase):

    def test_cola_vacia(self):
        self.assertEqual(cola_a_lista(atencion_a_clientes(armar_cola([]))), [])

    def test_un_cliente(self):
        a = ("Ana Perez", 1, False, False)
        self.assertEqual(cola_a_lista(atencion_a_clientes(armar_cola([a]))), [a])

    def test_orden_entre_grupos(self):
        resto = ("Resto", 1, False, False)
        pref = ("Pref", 2, True, False)
        prio = ("Prio", 3, False, True)
        res = atencion_a_clientes(armar_cola([resto, pref, prio]))
        self.assertEqual(cola_a_lista(res), [prio, pref, resto])

    def test_prioridad_y_preferencial_va_con_prioridad(self):
        ambos = ("Ambos", 1, True, True)
        pref = ("Pref", 2, True, False)
        res = atencion_a_clientes(armar_cola([pref, ambos]))
        self.assertEqual(cola_a_lista(res), [ambos, pref])

    def test_respeta_orden_de_llegada_dentro_de_cada_grupo(self):
        p1 = ("P1", 1, False, True)
        p2 = ("P2", 2, True, True)
        f1 = ("F1", 3, True, False)
        f2 = ("F2", 4, True, False)
        r1 = ("R1", 5, False, False)
        r2 = ("R2", 6, False, False)
        entrada = [r1, f1, p1, r2, f2, p2]
        res = atencion_a_clientes(armar_cola(entrada))
        self.assertEqual(cola_a_lista(res), [p1, p2, f1, f2, r1, r2])

    def test_todos_del_mismo_grupo_conserva_orden(self):
        r1 = ("R1", 1, False, False)
        r2 = ("R2", 2, False, False)
        r3 = ("R3", 3, False, False)
        res = atencion_a_clientes(armar_cola([r1, r2, r3]))
        self.assertEqual(cola_a_lista(res), [r1, r2, r3])

    def test_misma_cantidad_de_clientes(self):
        entrada = [("A", 1, False, False), ("B", 2, True, False), ("C", 3, False, True)]
        res = atencion_a_clientes(armar_cola(entrada))
        self.assertEqual(len(cola_a_lista(res)), 3)

    def test_la_cola_original_no_se_modifica(self):
        entrada = [("A", 1, False, False), ("B", 2, True, False), ("C", 3, False, True)]
        c = armar_cola(entrada)
        atencion_a_clientes(c)
        self.assertEqual(cola_a_lista(c), entrada)


if __name__ == '__main__':
    unittest.main(verbosity=2)