from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
#Pilas
def imprimir_legal(p:Pila[int])->None:
    elemento_acutal:int
    p_aux:Pila[int]=Pila()
    while not (p.empty()):
        elemento_acutal=p.get()
        p_aux.put(elemento_acutal)
        print(elemento_acutal)
    while not (p_aux.empty()):
        p.put(p_aux.get())

def devuelta(q:Pila,p:Pila)->None:
    while not(p.empty()):
        q.put(p.get())

def devuelta_cola(q:Cola,p:Cola)->None:
    while not(p.empty()):
        q.put(p.get())
#Ejercicio 1

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    res:Pila[int]=Pila()
    for _ in range(cantidad):
        res.put(random.randint(desde,hasta))
    return res

def cantidad_elementos(p:Pila[int])->int:
    p_aux:Pila[int]=Pila()
    elemento:int
    contador:int=0
    while not (p.empty()):
        elemento=p.get()
        contador+=1
        p_aux.put(elemento)
    while not (p_aux.empty()):
        elemento=p_aux.get()
        p.put(elemento)
    return contador

def buscar_el_maximo(p:Pila[int])->int:
    max_temp:int
    p_aux:Pila[int]=Pila()
    max_actual:int=p.get()
    p_aux.put(max_actual)
    while not p.empty():
        max_temp=p.get()
        p_aux.put(max_temp)
        if max_temp>max_actual:
            max_actual=max_temp
    while not (p_aux.empty()):
        p.put(p_aux.get())
    return max_actual

def buscar_nota_maxima(p:Pila[tuple[str,int]])->tuple[str,int]:
    tupla_res:tuple[str,int]=p.get()
    res_aux:tuple[str,int]
    p_aux:Pila[tuple[str,int]]=Pila()
    p_aux.put(tupla_res)
    while not(p.empty()):
        res_aux=p.get()
        if (tupla_res[1]<res_aux[1]):
            tupla_res=res_aux
        p_aux.put(res_aux)
    devuelta(p,p_aux)
    return tupla_res
    
def esta_bien_balanceada(s:str)->bool:
    res:int=0
    operacion:Pila[str]=Pila()
    car:str
    for caracter in s:
        operacion.put(caracter)
    while (not(operacion.empty()))and res>=0:
        car=operacion.get()
        if(car==")"):
            res=res+1
        elif(car=="("):
            res=res-1
    return(res==0)

def evaluar_expresion(s:str)->float:
    operaciones:list[str]=["+", "-", "*", "/"]
    token:Pila[float]=Pila()
    for unidad in s.split(" "):
        if unidad in operaciones:
            if unidad=="+":
                primero=token.get()
                token.put(primero+token.get())
            elif unidad=="-":
                primero=token.get()
                token.put(token.get()-primero)
            elif unidad=="/":
                primero=token.get()
                token.put(token.get()/primero)
            elif unidad=="*":
                primero=token.get()
                token.put(primero*token.get())
        else:
            token.put(float(unidad))
    return(float(token.get()))


def intercalar(p1:Pila,p2:Pila)->Pila:
    res_aux:Pila=Pila()
    res:Pila=Pila()
    p1_aux:Pila=Pila()
    p2_aux:Pila=Pila()
    while not (p1.empty()):
        elem_p1=p1.get()
        elem_p2=p2.get()
        p1_aux.put(elem_p1)
        p2_aux.put(elem_p2)
        res_aux.put(elem_p1)
        res_aux.put(elem_p2)
    while not (res_aux.empty()):
        res.put(res_aux.get())
    devuelta(p1,p1_aux)
    devuelta(p2,p2_aux)
    return res

#Colas
def generar_nros_al_azar_cola(cantidad:int,desde:int,hasta:int)->Cola[int]:
    res:Cola[int]=Cola()
    for _ in range(cantidad):
        res.put(random.randint(desde,hasta))
    return res

def cantidad_elementos_cola(c:Cola)->int:
    c_aux:Cola=Cola()
    contador:int=0
    while not (c.empty()):
        contador+=1
        c_aux.put(c.get())
    devuelta_cola(c,c_aux)
    return contador

