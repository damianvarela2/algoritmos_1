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

--2g
--problema sumaDistintos(x,y,z:Z){
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

--problema digitoDecenas(x:Z):Z{
--requiere{True}
--asegura{res es el digito correspondiente a las decenas}}
digitoDecena :: Integer -> Integer
digitoDecena x = div (mod (absoluto x) 100) 10
--podria haber restado digitoUnidades
--podria haber hecho div x 10 y despues sacar el 1er digito