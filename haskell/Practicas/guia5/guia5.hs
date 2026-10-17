--Ejercicio 1
longitud :: [t]->Integer
longitud []=0
longitud (x:xs) = 1+ longitud (xs)

ultimo :: [t]-> t
ultimo [x]=x
ultimo (x:xs)= ultimo (xs)

principio :: [t] -> [t]
principio [x]=[]
principio (x:xs)= [x] ++ principio xs

reverso :: [t] -> [t]
reverso []=[]
reverso (x:xs)= reverso (xs) ++ [x]


--Ejercicio 2
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece t (x:xs)| t==x=True
                  |otherwise=pertenece t xs

todosIguales :: (Eq t) => [t] -> Bool
todosIguales []=True
todosIguales [t]=True
todosIguales (x:y:xs)| x==y=todosIguales(y:xs)
                     |otherwise=False

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos []=True
todosDistintos [t]=True
todosDistintos (x:xs)|comparar1contodos x xs=False
                     |xs==[]=True
                     |otherwise= todosDistintos xs

comparar1contodos :: (Eq t) => t -> [t] -> Bool
comparar1contodos _ []=False
comparar1contodos y (x:xs)
                        |y==x=True
                        |xs==[]=False
                        |otherwise =comparar1contodos y xs
                

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos []=False
hayRepetidos (xs)| todosDistintos xs == False =True
                 |otherwise = False



--Eq es un tipo de dato de equivalencia, es decir, admite la operacion ==
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ []=[]--"_" es que no me importa el valor que me diste antes
quitar t (x:xs)
               |t==x=xs
               |otherwise = x:(quitar t xs)

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ []=[]
quitarTodos x xs| pertenece x xs= quitarTodos x (quitar x xs)
                | otherwise = xs


eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos []=[]
eliminarRepetidos (x:xs) =x:(eliminarRepetidos (quitarTodos x xs)) 
{-
cantidadDeApariciones :: (Eq t) => [t] -> t -> Integer
cantidadDeApariciones [] _=0
cantidadDeApariciones (x:xs) y| x==y =1 + cantidadDeApariciones xs y
                              |otherwise=cantidadDeApariciones xs y

-}
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] []=True
mismosElementos (xs) ys= mismosElementosAux (eliminarRepetidos xs) (eliminarRepetidos ys)

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] []=True
mismosElementosAux [] (x:xs)=False
mismosElementosAux (x:xs) [] =False
mismosElementosAux (x:xs) (y:ys)|(pertenece x (y:ys)) && (pertenece y (x:xs))= mismosElementosAux (quitar y (quitar x (x:xs))) (quitar x (quitar y (y:ys)))
                             |otherwise=False

capicua :: (Eq t) => [t] -> Bool
capicua xs = xs==reverso xs

--Ejercicio 3
sumatoria :: [Integer] -> Integer
sumatoria []=0
sumatoria (x:xs)= x + sumatoria(xs)

productoria :: [Integer] -> Integer
productoria []=1
productoria (x:xs)= x * productoria xs

maximo :: [Integer] -> Integer
maximo [t]=t
maximo (x:y:xs)|x>=y=maximo (x:xs)
                 |otherwise= maximo (y:xs)

maximo2 :: [Integer] -> Integer
maximo2 [t]=t
maximo2 (x:xs)|x>=maximo (xs)=x
              |otherwise= maximo (xs)

