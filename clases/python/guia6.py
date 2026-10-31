import math
def imprimir_hola_mundo ():
    print("¡Hola mundo!")

#imprimir_hola_mundo()

def imprimir_un_verso():
    print("El mundo no se va a parar porque tú te sientas así \n A veces caminamos como si dos manos por los lados\n De la cara taparan lo que tienes al lado")

#imprimir_un_verso()

def raizDe2():
    print(round(2**(0.5),4))
#raizDe2()

def factorial_de_dos()->int:
    return(2)
#print(factorial_de_dos())

def perimetro()->float:
    return(2*math.pi)
#print(perimetro())

#Ejercicio 2
def imprimir_saludo (nombre: str):
    print("Hola",nombre)

#imprimir_saludo("damian")
def raiz_cuadrada_de(numero:int)->int:
    return(round(numero**(1/2),4))
#print(raiz_cuadrada_de(3))

def fahrenheit_a_celsius(t:float)->float:
    return ((t-32)*5/9)
#print(fahrenheit_a_celsius(0))
def imprimir_dos_veces(estribillo):
    print(2*estribillo)
#imprimir_dos_veces("Vienilla y milu \n Estan Gorditas\n")

def es_multiplo_de (n:int, m:int)->bool:
    return (m%n==0)
#print(es_multiplo_de(2,4))
#print(es_multiplo_de(2,5))

def es_par(numero)->bool:
    return (es_multiplo_de(numero,2))
#print(es_par(2))
#print(es_par(3))

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int)->int:
    total_comidas:int=comensales*min_cant_de_porciones
    if es_multiplo_de(8,total_comidas):
        pizzas_necesarias:int=total_comidas//8
    else:
        pizzas_necesarias:int=total_comidas//8+1
    return(pizzas_necesarias)
#print(cantidad_de_pizzas(3,8))
#print(cantidad_de_pizzas(1,9))

#Ejercicio 3

def alguno_es_0(a:float,b:float)->bool:
    return(a==0 or b==0)
# print(alguno_es_0(0,1))
# print(alguno_es_0(1,0))
# print(alguno_es_0(1,1))
# print(alguno_es_0(0,0))
def ambos_es_0(a:float,b:float)->bool:
    return(a==0 and b==0)

def es_nombre_largo(nombre:str)->bool:
    return(3<=len(nombre)<=8)

def es_bisiesto(anio:int)->bool:
    return(anio%400==0 or (anio%4==0 and anio%100!=0))

#Ejercicio 4
#usar min y max
def peso_pino(altura:int)->int:
    peso=0
    if (altura > 300):
        peso=300*3+(altura-300)*2
    else:
        peso=altura*3
    return(peso)
def es_peso_util(peso:int)->bool:
    es_util=False
    if (400<=peso and peso<=1000):
        es_util=True
    return (es_util)
def sirve_pino(pino:int)->bool:
    return(es_peso_util(peso_pino(pino)))

#Ejercicio 5
def doble_si_es_par(n: int)-> int:
    res=n
    if (n%2==0):
        res=2*n
    return res

def devolver_valor_si_es_par_si_no_el_que_sigue(n:int)->int:
    if(n%2!=0):
        n=n+1
    return n

def doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int:
    if (numero%9==0):
        numero=3*numero
    elif (numero%3==0):
        numero=2*numero
    return(numero)
def lindo_nombre(nombre:str):
    if (len(nombre)>=5):
        print("Tu nombre tiene muchas letras")
    else:
        print("u nombre tiene menos de 5 caractere")

def elRango(numero:int):
    if(numero<5):
        print("Menor a 5")
    elif(10<=numero<=20):
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")

def vacaciones(sexo:str,edad:int):
    if (edad<18 or ((sexo=='F' and edad>=60) or (sexo=='M' and edad>=65))):
        print("vacaciones")
    else:
        print("laburar")

#Ejercicio 7 (igual al 6 con for num in range(i,f,p))
def imprimir_1_al_10():
    for i in range (1,11,1):
        print(i)
#imprimir_1_al_10()
def pares_10_al_40():
    for i in range(10,41,2):
        print(i)
# pares_10_al_40()
def eco_10():
    for i in range(10):
        print("eco")
# eco_10()
def conteo_regresivo(num:int):
    for i in range(num,0,-1):
        print(i)
    print("Despegue")
# conteo_regresivo(7)
def viaje_en_el_tiempo(pasado:int,presente:int):
    for i in range(presente,pasado-1,-1):
        print("Viajó un año al pasado, estamos en el año: ",i)
# viaje_en_el_tiempo(2012,2020)
def conocer_aristoteles(anio_actual:int):
    for i in range (anio_actual,-385,-20):
        print("Viajó 20 años al pasado, estamos en el año: ",i)

# conocer_aristoteles(-304)
#Ejercicio 6   (while)
def imprimir_1_al_102():
    a=1
    while (a<=10):
        print(a)
        a+=1
#imprimir_1_al_102()
def pares_10_al_402():
    a=10
    while(a<=40):
        print(a)
        a+=2
# pares_10_al_402()
def eco_102():
    c=0
    while (c<10):
        print("eco")
        c+=1
# eco_10()
def conteo_regresivo2(num:int):
    while(num>=1):
        print(num)
        num-=1
    print("Despegue")
# conteo_regresivo2(7)
def viaje_en_el_tiempo2(pasado:int,presente:int):
    while(pasado<=presente):
        print("Viajó un año al pasado, estamos en el año: ",presente)
        presente-=1
# viaje_en_el_tiempo(2012,2020)
def conocer_aristoteles2(anio_actual:int):
    while(-384<=anio_actual):
        print("Viajó 20 años al pasado, estamos en el año: ",anio_actual)
        anio_actual-=20
# conocer_aristoteles2(12)

# Ejercicio 8
# 1. x=5 ; y=7; x = x + y, entonces x=5+7=12
# 2. x=5 ; y=7 ; z=x+y; y = z * 2 entonces z=12,y=12*2=24
# 3. x=5 ; y=7 ; x="hora"; y = x * 2 entonces y="horahora"
# # 4. x=False ; res=not(x) entonces res=True
# 5. x=False ; x=not(x) entonces x=True
#6. x=True ; y=False ; res=x and y; x = res and x entonces 1ro res=false and false=false, despues, x=false and false=false

# Ejercicio 9
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g
g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g


# 1. Cuál es el resultado de evaluar tres veces seguidas ro(1)?
# print(ro(1))#g pasa a valer 1 entonces ro printea 1+g=2
# print(ro(1))#g pasa a valer 2 entonces ro printea 3
# print(ro(1))#g pasa a valer 3 entonces ro printea 4
# 2. Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# print(rt(1,0))#devuelve 2
# print(rt(1,0))#devuelve 2
# print(rt(1,0))#devuelve 2
# 3. En cada función, realizar la ejecución simbólica.
#visto debuggeando
# 4. Dar la especificación para cada función, rt y ro
# problema ro(in x:Z):Z{
#     requiere{-}
#     modifica{g}
#     asegura{res=x+g}
# }
# problema rt(in x:Z,in y:Z):Z{
#     requiere{-}
#     asegura{res=x+g}
# }