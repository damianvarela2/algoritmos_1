--Ejercicio 7

type Punto3D = (Float, Float, Float)
distanciaManhattan:: Punto3D -> Punto3D -> Float
distanciaManhattan (a,b,c) (d,e,f) = absolutoflotante (a-d) + absolutoflotante (b-e) + absolutoflotante (c-f)

absolutoflotante :: Float -> Float
absolutoflotante x| x>=0=x
          | x<0=(-x)

absolutoentero :: Int -> Int
absolutoentero x| x>=0=x
          | x<0=(-x)

--Ejercicio 8
comparar :: Int -> Int -> Int
comparar a b|(sumaUltimosDosDigitos a) < (sumaUltimosDosDigitos b)=1
            |(sumaUltimosDosDigitos a) > (sumaUltimosDosDigitos b)=(-1)
            |otherwise=0



digitoUnidades :: Int -> Int
digitoUnidades x = mod (absolutoentero x) 10

digitoDecena :: Int -> Int
digitoDecena x = div (mod (absolutoentero x) 100) 10

sumaUltimosDosDigitos :: Int->Int
sumaUltimosDosDigitos x = (digitoDecena x) + (digitoUnidades x)

--Ejercicio 9
{-
a-
problema f1 (x:R):R{
requiere{true}
asegura{res es 1 si x=0, sino es 0}}

problema f2 (x:R):R{
requiere{x=1 o x=-1}
asegura{res es 15 si x es 1,  y -15 si x=-1}}

problema f3 (x:R):R{
requiere{true}
asegura{res es 7 si x es menor o igual a 9 y 5 sino}}

problema f4 (x, y:R):R{
requiere{}
asegura{res es (x+y)/2}}

problema f5 (t:(R,R)):R{
requiere{}
asegura{res es la suma de la primer componente de t mas la 2da, todo dividido 2}}

problema f6 (x:R n:N):Bool{
requiere{}
asegura{res es true si el entero mas cercano de x es n, sino da false}}

-}