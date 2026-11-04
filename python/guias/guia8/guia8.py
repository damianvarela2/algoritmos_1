from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import Union
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

def pila_a_lista(p: Pila) -> list:
    aux: list = []
    while not p.empty():
        aux.append(p.get())
    for elem in reversed(aux):
        p.put(elem)
    return aux[::-1]

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


#Diccionarios
#Ejercicio 16
def calcular_promedio_por_estudiante(notas:list[tuple[str,float]])->dict[str,float]:
    d_aux:dict[str,list[float]]={}
    d:dict[str,float]={}
    for alumno in notas:
        if alumno[0] not in (d_aux.keys()):
            d_aux[alumno[0]]=[alumno[1]]
        else:
            d_aux[alumno[0]].append(alumno[1])
    for (alumno1,notas1) in d_aux.items():
        d[alumno1]=sum(notas1)/len(notas1)
    return d

#Ejercicio 17
def lista_a_pila(lista) -> Pila:
    p: Pila = Pila()
    for elem in lista:
        p.put(elem)
    return p

histA:Pila[str]=lista_a_pila(["LINK1","LINK2"])
histB:Pila[str]=lista_a_pila(["LINK3","LINK4"])
histC:Pila[str]=lista_a_pila(["LINK5","LINK6"])
histD:Pila[str]=lista_a_pila(["LINK7","LINK8"])


historiales:dict[str,Pila[str]]={
    "a":histA,
    "b":histB,
    "c":histC,
    "d":histD
}



def visitar_sitio(historiales:dict[str,Pila[str]],usuario:str,sitio:str):
    historial_actual:Pila[str]=Pila()
    if usuario in historiales.keys():
        historial_actual=historiales[usuario]
        historial_actual.put(sitio)
    else:
        historial_actual=Pila()
        historial_actual.put(sitio)
        historiales[usuario]=historial_actual

def navegar_atras(historiales:dict[str,Pila[str]],usuario:str)->str:
    res:str
    res=historiales[usuario].get()
    return(res)

def agregar_producto(inventario:dict[str,dict[str,Union[int,float]]],nombre:str,precio:float,cantidad:int):
    inventario[nombre]={"precio":precio,"cantidad":cantidad}

def actualizar_stock(inventario:dict[str,dict[str,Union[int,float]]],nombre:str,cantidad:int):
    precio:float=inventario[nombre]["precio"]
    inventario[nombre]={"precio":precio,"cantidad":cantidad}

def calcular_valor_inventario(inventario:dict[str,dict[str,Union[int,float]]])->float:
    valor:float=0.0
    for nombre in inventario.keys():
        valor=valor+inventario[nombre]["precio"]*inventario[nombre]["cantidad"]
    return valor

#Archivos
def contar_lineas(nombre_archivo:str)->int:
    archivo = open(nombre_archivo, 'r')
    lista:list[str]=archivo.readlines()
    archivo.close()
    return(len(lista))

def exista_palabra(nombre_archivo:str,palabra:str)->bool:
    lista_palabras:list[str]=[]
    pal:str=""
    archivo = open(nombre_archivo, 'r')
    lineas=archivo.readlines()
    for linea in lineas:
        for caracter in linea:
            if caracter != " " and caracter!="\n":
                pal=pal+caracter
            elif pal != "":
                lista_palabras.append(pal)
                pal=""
        if pal != "":
            lista_palabras.append(pal)
            pal=""

    archivo.close()
    return(palabra in lista_palabras)

def cantidad_de_apariciones(nombre_archivo:str,palabra:str)->int:
    archivo = open(nombre_archivo, 'r')
    lista_palabras:list[str]=lista_de_palabras(archivo.readlines())
    archivo.close()
    return(lista_palabras.count(palabra))


def lista_de_palabras(lineas:list[str])->list[str]:
    pal:str=""
    res:list[str]=[]
    for linea in lineas:
        for caracter in linea:
            if caracter!=" " and caracter != "\n":
                pal=pal+caracter
            elif(pal!=""):
                res.append(pal)
                pal=""
        if(pal!=""):
            res.append(pal)
            pal=""
    return res

#Ejercicio 20
def agrupar_por_longitud(nombre_archivo:str)->dict[int,int]:
    res:dict[int,int]={}
    contador_actual:int
    archivo=open(nombre_archivo,'r')
    lineas:list[str]=archivo.readlines()
    archivo.close()
    lista_palabras:list[str]=lista_de_palabras(lineas)
    for palabra in lista_palabras:
        if len(palabra) not in res.keys():
            res[len(palabra)]=1
        else:
            contador_actual=res[len(palabra)]
            res[len(palabra)]=contador_actual+1
    return res

