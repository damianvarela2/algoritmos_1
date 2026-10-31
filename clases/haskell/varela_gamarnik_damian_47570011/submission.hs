module SolucionT1 where

-- Ejercicio 1
{-
pense que era sacar todos los pares, esto es para ello
ejercicio1 :: [Integer] -> Integer -> [Integer]
ejercicio1 [] _ = []
ejercicio1 [x] _=[x]
ejercicio1 (x:y:xs) n| sumanN x y n =quitarPrimer y (ejercicio1 (y:xs) n)
                     |otherwise=x:(ejercicio1 (y:xs) n)
-}
ejercicio1 :: [Integer] -> Integer -> [Integer]
ejercicio1 [] _ = []
ejercicio1 [x] _=[x]
ejercicio1 (x:y:xs) n| sumanN x y n =xs
                     |otherwise=x:(ejercicio1 (y:xs) n)

sumanN :: Integer->Integer->Integer->Bool
sumanN x y n| x+y==n=True
            |otherwise=False

quitarPrimer :: Integer -> [Integer]->[Integer]
quitarPrimer _ []=[]
quitarPrimer q (x:xs)|q==x=xs
                     |otherwise=x:quitarPrimer q xs


-- Ejercicio 4
cantidadDeRefactorizables :: Integer -> Integer -> Integer
cantidadDeRefactorizables d h=longitud (reFactorizablesEntre d h)

reFactorizablesEntre:: Integer->Integer->[Integer]
reFactorizablesEntre d h| d>h=[]
                        |esReFactorizable d =d:reFactorizablesEntre (d+1) h
                        |otherwise=reFactorizablesEntre (d+1) h

esReFactorizable :: Integer->Bool
esReFactorizable n| esDivisor n (cantidadDivisoresN n)=True
                  |otherwise=False

cantidadDivisoresN:: Integer->Integer
cantidadDivisoresN n= longitud (cantidadDivisoresPropios n)

longitud :: [Integer]->Integer
longitud []=0
longitud (x:xs)=1+ longitud xs

cantidadDivisoresPropios :: Integer -> [Integer]
cantidadDivisoresPropios 1 = [1]
cantidadDivisoresPropios n=cantidadDivisoresAux n 1

cantidadDivisoresAux:: Integer->Integer->[Integer]
cantidadDivisoresAux x d| x<d=[]
cantidadDivisoresAux x d| esDivisor x d=d:cantidadDivisoresAux x (d+1)
                        |otherwise= cantidadDivisoresAux x (d+1)

esDivisor :: Integer->Integer->Bool
esDivisor x d|mod x d ==0=True
             |otherwise=False





-- Ejercicio 5
sociosConComprasAltas :: [(String, Integer, Bool)] -> Integer -> [String]
sociosConComprasAltas [] _ = []
sociosConComprasAltas (xs) u=sacarRepetidos (sociosConComprasAltasAux xs u)

--sociosConComprasAltas [("a",21,True),("b",0,True),("c",2,True),("a",211,True),("d",221,True)] 20
sociosConComprasAltasAux :: [(String, Integer, Bool)] -> Integer -> [String]
sociosConComprasAltasAux [] _ = []
sociosConComprasAltasAux ((x,y,z):xs) u|esBuenComprador (x,y,z) u=(x:sociosConComprasAltasAux xs u)
                                    |otherwise=sociosConComprasAltasAux xs u

esBuenComprador :: (String,Integer,Bool)->Integer->Bool
esBuenComprador (x,y,z) u|pasaUmbral (x,y,z) u && esSocio (x,y,z)=True
                         |otherwise=False

pasaUmbral :: (String,Integer,Bool)->Integer->Bool
pasaUmbral (x,y,z) u| y>u=True
                    |otherwise=False

esSocio :: (String,Integer,Bool)->Bool
esSocio (x,y,z)|z==True=True
               |otherwise=False

quitarPrimerS:: String->[String]->[String]
quitarPrimerS _ []=[]
quitarPrimerS q (x:xs)|q==x=xs
                      |otherwise=(x:(quitarPrimerS q xs))

sacarRepetidos:: [String]->[String]
sacarRepetidos []=[]
sacarRepetidos (x:xs)|pertenece x xs=sacarRepetidos (x:quitarPrimerS x xs)
                     |otherwise = (x:(sacarRepetidos xs))

pertenece::String->[String]->Bool
pertenece _ []=False
pertenece palabra (x:xs)|palabra==x=True
                        |otherwise=pertenece palabra xs

-- Ejercicio 6
ejercicio6 :: [[Integer]] -> [[Integer]]
ejercicio6 [] = []
ejercicio6 (x:xs)=ejercicio6Aux (x:xs) 1 (longitud x)

ejercicio6Aux :: [[Integer]]->Integer->Integer->[[Integer]]
ejercicio6Aux (x:xs) d l|d==l=[cambiarNElemento l (x)]
                        |d<=l=(cambiarNElemento d x):(ejercicio6Aux xs (d+1) l)
                        |otherwise=[]

--ejercicio6 [[1]]
--ejercicio6 [[1,2],[3,4]]
--ejercicio6 [[1,2,3,20],[4,5,6,30],[7,8,9,40],[10,11,12,13]]
--ejercicio6 [[1,0,0],[0,1,0],[0,0,1]]
--ejercicio6 [[1,0,0],[0,0,0],[0,0,0]]


esParteDeDiagonal::(Integer,Integer) ->Bool
esParteDeDiagonal (f,c)|f==c=True
                     |otherwise=False

 

cambiarNElemento :: Integer->[Integer]->[Integer]
cambiarNElemento _ []=[]
cambiarNElemento n (x:xs)|n==1= 0:(xs)
                         |otherwise= x:(cambiarNElemento (n-1) xs)