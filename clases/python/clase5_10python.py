def triada_pitagorica (a:int, b:int, c:int)->bool:
    return (a**2 + b**2==c*2)
#esta mal esto elñ c*2, faltaria otro *, vamos a probar que esta mal con los test


def es_multiplo_de_n(n:int,m:int)->bool:
    if (m%n ==0):
        return True
    else:
        return False#en esta materia no usaremos multiples returns, se puede guardar en una variable o (return n%m)


def doble_si_es_par(n: int)-> int:
    if (n%2==0):
        return (2*n)
    else:
        return n


def fahrenheit_a_celsius(t:float)->float:
    return ((t-32)*5/9)
#parea ejecuitar hago, python3 -> importo el archivo (sin .py)-> nombre_archivo.nombre_funcicon(parametros)
#para correr todo el archivo (python3 tests.py)

def es_primo (n:int)->bool:
    contador:int=0
    for i in range (1,n+1,1):
        if (n%i==0 and n>0):
            contador+=1
    return contador==2

def cantidad_de_primos_en_rango(n:int,m:int)->int:
    if (n>m):
        n, m=m, n
    contador:int=0
    for i in range (n, m+1,1):
        if (es_primo (i)):
            contador+=1
    return contador

print (cantidad_de_primos_en_rango (2,7))

#debuggear, metemos un breakpint en alguna linea interesante
#hay varios "comandos" de breakponts, hay uno que es continuar hasta el siguiente bp (F5), f10 SALTEA EL PASO QUE EVALUA LA FUNCION EN ESA LINEA, f11 iingresa a la funcion que se evalua en la linea
#tengo que hacer los llamados a la funcion para debuggear
#sirve para ver el desarrollo del programa en tiempo real, para ver loss errores es top.