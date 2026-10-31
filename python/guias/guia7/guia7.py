#Ejercicio 1
#1
def pertenece1(s:list[int],n:int)->bool:
    return n in s

def pertenece2(s:list[int],n:int)->bool:
    esta:bool=False
    for i in range (len(s)):
        if n==s[i]:
            esta=True
    return esta

def pertenece3(s:list[int],n:int)->bool:
    esta:bool=False
    for i in s:
        if n==i:
            esta=True
    return esta
#2
def divide_a_todos(s:list[int],e:int)->bool:
    res:bool=True
    for i in s:
        if i%e!=0:
            res=False
    return res
#3
def suma_total(s:list[int])->int:
    a=0
    for i in s:
        a+=i
    return a    

#4 y 5
def maximo(s:list[int])->int:
    res:int=s[0]
    for i in s:
        if i>res:
            res=i
    return res

def minimo(s:list[int])->int:
    res:int=s[0]
    for i in s:
        if i<res:
            res=i
    return res
#6
def ordenados(s:list[int])->bool:
    res:bool=True
    for i in range(len(s)-1):
        if (s[i]>=s[i+1]):
            res=False
    return res

#7
def pos_maximo(s:list[int])->int:
    res:int
    if len(s)==0:
        res=-1
    else:
        res=s.index(maximo(s))
    return res


#8
def pos_minimo(s:list[int])->int:
    res:int
    if len(s)==0:
        res=-1
    else:
        res=s.index(minimo(s))
    return res
#9
def long_mayorASiete(lista:list[str])->bool:
    res:bool=False
    for palabra in lista:
        if (len(palabra)>7):
            res=True
    return res

#10
def es_palindroma(palabra:str)->bool:
    return(reverso(palabra)==palabra)

def reverso(palabra:str)->str:
    res=""
    for i in palabra:
        res=i + res
    return res
#11
def iguales_consecutivos(lista:list[int])->bool:
    res:bool=False
    if (len(lista)>=3):
        for i in range(len(lista)-2):
            if(lista[i]==lista[i+1]==lista[i+2]):
                res=True
    return res
#12
def vocales_distintas(palabra:str)->bool:
    vocales:list[str]=['a','e','i','o','u']
    contador:int=0
    for letra in palabra:
        if letra in vocales:
            contador+=1
            vocales.remove(letra)
    return(contador>=3)
#13
def pos_secuencia_ordenada_mas_larga(s:list[int])->int:
    contador_actual:int=0
    indice_sec_mas_larga:int=0
    k:int=0
    contador_final:int=0
    for i in range(len(s)-1):
        k=i
        while (k+1<len(s) and s[k]<=s[k+1]):
            k=k+1
            contador_actual+=1
        if contador_actual>contador_final:
            indice_sec_mas_larga=i
            contador_final=contador_actual
        contador_actual=0
    return indice_sec_mas_larga
#14
def cantidad_digitos_impares(s:list[int])->int:
    total_impares:int=0
    for numero in s:
        total_impares=digitosImpares(numero)+total_impares
    return total_impares
def digitosImpares(num:int)->int:
    res:int=0
    while(num>0):
        if num%10 in [1,3,5,7,9]:
            res+=1
        num=num//10
    return res

#Ejercicio 2 (modificas)

def CerosEnPosicionesPares(s:list[int]):
    for i in range(len(s)):
        if(i%2==0):
            s[i]=0

def CerosEnPosicionesPares2(s:list[int])->list[int]:
    res:list[int]=[]
    for i in range(len(s)):
        if(i%2==0):
            res.append(0)
        else:
            res.append(s[i])
    return(res)

def sin_vocales(s:str)->str:
    res:str=""
    for letra in s:
        if letra not in ['a','e','i','o','u']:
            res=res + letra
    return res

def remplaza_vocales(s:str)->str:
    res:str=""
    for letra in s:
        if letra in ['a','e','i','o','u']:
            res=res + "_"
        else:
            res=res+letra
    return res