def la_palabra_mas_frecuente(nombre_archivo:str)->str:
    palabra_actual:str=""
    contador_palabra_actual:int=0
    archivo=open(nombre_archivo,'r')
    lista_lineas:list[str]=archivo.readlines()
    archivo.close()
    lista_palabras:list[str]=lista_de_palabras(lista_lineas)
    for palabra in lista_palabras:
        n:int=lista_palabras.count(palabra)
        if n>contador_palabra_actual:
            palabra_actual=palabra
            contador_palabra_actual=n
    return palabra_actual

# def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
#     archivo = open(nombre_archivo, 'r')
#     lista_lineas: list[str] = archivo.readlines()
#     archivo.close()

#     lista_palabras: list[str] = lista_de_palabras(lista_lineas)

#     frecuencias: dict[str, int] = {}

#     for palabra in lista_palabras:
#         if palabra in frecuencias:
#             frecuencias[palabra] += 1
#         else:
#             frecuencias[palabra] = 1

#     palabra_actual: str = ""
#     contador_palabra_actual: int = 0

#     for palabra in frecuencias:
#         if frecuencias[palabra] > contador_palabra_actual:
#             palabra_actual = palabra
#             contador_palabra_actual = frecuencias[palabra]

#     return palabra_actual

def clonar_sin_comentarios(nombre_archivo_entrada:str,nombre_archivo_salida:str)->None:
    archivo=open(nombre_archivo_entrada,'r')
    lista_lineas:list[str]=archivo.readlines()
    archivo.close()
    lista_sin_comentarios:list[str]=[]
    for linea in lista_lineas:
        if not es_comentario(linea):
            lista_sin_comentarios.append(linea)
    archivo=open(nombre_archivo_salida,'w')
    for linea in lista_sin_comentarios:
        archivo.write(linea)
    archivo.close()

def es_comentario(linea:str)->bool:
    contador:int=0
    caracter:str=linea[contador]
    while caracter==" " and contador<len(linea):
        contador+=1
        caracter=linea[contador]
    return(contador<len(linea) and caracter=="#")

#Ejercicio 23
def invertir_lineas(nombre_archivo_entrada:str,nombre_archivo_salida:str)->None:
    archivo=open(nombre_archivo_entrada,'r')
    lista_lineas:list[str]=archivo.readlines()
    archivo.close()
    lista:list[str]=invertir_lista(lista_lineas)
    archivo=open(nombre_archivo_salida,'w')
    for linea in lista:
        archivo.write(linea)
    archivo.close()

def invertir_lista(lista:list[str])->list[str]:
    res:list[str]=[]
    for elemento in lista:
        res=elemento+res
    return res

#Ejercicio 24
def agregar_frase_al_final(nombre_archivo:str,frase:str)->None:
    archivo = open(nombre_archivo, 'r')
    contenido: str = archivo.read()
    archivo.close()
    archivo = open(nombre_archivo, 'w')
    archivo.write(contenido + "\n" + frase)
    archivo.close()

#Ejercicio 25
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    archivo = open(nombre_archivo, 'r')
    contenido: str = archivo.read()
    archivo.close()
    archivo = open(nombre_archivo, 'w')
    archivo.write(frase + "\n" + contenido)
    archivo.close()

#Ejercicio 26
def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    archivo = open(nombre_archivo, 'rb')
    contenido: bytes = archivo.read()
    archivo.close()

    res: list[str] = []
    actual: str = ""
    for byte in contenido:
        c: str = chr(byte)
        if es_legible(c):
            actual = actual + c
        else:
            if len(actual) >= 5:
                res.append(actual)
            actual = ""
    if len(actual) >= 5:
        res.append(actual)
    return res

def es_legible(c:str)->bool:
    return (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') or c == ' ' or c == '_')

#Ejercicio 27
def calcular_promedio_por_estudiante(nombre_archivo_notas:str,nombre_archivo_promedio:str)->None:
    archivo=open(nombre_archivo_notas,'r')
    lineas:list[str]=archivo.readlines()
    archivo.close()
    archivo=open(nombre_archivo_promedio,'w')
    for lu in lista_de_lu(lineas):
        archivo.write(lu + ","+ promedio_estudiante(lineas,lu))
    archivo.close()

def lista_de_lu(notas_de_estudiantes:list[str])->list[str]:
    res:list[str]=[]
    for linea in notas_de_estudiantes:
        lu:str=separar_por_coma(linea)[0]
        if lu not in res and lu!="":
            res.append(lu)
    return res

def promedio_estudiante(notas_de_estudiantes:list[str],lu:str)->float:
    notas:list[float]=[]
    for linea in notas_de_estudiantes:
        info:list[str]=separar_por_coma(linea)
        if info[0]==lu:
            notas.append(float(info[3]))
    return(sum(notas)/len(notas))

def separar_por_coma(linea:str)->list[str]:
    res:list[str]=[]
    agrego:str=""
    for caracter in linea:
        if caracter==",":
            res.append(agrego)
            agrego = ""
        elif caracter!="\n":
            agrego=agrego+caracter
    res.append(agrego)
    return res