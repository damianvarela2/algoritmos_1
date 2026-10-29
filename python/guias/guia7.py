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