def da_vuelta_str(s:str)->str:
    res:str=""
    for letra in s:
        res=letra + res
    return res

def elimina_repetidos(s:str)->str:
    res:str=""
    for letra in s:
        if letra not in res:
            res=res+letra
    return res

#Ejercicio 3
def resultado_materias(s:list[int])->int:
    res:int
    if(hayAlgunAplazo(s) or promedio(s)<4):
        res=3
    elif(not hayAlgunAplazo(s) and 4<=promedio(s)<7):
        res=2
    elif(not hayAlgunAplazo(s) and promedio(s)>=7):
        res=1
    return res


def promedio(s:list[int])->float:
    return(sum(s)/len(s))
def hayAlgunAplazo(s:list[int])->bool:
    res=False
    for nota in s:
        if(nota<4):
            res=True
    return(res)

#Ejercicio 4

def saldoActual(movimientos:list[tuple[str,int]])->int:
    saldo:int=0
    for trans in movimientos:
        if trans[0]=="I":
            saldo=saldo+trans[1]
        else:
            saldo=saldo-trans[1]
    return saldo

#Ejercicio 5
def pertenece_a_cada_uno1(s:list[list[int]],e:int,res:list[bool]):
    while len(res) < len(s):
        res.append(False)

    for i in range(len(s)):
        res[i] = e in s[i]


def pertenece_a_cada_uno2(s:list[list[int]],e:int,res:list[bool]):
    res=[]
    for fila in s:
        res.append(e in fila)

def pertenece_a_cada_uno3(s:list[list[int]],e:int)->list[bool]:
    res:list[bool]
    for fila in s:
        res.append(e in fila)
    return res

#La implementacion de 2 se puede usar para 1 pero la de 1 no para 2, por el largo de res

#Ejercicio 6:

def es_matriz(s:list[list[int]])->bool:
    res:bool=len(s)>0
    if res:
        res=res and len(s[0])>0
    if(res):
        for indice in range(len(s)-1):
            res=res and (len(s[indice])==len(s[indice+1]))
    return res

def filas_ordenadas(m:list[list[int]])->list[bool]:
    res:list[bool]=[]
    for fila in m:
        res.append(ordenados(fila))
    return res

def columna(m:list[list[int]],c:int)->list[int]:
    res:list[int]=[]
    for fila in m:
        res.append(fila[c])
    return res

def columnas_ordenadas(m:list[list[int]])->list[bool]:
    res:list[bool]=[]
    cantidad_columnas:int= len(m[0])
    for i in range(cantidad_columnas):
        res.append(ordenados(columna(m,i)))
    return res

def trasponer(m:list[list])->list[list]:
    res:list[list[int]]=[]
    cantidad_columnas:int= len(m[0])
    for i in range(cantidad_columnas):
        res.append(columna(m,i))
    return res

def tateti(tab:list[list[str]])->int:
    res:int
    if(ganoEnFilas("x",tab) or ganoEnColumnas("x",tab) or ganoEnDiagonal("x",tab)):
        res=1
    elif(ganoEnFilas("o",tab) or ganoEnColumnas("o",tab) or ganoEnDiagonal("o",tab)):
        res=0
    else:
        res=2
    return res

def ganoEnFilas(jugador:str,tablero:list[list[str]])->bool:
    res:bool=False
    for fila in tablero:
        if fila==[jugador,jugador,jugador]:
            res=True
    return res
def ganoEnColumnas(jugador:str,tablero:list[list[str]])->bool:
    return(ganoEnFilas(jugador,trasponer(tablero)))

def ganoEnDiagonal(jugador:str,tablero:list[list[str]])->bool:
    return(jugador==tablero[0][0]==tablero[1][1]==tablero[2][2] or jugador==tablero[2][0]==tablero[1][1]==tablero[0][2])