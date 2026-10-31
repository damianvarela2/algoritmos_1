doubleMe :: Integer -> Integer
doubleMe x = 2 * x
--guia 3
--Ejercicio 1a, 1b y 1c
f :: Integer -> Integer--pattern matching
f 1=8
f 4=131
f 16=16

g :: Integer -> Integer--divido por casos en guardas
g n | (n == 8) = 16
    | (n == 16) = 4
    | (n == 131) = 1

h :: Integer -> Integer -- f o g(x)= f(g(x)), h(1)=
h x | (x == 8) = f (g x)
    | (x == 131) = f (g x)
    | (x == 16) = f (g x)

k :: Integer -> Integer --g o f(x)=g(f(X))=>g o f(4)=1
k x | (x == 1) = g (f x)
    | (x == 4) = g (f x)
    | (x == 16) = g (f x)

--Ejercicio 2
--2a
--problema absoluto (x:Z) : Z {
--    requiere{True}
--    asegura{si x es 0, res=0}
--    asegura{si x es mayor a 0, res=x}
--    asegura{si x es menor a 0, res=-x}
--}
absoluto :: Integer -> Integer
absoluto x|(x<0) = -x
        |(x>=0) = x

--2b
--problema maximoAbsoluto(x,y:Z) : Z{
--requiere{True}
--
--asegura{res= absoluto(x) o res=absoluto(y)}}

--2c
--problema maximo3(x,y,z: Z) : Z {
--requiere{True}
--asegura{res es igual a x, o a y o a z}
--asegura{res es mayor igual a x, y a y y a z}}

maximo3 :: Integer -> Integer -> Integer -> Integer--(&&=and y ||=or)
maximo3 x y z| ((x>=y) && (x>=z)) = x
            |((y>=x) && (y>=z)) = y
            |((z>=y) && (z>=x)) = z

maximo4 :: Integer -> Integer -> Integer -> Integer
maximo4 x y z| ((x>=y) && (x>=z)) = x
            |((y>=z)) = y
            |(otherwise) = z

--2d
--problema algunoEsCero(x,y:R):Bool{
--requiere{-}
--asegura{Res es true si x o y es 0, y false sino}
--}
algunoEsCero :: Float -> Float -> Bool
algunoEsCero 0 y = True
algunoEsCero x 0 = True
algunoEsCero x y = False

algunoEsCero2 :: Float -> Float -> Bool
algunoEsCero2 x y | (x==0)=True
                 | (y==0)=True
                 | otherwise=False

--2e
--problema ambos0(x,y:R):Bool{
--requiere{-}
--asegura{Res es true si x y y es 0, y false sino}
--}
ambos0 :: Float -> Float -> Bool
ambos0 0 0 = True
ambos0 x y = False

ambosCero :: Float -> Float -> Bool
ambosCero x y | ((x==0) && (y==0))=True
                 | otherwise=False

--2f
--problema enMismoIntervalo(x,y R): Bool{
--requiere{-}
--asegura{Res es true si x e y pertenecen al mismo intervalo de  (−∞, 3], (3, 7] y (7, ∞),}
--}
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y| ((x<=3)&&(y<=3))=True
                    | ((x<=7)&&(y<=7))=True
                    | ((x>7)&&(y>7))=True
                    | otherwise = False


--2h
--problema esMultiploDe (x, y:N):Bool{
--requiere{-}
--asegura{res es true si x es multiplo de y, sino false}
--}
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y| mod x y == 0 =True
                | otherwise = False


--2g
--problema sumaDistintos(x,y,z:Z):Z{
--requiere{-}
--asegura{si los 3 parametros son distintos res=x+y+z}
--asegura{si 2 parametros son iguales res es igual al no repetido}
--asegura{si los 3 parametros son iguales res=0}}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z|(x == y)&&(x == z) = 0
                   |(x==y) = z
                   | (x==z) = y
                   | (z==y) = x
                   | (otherwise) = z+y+x


--MOD y DIV operaciones de haskell
--mod 5434 10 = 4 (resto)
--div 5434 10 = 543 (division entera)

--2i
--problema digitoUnidades(x:Z):Z{
--requiere{True}
--asegura{res es el digito correspondiente a las unidades}}

digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (absoluto x) 10
--si le paso un numero negativo explota, entonces le pongo absoluto para que salve las papas

--2j
--problema digitoDecenas(x:Z):Z{
--requiere{True}
--asegura{res es el digito correspondiente a las decenas}}
digitoDecena :: Integer -> Integer
digitoDecena x = div (mod (absoluto x) 100) 10
--podria haber restado digitoUnidades
--podria haber hecho div x 10 y despues sacar el 1er digito

