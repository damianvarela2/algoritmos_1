def suma_total (s: list[int])->int:
    a:int=0
    for i in s:
        a+=i
    return a

#for esta bueno pq automatiza el recorrido, toma todos los valores de una seq hasta agotarla 

def pertenece (s: list[int], e:int)->bool:
    result:bool=False
    for i in s:
        if i==e:
            result=True
        else:
            pass
    return result


#los procedimientos no necesariamente devuelven algo, en cambio, las funciones si
#pythontutor, pagina donde le doy el codigo y me va diciendo lo que esta pasando en la memoria y las variables etc etc... es como debuggear

#while permite cortar antes, te da el control, en pertenece convenia hacerlo con while para mas eficiencia.
l:list[int]=[2,3,4,5,6,7]
def cerosEnPosicionesPares (s:list[int])->None:
    for i in range(len (s)):#podria haber hecho que el paso sea de a 2 y me ahorraba el if
        if i%2==0:
            s[i]=0
#print(l)   
#cerosEnPosicionesPares(l)
#print(l)

def cerosEnPosicionesPares2 (s:list[int])->list[int]:
    res:list[int]=[]
    for i in range(len (s)):
        if i%2==0:
            res.append(0)
        else:
            res.append(s[i])
    return res

#print(cerosEnPosicionesPares2([1,2,3,4,5,5,3,6,67]))
#ctrl+k+c comenta y ctrl+k+u descomenta

#si hago lista1=lista2 y cambio lista1 se cambia lista2, entonces se usa lista1=lista2.copy

#map, es parar aplicar una transformacion a toda una lista, patron gral, 1. crear una secuencia de res del mismo largo 2. recorrer la sec original y 3. guardar en res la transformacion de sec original.

def UnirPalabras (ps:list[str])->str:
    res=""
    for p in range (len (ps)-1):
        res+=ps[p]+ " "
    return res+ ps[len(ps)-1]

print(UnirPalabras(["hola","aa","ddd"]))
