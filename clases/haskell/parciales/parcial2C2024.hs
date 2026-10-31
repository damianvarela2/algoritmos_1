
-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }
mediaMovilN :: [Integer] ->Integer->Float
mediaMovilN [] _=0.0
mediaMovilN (xs) n= fromInteger (sumaPrimerosN (reverso xs) n)/fromInteger n

reverso :: [Integer]->[Integer]
reverso []=[]
reverso (x:xs)= reverso xs ++ [x]

sumaPrimerosN :: [Integer]-> Integer-> Integer
sumaPrimerosN _ 0=0
sumaPrimerosN [] _=0
sumaPrimerosN (x:xs) n = x+ sumaPrimerosN xs (n-1)





-- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 
esAtractivo::Integer->Bool
esAtractivo 1=False
esAtractivo n= esPrimo (cantidadElementos (factorizacionPrima n))

cantidadElementos ::[Integer]->Integer
cantidadElementos []=0
cantidadElementos (x:xs)=1+cantidadElementos xs

factorizacionPrima::Integer->[Integer]
factorizacionPrima n|esPrimo n=[n]
                    |otherwise=factorizacionPrimaAux n 2
factorizacionPrimaAux:: Integer->Integer->[Integer]
factorizacionPrimaAux n d|d>n=[]
                         |mod n d ==0= d: factorizacionPrimaAux (div n d) d
                         |otherwise= factorizacionPrimaAux n (siguientePrimo d)
siguientePrimo ::Integer->Integer
siguientePrimo n|esPrimo(n+1)=n+1
                |otherwise=siguientePrimo (n+1)
esPrimo::Integer->Bool
esPrimo 1=False
esPrimo n=esPrimoAux n 2

esPrimoAux:: Integer->Integer->Bool
esPrimoAux n m|n==m=True
              |mod n m ==0=False
              |otherwise=esPrimoAux n (m+1)

-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. 
palabraOrdenada:: String ->Bool
palabraOrdenada p = palabraOrdenadaAux (sinBlancos p)

palabraOrdenadaAux :: String ->Bool
palabraOrdenadaAux []=True
palabraOrdenadaAux [x]=True
palabraOrdenadaAux (x:y:xs)|x<=y=palabraOrdenadaAux (y:xs)
                           |otherwise=False

sinBlancos :: String -> String
sinBlancos []=[]
sinBlancos (x:xs)|x== ' '=sinBlancos xs
                 |otherwise= x:(sinBlancos xs)


-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }
similAnagrama::String->String->Bool
similAnagrama a b = similAnagramaAux (sinBlancos a) (sinBlancos b)

similAnagramaAux::String->String->Bool
similAnagramaAux a b| a/=b && esPermutacion a b=True
                    |otherwise=False

esPermutacion :: String ->String->Bool
esPermutacion [] []=True
--esPermutacion _ []=False
--esPermutacion [] _=False
esPermutacion (x:xs) (y:ys)|pertenece x (y:ys) && pertenece y (x:xs)=esPermutacion (quitar x (x:xs)) (quitar y (y:xs))
                           |otherwise=False

quitar :: Char -> String -> String
quitar _ []=[]
quitar x (p:palabra)|x==p=palabra
                    |otherwise=p:quitar x palabra
pertenece:: Char ->String ->Bool
pertenece _ []=False
pertenece x (p:palabra)|x==p=True
                       |otherwise=pertenece x palabra
