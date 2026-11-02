from queue import LifoQueue as Pila
from queue import Queue as Cola

import random
"""p:Pila[int]#creo pila tipo int
p.put(5)#apilo 5
p.put(2)
p.get()#desapilo el 5
elemento: int=p.get()#obtengo y guardo el ultimo elem
p.empty()#pregunto si esta vacia"""
def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    p:Pila[int]=Pila()
    for i in range(cantidad):
        p.put(random.randint(desde,hasta))
    return p#no se puede usar el .queue en pq no esta permitida, hay que hacer funcion imprimir
def imprimir_legal(p:Pila[int])->None:
    p_aux:Pila[int]=Pila()
    while not (p.empty()):
        elemento_acutal:int=p.get()
        p_aux.put(elemento_acutal)
        print(elemento_acutal)
    while not (p_aux.empty()):
        p.put(p_aux.get())

def buscar_el_maximo(p:Pila[int])->int:
    p_aux:Pila[int]=Pila()    
    max:int=p.get()
    p_aux.put(max)
    while not (p.empty()):
        elem_actual=p.get()
        p_aux.put(elem_actual)
        if (max<elem_actual):
            max=elem_actual
    while not (p_aux.empty()):
        p.put(p_aux.get())
    return max
pila:Pila[int]=generar_nros_al_azar(5,1,10)
# imprimir_legal(pila)
# print("esta es mi pila original")
# print(buscar_el_maximo(pila),"este es el maximo")
# print("despues")
# imprimir_legal(pila)

def armar_seciencia_de_bingo()->Cola[int]:
    lista:list[int]=range(0,100)
    lista=random.shuffle(lista)
    c:Cola[int]=Cola()
    for i in lista:
        c.put(i)
    return c

def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int])->int:
    res=0
    bolillero_aux:Cola[int]=Cola()
    carton_aux=carton.copy
    while len(carton_aux)>0:
        num:int=bolillero.get()
        if(num in carton_aux):
            carton_aux.remove(num)
        bolillero_aux.put(num)
        res+=1
    while not bolillero.empty:
        bolillero_aux.put(bolillero.get())
    while not bolillero_aux.empty:
        bolillero.put(bolillero_aux.get())
    return res

print