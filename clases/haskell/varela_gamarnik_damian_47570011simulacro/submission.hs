module SolucionT1 where

-- Ejercicio 1
f1 :: Integer -> Integer -> Integer
f1 x h|(x==h) && esAbundante h=1
      |(x==h) && not (esAbundante h)=0
f1 d h | esAbundante d= 1+ f1 (d+1) h
       |otherwise= f1 (d+1) h

esAbundante :: Integer -> Bool
esAbundante n|sumarDivisoresDeUnEnteroAux n (n-1)>n=True
             |otherwise=False

sumarDivisoresDeUnEnteroAux :: Integer -> Integer ->Integer
sumarDivisoresDeUnEnteroAux _ 0=0
sumarDivisoresDeUnEnteroAux _ 1=1
sumarDivisoresDeUnEnteroAux n d| esDivisor n d=d+sumarDivisoresDeUnEnteroAux n (d-1)
                               |otherwise= sumarDivisoresDeUnEnteroAux n (d-1)

esDivisor ::  Integer->Integer->Bool
esDivisor _ 1=True
esDivisor n d|mod n d ==0=True
             |otherwise=False

--hacer una funcion que vaya sumando todos los divisores de un numero
--en la funcion f1 quiero hacer una recursion hasta que llegue al numero y c/u que devuelva true sumo 1
--


-- Ejercicio 2
f2 :: [(String, Integer, Integer)] -> [String]
f2 [] = []
f2 (x:xs)=eliminarMateriasRepetidas(listaDeVigentes (x:xs))

--tengo que sacar todas las materias con año <= 2021
--debo devolver el nombre de las materias
primero :: (String, Integer, Integer) -> String
primero (palabra,num,numero)=palabra

segundo :: (String, Integer, Integer) -> Integer
segundo (palabra,num,numero)=num

tercero :: (String, Integer, Integer) -> Integer
tercero (palabra,num,numero)=numero

esVigente :: (String, Integer, Integer)-> Bool
esVigente (materia,año,cuatri)|año>=2021=True
                              |otherwise=False

listaDeVigentes :: [(String, Integer, Integer)]-> [String]
listaDeVigentes []=[]
listaDeVigentes (x:xs)|not (esVigente x)= (primero x):(listaDeVigentes (xs))
                      |otherwise=listaDeVigentes (xs)

pertenece :: String -> [String]-> Bool
pertenece _ []=False
pertenece palabra (x:xs)|x==palabra=True
                        |otherwise=pertenece palabra (xs)
quitar :: String -> [String]-> [String]
quitar _ []=[]
quitar p (x:xs)| p==x=xs
               |otherwise= x:(quitar p (xs))
quitarTodas :: String -> [String]-> [String]
quitarTodas _ []=[]
quitarTodas palabra (xs)| pertenece palabra xs =quitarTodas palabra (quitar palabra xs)
                        |otherwise=xs

eliminarMateriasRepetidas :: [String]->[String]
eliminarMateriasRepetidas []=[]
eliminarMateriasRepetidas (x:xs)| pertenece x xs= x:(eliminarMateriasRepetidas (quitarTodas x xs))
                                |otherwise= x:(eliminarMateriasRepetidas xs)

-- Ejercicio 3
f3 :: [Integer] -> Integer -> [Integer]
f3 [] _=[]
f3 xs u=f3aux (cortarAlPrimerNegativo xs) u
f3aux :: [Integer] -> Integer -> [Integer]
f3aux [] _ = []
f3aux (x:xs) u| x >= u = u:f3 (xs) u
           |otherwise= x:f3 (xs) u

{-cantidadDeNoNegativosDesdeElComienzo :: [Integer] -> Integer
cantidadDeNoNegativosDesdeElComienzo []=0
cantidadDeNoNegativosDesdeElComienzo (x:xs)| x>=0= 1+ cantidadDeNoNegativosDesdeElComienzo xs
                                           |otherwise=0
--si es mayor a u pongo u(u es mi techo), si es menor dejo el numero
-}
cortarAlPrimerNegativo ::[Integer]->[Integer]
cortarAlPrimerNegativo []=[]
cortarAlPrimerNegativo [x]|x>=0=[x]
                          |otherwise=[]
cortarAlPrimerNegativo (x:y:xs)| y>=0=x:cortarAlPrimerNegativo (y:xs)
                             |otherwise= [x]


-- Ejercicio 4
f4 :: [[Integer]] -> Integer -> Integer
f4 [] _ = 1 --Impar entonces no lo cuento, puedo pq se que la matriz no va a ser vacia
f4 (x:xs) n = cantidadDePares ((f4aux (x:xs) n):[(f4 xs n)])

f4aux :: [[Integer]] -> Integer -> Integer
f4aux (x:xs) n= nesimoElemento n x

nesimoElemento:: Integer->[Integer]->Integer
nesimoElemento _ [a]=a
nesimoElemento n (x:xs)=nesimoElementoDesde n 1 (x:xs)

nesimoElementoDesde :: Integer->Integer->[Integer]->Integer
nesimoElementoDesde _ _ [x]=x
nesimoElementoDesde n a (z:xs)|a/=n=nesimoElementoDesde n (a+1) (xs)
                              |a==n=z
cantidadDePares :: [Integer] -> Integer
cantidadDePares []=0
cantidadDePares (x:xs)| mod x 2==0=1+ cantidadDePares xs
                      |otherwise= cantidadDePares xs