--3
estanRelacionados :: Int -> Int -> Bool
--estan relacionados sii x²+xyk=0, sacando factor comun x(x+yk)=0,como x!=0 x+yk=0, 
--entonces x=-yk, es decir, x e y se relacionan si x es multiplo de -y
estanRelacionados x y| (esMultiploDe x (-y)==True)=True
                     |otherwise = False





{-ESPECIFICACIÓNES 4
a- 
problema productoInterno ((a,b) (c,d):RxR):R{
requiere{}
asegura{res es el producto interno de los vectores ingresados}}-}
type Punto2D = (Float, Float)
productoInterno :: Punto2D -> Punto2D->Float
productoInterno (a,b) (c,d) = a*c + b*d
{-
b
problema esParMenor ((a,b) (c,d):RxR)):Bool{
requiere{}
asegura{res es true si cada coordenada de (a,b) es menor a la coordenada
correspondiente de (c,d)}}-}
esParMenor :: Punto2D -> Punto2D->Bool
esParMenor (a,b) (c,d)|((a<=c)&&(b<=d))==True=True
                      | otherwise=False
{-
c
problema distancia((a,b) (c,d):RxR)):R{
requiere{}
asegura{res es la distancia entre ambos puntos}}-}
distancia :: Punto2D -> Punto2D->Float
distancia (a,b) (c,d)=sqrt((c-a)**2+(d-b)**2)
{-
d
problema sumaTerna((a,b,c):RxRxR):R{
requiere{}
asegura{res es la suma de los 3 elementos del vector}}-}
sumaTerna :: (Float,Float,Float)->Float
sumaTerna (x,y,z)=x+y+z
{-
e
problema sumarSoloMultiplos ((x,y,z):Z n:N):Z{
requiere{}
asegura{res es la suma de (x,y,z) que son multiplos de n}}-}
sumarSoloMultiplos :: (Int,Int,Int)->Int->Int
sumarSoloMultiplos (x1,x2,x3) n=sumamult x1 n + sumamult x2 n + sumamult x3 n

sumamult :: Int->Int->Int
sumamult x n | esMultiploDe x n==True= x
             | otherwise =0    
{-
f
problema posPrimerPar ((x,y,z):Z):Z{
requiere{}
asegura{res es la posicion del primer numero par de la terna, sino hay par es 4}}-}
posPrimerPar :: (Int,Int,Int)->Int
posPrimerPar (x,y,z)|mod x 2==0=1
                    |mod y 2==0=2
                    |mod z 2==0=3
                    |otherwise=4

{-
g/preguntar como se nota que una variable no tiene tipo definido
problema crearPar (a:x b:y):(a,b){
requiere{}
asegura{res es el par ordenado (a,b)}}-}
crearPar :: a -> b -> (a, b)
crearPar x y=(x,y)

{-
h
problema invertir ((a,b)):(b,a){
requiere{}
asegura{res es el par dado vuelta}}
-}
invertir :: (a,b)->(b,a)
invertir (x,y)=(y,x)



--Ejercicio 5
{-
problema todosMenores (t : Z × Z × Z) : Bool {
requiere: {T rue}
asegura: {(res = true) ↔ ((f (t0) > g(t0)) ∧ (f (t1) > g(t1)) ∧ (f (t2) > g(t2)))}
}
problema f (n : Z) : Z {
requiere: {T rue}
asegura: {(n ≤ 7 → res = n2) ∧ (n > 7 → res = 2n − 1)}
}
problema g (n : Z) : Z {
requiere: {T rue}
asegura: {Si n es un n´umero par entonces res = n/2, en caso contrario, res = 3n + 1}
}-}
todosMenores :: (Int,Int,Int)->Bool
todosMenores (x,y,z)| (f1 x > g1 x)&&(f1 y > g1 y)&&(f1 z > g1 z)=True
                    | otherwise=False

f1 :: Int->Int
f1 n|(n<=7)= n*n
    |otherwise= 2*n-1

g1 :: Int->Int
g1 n|mod n 2==0=div n 2
    |otherwise= 3*n+1


--Ejercicio 6
{-problema bisiesto (anio : Z) : Bool {
requiere: {T rue}
asegura: {(res = f alse) ↔ (a˜no no es m´ultiplo de 4, o bien, a˜no es m´ultiplo de 100 pero no de 400)}
}-}
type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto n|(mod n 4 ==0)||(mod n 100==0)&&(not(mod n 400==0))=True
          |otherwise=False

--Ejercicio 7
{-
problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
requiere: {T rue}
asegura: {res = sumatoria (2, i=0) |pi − qi|}-}

distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float