ordenar :: [Integer] -> [Integer]
ordenar []=[]
ordenar (xs)= ordenar(quitar (max) xs) ++ [max]
    where max=maximo xs

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ []=[]
sumarN n (x:xs)= (n+x):(sumarN n xs)

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs)= sumarN x (x:xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo []=[]
sumarElUltimo (x:xs)= reverso (sumarElUltimoAux (x:xs))

sumarElUltimoAux :: [Integer] -> [Integer]
sumarElUltimoAux []=[]
sumarElUltimoAux (x:xs) =sumarElPrimero (reverso (x:xs))

pares :: [Integer] -> [Integer]
pares []=[]
pares (x:xs)| esMultiplo x 2= x:(pares xs)
            |otherwise= pares xs

esMultiplo :: Integer -> Integer->Bool
esMultiplo x n| mod x n==0=True
       |otherwise = False

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN 0 _=[]
multiplosDeN _ []=[]
multiplosDeN n (x:xs)| esMultiplo x n = x:(multiplosDeN n xs)
            |otherwise= multiplosDeN n xs

--Ejercicio 4
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos []=[]
sacarBlancosRepetidos [x]=[x]
sacarBlancosRepetidos (x:y:xs)| [x,y]=="  "=sacarBlancosRepetidos (y:xs)
                              |otherwise=x:(sacarBlancosRepetidos (y:xs))

contarPalabras :: [Char] -> Integer
contarPalabras []=0
contarPalabras xs = contarPalabrasaux (sacarBlancosRepetidos (' ':xs++ [' ']))-1

contarPalabrasaux :: [Char] -> Integer
contarPalabrasaux []=0
contarPalabrasaux (x:xs)|x == ' ' = 1+ contarPalabrasaux xs
                        |otherwise= contarPalabrasaux xs

palabras :: [Char] -> [[Char]]
palabras []= []
palabras (xs)= palabrasaux (sacarBlancosRepetidos (' ':xs++ [' ']))

palabrasaux  :: [Char] -> [[Char]]
palabrasaux []=[]
palabrasaux [' ']=[]
palabrasaux (xs)= (primerPalabra xs): palabrasaux (menosPrimerPalabra xs)

primerPalabra :: [Char] ->[Char]
primerPalabra []=[]
primerPalabra (x:y:xs)| y/=' '=y:primerPalabra (y:xs)
                    | otherwise= []


menosPrimerPalabra :: [Char] ->[Char]
menosPrimerPalabra []=[]
menosPrimerPalabra [x]=[x]
menosPrimerPalabra (x:y:xs)| y==' '=' ':xs
                           |otherwise= menosPrimerPalabra (y:xs)

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga []=[]
palabraMasLarga xs= palabraMasLargaaux (palabras xs)

palabraMasLargaaux :: [[Char]] -> [Char]
palabraMasLargaaux []= []
palabraMasLargaaux [x]=x
palabraMasLargaaux (x:y:xs)| longitud x >= longitud y= palabraMasLargaaux (x:xs)
                           |otherwise = palabraMasLargaaux (y:xs)

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos []=[]
aplanarConBlancos (x:xs)= x ++ " " ++ aplanarConBlancos xs

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _=[]
aplanarConNBlancos (x:xs) n= x ++ (nBlancos n) ++ (aplanarConNBlancos xs n)

nBlancos:: Integer ->[Char]
nBlancos 0=[]
nBlancos 1 = " "
nBlancos n= " " ++ nBlancos (n-1)

--Ejercicio 5
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada []=[]
sumaAcumulada [x]=[x]
sumaAcumulada (x:xs) = sumarHasta (x:xs) 0

sumarHasta :: (Num t) => [t] -> t-> [t] 
sumarHasta [] _=[]
sumarHasta (y:ys) acc = (acc + y) : sumarHasta ys (acc + y)

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos []=[]
descomponerEnPrimos (x:xs)= (factoresPrimos x): (descomponerEnPrimos xs)

factoresPrimos :: Integer -> [Integer]
factoresPrimos 2=[2]
factoresPrimos n=factoresPrimosAux n 2

factoresPrimosAux :: Integer -> Integer -> [Integer]
factoresPrimosAux n m| m>n=[]
factoresPrimosAux n m| esPrimo n=[n]
                     |mod n m == 0= m: factoresPrimosAux (div n m) (m)
                     |otherwise=factoresPrimosAux n (siguientePrimo m)

siguientePrimo :: Integer -> Integer
siguientePrimo 2 =3
siguientePrimo n|esPrimo (n+1)= n+1
                |otherwise= siguientePrimo (n+1)

esPrimo :: Integer -> Bool
esPrimo 2=True
esPrimo n| esPrimoAux n 2 = True
         |otherwise=False

esPrimoAux :: Integer -> Integer -> Bool
esPrimoAux n m| m==n=True
              | mod n m ==0=False
              |otherwise = esPrimoAux n (m+1)

--Ejercicio 6
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

--a
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ []= False
enLosContactos nom (contacto:restoDeContactos)| nom==elNombre (contacto)=True
                                            |otherwise = enLosContactos nom restoDeContactos

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto c []=[c]
agregarContacto (n_nuevo,t_nuevo) ((n,t):xs)| n_nuevo==n= (n,t_nuevo):xs
                                            |otherwise= (n,t): (agregarContacto (n_nuevo,t_nuevo) (xs))
contactos=[("dami","222"),("nodami","234")]
nuevo=("sol","444")
viejo=("dami","22")
elNombre :: Contacto -> Nombre
elNombre (nom,num)= fst (nom,num)


elTelefono :: Contacto -> Telefono
elTelefono (nom,num)=snd (nom,num)

--Ejercicio 7
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

existeElLocker :: Identificacion ->MapaDeLockers ->Bool
existeElLocker _ []=False
existeElLocker id (x:xs)|id == fst x=True
                        |otherwise = existeElLocker id xs

ubicacionDelLocker :: Identificacion ->MapaDeLockers ->Ubicacion
ubicacionDelLocker id (x:xs)|id==fst x=snd (snd x)
                            |otherwise= ubicacionDelLocker id xs

estaDisponibleElLocker :: Identificacion ->MapaDeLockers ->Bool
estaDisponibleElLocker id (x:xs)|id==fst x && fst (snd x)==True=True
                                |id==fst x && fst (snd x)==False=False
                                |otherwise= estaDisponibleElLocker id xs
ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers
ocuparLocker id (x:xs)|id==fst x= (ocupo x):xs
                      |otherwise= x: ocuparLocker id xs

ocupo :: Locker -> Locker
ocupo (id,(estado,ubicación))=(id,(False,ubicación))
lockers = [(100,(False,"ZD39I")), (101,(True,"JAH3I")), (103,(True,"IQSA9")), (105,(True,"QOTSA")), (109,(False,"893JJ")), (110,(False,"99292"))]
--Ejerecicio 8
{-[[1, 0, 0], [0, 1, 0], [0, 0, 1]] esto es una matriz, el
 primer elemento es la 1era fila, y su 2do elemento es el elemento 1,2
-}

sumaTotal :: [[Integer]] -> Integer
sumaTotal [x]=sumarFila x
sumaTotal (x:xs)=sumarFila x + (sumaTotal xs)

sumarFila :: [Integer]-> Integer
sumarFila [x]=x
sumarFila (x:xs)=x+sumarFila xs

multiplicarFilas :: [[Integer]]->[Integer]
multiplicarFilas [x]= [multiplicarLista x]
multiplicarFilas (x:xs)=(multiplicarLista x):(multiplicarFilas xs)

multiplicarLista :: [Integer]->Integer
multiplicarLista [x]=x
multiplicarLista (x:xs)=x * multiplicarLista xs


cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones _ []=0
cantidadDeApariciones n (x:xs)= cantidadDeAparicionesEnFila n x + cantidadDeApariciones n xs

cantidadDeAparicionesEnFila :: Integer -> [Integer] -> Integer
cantidadDeAparicionesEnFila _ []=0
cantidadDeAparicionesEnFila n (x:xs)|n==x=1+cantidadDeAparicionesEnFila n xs
                                    |otherwise=cantidadDeAparicionesEnFila n xs

contarPalabras2 :: String ->[[String]] ->Int
contarPalabras2 _ []=0
contarPalabras2 n (x:xs)= cantidadDePalabrasEnFila n x + contarPalabras2 n xs

cantidadDePalabrasEnFila :: String -> [String] -> Int
cantidadDePalabrasEnFila _ []=0
cantidadDePalabrasEnFila n (x:xs)|n==x=1+cantidadDePalabrasEnFila n xs
                                 |otherwise=cantidadDePalabrasEnFila n xs


cantidadDeApariciones2 :: (Eq a) => a -> [[a]] -> Integer
cantidadDeApariciones2 _ []=0
cantidadDeApariciones2 n (x:xs)= cantidadDeAparicionesEnFila2 n x + cantidadDeApariciones2 n xs

cantidadDeAparicionesEnFila2 :: (Eq a) => a -> [a] -> Integer
cantidadDeAparicionesEnFila2 _ []=0
cantidadDeAparicionesEnFila2 n (x:xs)|n==x=1+cantidadDeAparicionesEnFila2 n xs
                                    |otherwise=cantidadDeAparicionesEnFila2 n xs

multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar _ []=[]
multiplicarPorEscalar n (x:xs)= (multiplicarFilasPor n x): multiplicarPorEscalar n xs

multiplicarFilasPor:: Integer-> [Integer]->[Integer]
multiplicarFilasPor _ []=[]
multiplicarFilasPor n (x:xs)=(n*x):multiplicarFilasPor n xs

concatenarFilas :: [[String]] ->[String]
concatenarFilas [x]= [concateno1lista x]
concatenarFilas (x:xs)= [concateno1lista x] ++ concatenarFilas xs

concateno1lista :: [String]->String
concateno1lista [x]=x
concateno1lista (x:xs)= x ++ concateno1lista xs

iesimaFila :: Integer -> [[a]] -> [a]
iesimaFila _ []=[]
iesimaFila 0 (x:xs)=x
iesimaFila n (x:xs)=iesimaFila (n-1) xs

iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna _ []=[]
iesimaColumna n (x:xs)= (nesimoelemento n x): iesimaColumna n xs

nesimoelemento :: Integer -> [a]->a
nesimoelemento 0 (x:xs)=x
nesimoelemento n (x:xs)= nesimoelemento (n-1) xs

matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad n= reverso (matrizIdentidadAux n 1)

matrizIdentidadAux :: Integer -> Integer->[[Integer]]
matrizIdentidadAux n c|n==c= [filaIdentidad n n]
                      |otherwise=( filaIdentidad n c ):(matrizIdentidadAux n (c+1))

filaIdentidad :: Integer ->Integer->[Integer]
filaIdentidad 0 _ =[]
filaIdentidad n m | n == m =  (1:filaIdentidad (n-1) m)
                  |otherwise =  (0:filaIdentidad (n-1) m)

mInts    = [ [1, 2, 3], [40, 50, 60], [70, 80, 9] ]

cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna i xs= cantidadPares (iesimaColumna i xs)

cantidadPares :: [Integer]-> Integer
cantidadPares []=0
cantidadPares (x:xs)| mod x 2==0= 1 +cantidadPares xs
                    |otherwise= cantidadPares xs