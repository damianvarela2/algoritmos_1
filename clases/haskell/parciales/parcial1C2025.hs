--tema a
--Ejercicio 1
hayPrimosGemelos :: Integer->Integer->Bool
hayPrimosGemelos x y|x==y=False
                    |ambosPrimos x y && gemelos x y=True
                    |otherwise= hayPrimosGemelos (x+1) y


esPrimo :: Integer -> Bool
esPrimo 1=False
esPrimo x=esPrimoaux x 2

esPrimoaux :: Integer-> Integer->Bool
esPrimoaux x y|x==y=True
              |mod x y==0=False
              |otherwise=esPrimoaux x (y+1)

ambosPrimos :: Integer->Integer->Bool
ambosPrimos n m| esPrimo n && esPrimo m=True
               |otherwise=False

absoluto :: Integer->Integer
absoluto x|x>=0=x
          |otherwise=(-x)

gemelos :: Integer ->Integer->Bool
gemelos x y| absoluto (x-y)==2=True
           |otherwise=False

--Ejercicio 2

materiasTurnoTarde :: [(String,String,Integer,Integer)]->[String]
materiasTurnoTarde []=[]
materiasTurnoTarde ((materia,dia,empieza,termina):xs)|seCursaEnLaTarde (materia,dia,empieza,termina)= materia: materiasTurnoTarde xs
                                                     |otherwise=materiasTurnoTarde xs

seCursaEnLaTarde :: (String,String,Integer,Integer)->Bool
seCursaEnLaTarde (materia,dia,empieza,termina)| seChocanlosIntervalos empieza termina 14 17 = True
                                              |otherwise=False

seChocanlosIntervalos :: Integer -> Integer ->Integer->Integer ->Bool
seChocanlosIntervalos x y a b|pertenece x (intervalo a b)=True
                       |x==y=False
                       |otherwise= seChocanlosIntervalos (x+1) y a b

intervalo:: Integer -> Integer ->[Integer]
intervalo x y|x==y=[]
             |otherwise= x: intervalo (x+1) y

pertenece :: Integer-> [Integer]->Bool
pertenece _ []=False
pertenece n (x:xs)|n==x=True
                  |otherwise= pertenece n xs

--Ejercicio 3

maximaSumaDeTresConsecutivos :: [Integer]->Integer
maximaSumaDeTresConsecutivos [x,y,z]=sumaPrimeros3 [x,y,z]
maximaSumaDeTresConsecutivos (x:y:z:xs)= maximaSumaDeTresConsecutivosAux (sumaPrimeros3 (x:y:z:xs)) (y:z:xs)

sumaPrimeros3 :: [Integer]->Integer
sumaPrimeros3 []=0
sumaPrimeros3 [x,y,z]=x+y+z
sumaPrimeros3 (x:y:z:xs)= x +y+ z

maximaSumaDeTresConsecutivosAux :: Integer->[Integer]->Integer
maximaSumaDeTresConsecutivosAux a [x,y,z]|a>= (x+y+z)=a
                                         |otherwise=x+y+z
maximaSumaDeTresConsecutivosAux max xs| max >= sumaPrimeros3 xs =maximaSumaDeTresConsecutivosAux (max) (eliminarPrimero xs)
                                      |otherwise= maximaSumaDeTresConsecutivosAux (sumaPrimeros3 xs) (eliminarPrimero xs)

eliminarPrimero :: [Integer]->[Integer]
eliminarPrimero []=[]
eliminarPrimero (x:xs)=xs

--Ejercicio 4
sumaIesimaColumna::[[Integer]]->Integer->Integer
sumaIesimaColumna [] _=0
sumaIesimaColumna _ 0=0
sumaIesimaColumna xs col= sumarTodos (iesimaColumna xs col)

sumarTodos :: [Integer]->Integer
sumarTodos []=0
sumarTodos (x:xs)=x+sumarTodos (xs)

iesimaColumna :: [[Integer]]->Integer->[Integer]
iesimaColumna [] _=[]
iesimaColumna (x:xs) col= (nesimoElemento x col):(iesimaColumna xs col)

nesimoElemento:: [Integer]->Integer->Integer
nesimoElemento [a] _=a
nesimoElemento (x:xs) n|n==1=x 
                       |otherwise=nesimoElemento xs (n-1)
--tema b
--es el parcial prueba