def buscar_el_maximo_cola(c:Cola[int])->int:
    max_actual:int=c.get()
    temp:int
    c_aux:Cola[int]=Cola()
    c_aux.put(max_actual)
    while not (c.empty()):
        temp=c.get()
        c_aux.put(temp)
        if max_actual<temp:
            max_actual=temp
    devuelta_cola(c,c_aux)
    return max_actual

def buscar_nota_minima(c:Cola[tuple[str,int]])->tuple[str,int]:
    tupla_res:tuple[str,int]=c.get()
    res_aux:tuple[str,int]
    c_aux:Cola[tuple[str,int]]=Cola()
    c_aux.put(tupla_res)
    while not(c.empty()):
        res_aux=c.get()
        if (tupla_res[1]>res_aux[1]):
            tupla_res=res_aux
        c_aux.put(res_aux)
    devuelta_cola(c,c_aux)
    return tupla_res

def intercalar_cola(c1:Cola,c2:Cola)->Cola:
    res:Cola=Cola()
    c1_aux:Cola=Cola()
    c2_aux:Cola=Cola()
    while not (c1.empty()):
        elem_c1=c1.get()
        elem_c2=c2.get()
        c1_aux.put(elem_c1)
        c2_aux.put(elem_c2)
        res.put(elem_c1)
        res.put(elem_c2)
    devuelta_cola(c1,c1_aux)
    devuelta_cola(c2,c2_aux)
    return res

def armar_secuencia_de_bingo()->Cola[int]:
    lista:list[int]=list(range(0,100))
    random.shuffle(lista)
    c:Cola[int]=Cola()
    for i in lista:
        c.put(i)
    return c

def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int])->int:
    carton_aux=carton.copy()
    jugadas:int=0
    bolillero_aux:Cola[int]=Cola()
    bola_actual:int
    while len(carton_aux)>0:
        bola_actual=bolillero.get()
        bolillero_aux.put(bola_actual)
        if bola_actual in carton_aux:
            carton_aux.remove(bola_actual)
        jugadas+=1
    while not (bolillero.empty()):
        bolillero_aux.put(bolillero.get())
    devuelta_cola(bolillero,bolillero_aux)
    return jugadas
#Ejercicio 14
def pacientes_urgentes(c:Cola[tuple[int,str,str]])->int:
    contador:int=0
    c_aux:Cola[tuple[int,str,str]]=Cola()
    paciente:tuple[int,str,str]
    while not (c.empty()):
        paciente=c.get()
        c_aux.put(paciente)
        if paciente[0]<4:
            contador+=1
    devuelta_cola(c,c_aux)
    return contador


#Ejercicio 15
#especificacion
# problema atencion_a_clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]]{
#   requiere{}
#   asegura: {res tiene los mismos elementos que c (mismas repeticiones)}
#   asegura: {primero están en res los clientes con prioridad (índice 3 en true),
#             luego los de cuenta preferencial sin prioridad (índice 2 en true),
#             y por último el resto}
#   asegura: {dentro de cada subgrupo se mantiene el orden relativo que tenían en c}
#   asegura: {c no se modifica}
# }
def atencion_a_clientes(c:Cola[tuple[str,int,bool,bool]])->Cola[tuple[str,int,bool,bool]]:
    c_aux:Cola[tuple[str,int,bool,bool]]=Cola()
    cliente_actual:tuple[str,int,bool,bool]
    res:Cola[tuple[str,int,bool,bool]]=Cola()
    prioridad:Cola[tuple[str,int,bool,bool]]=Cola()
    preferencial:Cola[tuple[str,int,bool,bool]]=Cola()
    resto:Cola[tuple[str,int,bool,bool]]=Cola()
    while not (c.empty()):
        cliente_actual=c.get()
        c_aux.put(cliente_actual)
        if(cliente_actual[3]):#prioridad
            prioridad.put(cliente_actual)
        elif(cliente_actual[2]):#preferencial
            preferencial.put(cliente_actual)
        else:#resto
            resto.put(cliente_actual)
    devuelta_cola(res,prioridad)
    devuelta_cola(res,preferencial)
    devuelta_cola(res,resto)
    devuelta_cola(c,c_aux)
    return res



        