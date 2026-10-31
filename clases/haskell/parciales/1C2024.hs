--Ejercicio 1
quitar::String->[String]->[String]
quitar _ []=[]
quitar palabra (x:xs)| palabra==x= xs
                     |otherwise =x:quitar palabra xs
quitarTodos:: String ->[String]->[String]
quitarTodos _ []=[]
quitarTodos palabra (xs)| pertenece palabra xs= quitarTodos (palabra) (quitar palabra xs)
                        |otherwise=xs
pertenece:: String->[String]->Bool
pertenece _ []=False
pertenece palabra (x:xs)|palabra==x=True
                        |otherwise= pertenece palabra xs

cantidadApariciones :: [String]->String->Integer
cantidadApariciones [] _=0
cantidadApariciones (x:xs) palabra| x==palabra=1+cantidadApariciones xs palabra
                                  |otherwise=cantidadApariciones xs palabra

generarStock :: [String]-> [(String,Integer)]
generarStock []=[]
generarStock (x:xs) = (x,cantidadApariciones (x:xs) x): generarStock (quitarTodos x xs)

--Ejercicio 2
stockDeProducto :: [(String,Integer)] -> String -> Integer
stockDeProducto [] _=0
stockDeProducto ((producto,cantidad):xs) query|query==producto=cantidad
                                              |otherwise =stockDeProducto xs query

chad = generarStock ["a","a","b","c","a"]
chad2= [("a",3),("b",1),("c",1)]
precios = [("a",fromInteger 100),("b",fromInteger 200),("c",fromInteger 300)]
--Ejercicio 3
dineroEnStock:: [(String,Integer)]->[(String,Float)]->Float
dineroEnStock [] _=0
dineroEnStock ((nom,cantidad):xs) ((nombre,precio):ys)=  enStockdeUno nom ((nom,cantidad):xs) ((nombre,precio):ys)+ dineroEnStock xs ((nombre,precio):ys)

enStockdeUno :: String -> [(String,Integer)]->[(String,Float)]->Float
enStockdeUno _ [] _ =0
enStockdeUno producto (x:xs) (y:ys)= precioDeProducto producto (y:ys) * fromIntegral (cantidadDeProducto producto (x:xs))

precioDeProducto ::  String -> [(String,Float)]->Float
precioDeProducto _ []=0
precioDeProducto producto (x:xs)| producto== fst x = (snd x) 
                                |otherwise= precioDeProducto producto xs

cantidadDeProducto ::  String -> [(String,Integer)]->Integer
cantidadDeProducto _ []=0
cantidadDeProducto producto (x:xs)| fst x == producto = snd x
                                  |otherwise = cantidadDeProducto producto xs

--Ejercicio 4
aplicarOferta :: [(String,Integer)]->[(String,Float)]->[(String,Float)]
aplicarOferta _ [] = []
aplicarOferta (xs) ((nom,precio):ys)| cantidadDeProducto nom (xs) >10= (nom, 0.8*precio):aplicarOferta xs ys
                                         |otherwise=(nom, precio):aplicarOferta (xs) ys