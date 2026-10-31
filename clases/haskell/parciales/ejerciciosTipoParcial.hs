type Fila=[Int]
type Tablero = [Fila]
type Posicion = (Int,Int)
type Camino =[Posicion]

maximo :: Tablero ->Int
maximo t= maximoEnFila (maximoEnCadaFila t)

maximoEnFila:: Fila -> Int
maximoEnFila [a]=a
maximoEnFila (x:xs)|x>=maximoEnFila xs=x
                   |otherwise= maximoEnFila xs

maximoEnCadaFila :: [Fila]->[Int]
maximoEnCadaFila []=[]
maximoEnCadaFila (x:xs)= (maximoEnFila x):(maximoEnCadaFila xs)

masRepetido :: Tablero ->Int
masRepetido (x:xs)= encontrarPrimero (maximoEnFila (listaDeSegundos (repeticionEnFilas (masRepetidoAux (x:xs))))) (repeticionEnFilas (masRepetidoAux (x:xs)))

masRepetidoAux :: Tablero -> Fila
masRepetidoAux []=[]
masRepetidoAux (x:xs)=x ++ masRepetidoAux(xs)

repeticionEnFilas :: Fila->[(Int,Int)]
repeticionEnFilas []=[]
repeticionEnFilas (x:xs)=(x,cantidadDeApariciones x (x:xs)):repeticionEnFilas xs

cantidadDeApariciones :: Int -> [Int]->Int
cantidadDeApariciones _ []=0
cantidadDeApariciones n (x:xs)|n==x=1+cantidadDeApariciones n xs
                              |otherwise=cantidadDeApariciones n xs

concatenacionFilas :: [(Int,Int)]->[(Int,Int)]->[(Int,Int)]
concatenacionFilas [] x=x
concatenacionFilas y []=y
concatenacionFilas (x:xs) (y:ys)=concatenacionFilasAux x (y:ys):concatenacionFilasAux y (x:xs) :(concatenacionFilas xs (ys))

concatenacionFilasAux :: (Int,Int)->[(Int,Int)]->(Int,Int)
concatenacionFilasAux (x,y) []=(x,y)
concatenacionFilasAux (posicion,cantidadEnFila) (y:ys)|posicion== fst y=(posicion,cantidadEnFila+ snd y)
                                                      |otherwise=concatenacionFilasAux (posicion,cantidadEnFila) (ys)
listaDeSegundos:: [(Int,Int)]->[Int]
listaDeSegundos []=[]
listaDeSegundos ((x,y):xs)=y:listaDeSegundos xs

encontrarPrimero :: Int -> [(Int,Int)]->Int
encontrarPrimero n ((x,y):xs)|n==y=x
                             |otherwise=encontrarPrimero n xs

                             
valoresDeCamino :: Tablero ->Camino ->[Int]
valoresDeCamino _ []=[]
valoresDeCamino t ((f,c):xs)= (acceder t (f,c)):(valoresDeCamino t xs)


acceder:: Tablero ->Posicion->Int
acceder t (f,c)=  nesimoElemento c (nesimoFila f t)

nesimoFila :: Int-> Tablero -> Fila
nesimoFila 1 (x:xs)=x
nesimoFila n (x:xs)=nesimoFila (n-1) xs

nesimoElemento :: Int->Fila ->Int
nesimoElemento 1 (x:xs)=x
nesimoElemento n (x:xs)=nesimoElemento (n-1) xs

esFibonacci :: Int -> Bool
esFibonacci 0 = True
esFibonacci n =esFibonacciAux n 1

esFibonacciAux ::Int->Int->Bool
esFibonacciAux n m| n == iesimoFibonacci m =True
                  |n< iesimoFibonacci m=False
                  |otherwise= esFibonacciAux n (m+1)

iesimoFibonacci :: Int -> Int
iesimoFibonacci 0=0
iesimoFibonacci 1 =1
iesimoFibonacci n= iesimoFibonacci (n-1) +iesimoFibonacci (n-2)

esCaminoFibo :: [Int] ->Int ->Bool
esCaminoFibo (x:xs) n|iesimoFibonacci n==x && esFibonacciListaOrdenada (x:xs) n=True
                     |otherwise=False

siguienteFiboindice::Int->Int
siguienteFiboindice m= iesimoFibonacci (m+1)

siguienteFibo::Int->Int
siguienteFibo 0 =1
siguienteFibo m=siguienteFiboAux m 1

siguienteFiboAux::Int->Int->Int
siguienteFiboAux m i|iesimoFibonacci i ==m=iesimoFibonacci (i+1)
                    |otherwise=siguienteFiboAux m (i+1)

esFibonacciListaOrdenada :: [Int]->Int->Bool
esFibonacciListaOrdenada [] _=True
esFibonacciListaOrdenada (x:xs) i|x==iesimoFibonacci i=esFibonacciListaOrdenada xs (i+1)
                                 |otherwise=False


divisoresPropios :: Int ->[Int]
divisoresPropios n= divisoresPropiosAux n 1

esDivisor :: Int->Int->Bool
esDivisor _ 1 =True
esDivisor n d | mod n d ==0=True
              |otherwise=False

divisoresPropiosAux :: Int->Int->[Int]
divisoresPropiosAux 1 _=[1]
divisoresPropiosAux n m|n<=m=[]
                       |esDivisor n m =m:divisoresPropiosAux n (m+1)
                       |otherwise= divisoresPropiosAux n (m+1)

sumarTodos :: [Int]->Int
sumarTodos []=0
sumarTodos (x:xs)=x+sumarTodos xs

sonAmigos :: Int->Int->Bool
sonAmigos n m| sumarTodos (divisoresPropios n) == m && n==sumarTodos (divisoresPropios m) && n/=m=True 
             |otherwise=False

losPrimerosNPerfectos :: Int ->[Int]
losPrimerosNPerfectos n = listaDePerfectos n 1

listaDePerfectos :: Int->Int->[Int]
listaDePerfectos 0 _ =[]
listaDePerfectos n m|esPerfecto m=m:listaDePerfectos (n-1) (m+1)
                    |otherwise= listaDePerfectos n (m+1)

losPerfectosHasta :: Int->Int->[Int]
losPerfectosHasta n m|n<m=[]
                            |esPerfecto m=m: losPerfectosHasta n (m+1)  
                            |otherwise= losPerfectosHasta n (m+1)


esPerfecto ::Int->Bool
esPerfecto 1=False
esPerfecto n| sumarTodos (divisoresPropios n)==n=True   
            |otherwise=False

listaDeAmigos :: [Int] ->[(Int,Int)]
listaDeAmigos []=[]
listaDeAmigos [x]=[]
listaDeAmigos (x:y:xs)=  compararConTodos x (y:xs) ++ listaDeAmigos (y:xs)

parSiSonAmigos :: Int ->Int -> [(Int,Int)]
parSiSonAmigos a b|sonAmigos a b= [(a,b)]
                  |otherwise=[]

compararConTodos:: Int -> [Int]->[(Int,Int)]
compararConTodos _ []=[]
compararConTodos x (y:ys)=parSiSonAmigos x y ++ compararConTodos x ys