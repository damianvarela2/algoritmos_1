--ej 1.2
formulasValidas :: [(String,String)]->Bool
formulasValidas []=True
formulasValidas xs = not (hayRepetidos (obtenerCandidatos xs))

obtenerCandidatos :: [(String,String)]->[String]
obtenerCandidatos []=[]
obtenerCandidatos ((presidente,vice):xs)=(presidente:vice:(obtenerCandidatos xs))

hayRepetidos::[String]->Bool
hayRepetidos []=False
hayRepetidos (x:xs)|pertenece x xs=True
                   |otherwise=hayRepetidos xs

pertenece :: String -> [String]->Bool
pertenece _ []=False
pertenece palabra (x:xs)|palabra==x=True
                        |otherwise=pertenece palabra xs
--ej 1.1
votosEnBlanco :: [(String,String)]-> [Integer]->Integer->Integer
votosEnBlanco _ xs total= total- sumarVotos xs

sumarVotos :: [Integer]->Integer
sumarVotos []=0
sumarVotos (x:xs)=x+sumarVotos xs

--ej1.3
porcentajeDeVotos :: String ->[(String,String)]->[Integer]->Float 
porcentajeDeVotos _ [] _ =0
porcentajeDeVotos _ _ []=0
porcentajeDeVotos presidente xs votos= 100* division (cantidadDeVotosdeUnPresi presidente (asociarPresiConVotos xs votos)) (sumarVotos votos)


asociarPresiConVotos:: [(String,String)]->[Integer]->[(String,Integer)]
asociarPresiConVotos [] _=[]
asociarPresiConVotos _ []=[]
asociarPresiConVotos (x:xs) (y:ys) =(fst x,y): asociarPresiConVotos xs ys

cantidadDeVotosdeUnPresi :: String ->[(String,Integer)]->Integer
cantidadDeVotosdeUnPresi _ []=0
cantidadDeVotosdeUnPresi presidente ((nombre,votos):xs)|presidente==nombre=votos
                                                       |otherwise = cantidadDeVotosdeUnPresi presidente xs

division :: Integer->Integer->Float
division a b = (fromIntegral a)/(fromIntegral b)

proximoPresidente :: [(String,String)]->[Integer]->String
proximoPresidente (xs) votos= proximoPresidenteAux (buscarMayor votos) (asociarPresiConVotos xs votos)

proximoPresidenteAux::Integer-> [(String,Integer)]->String
proximoPresidenteAux _ []=[]
proximoPresidenteAux max (x:xs)| max == snd x = fst x
                               |otherwise =proximoPresidenteAux max xs

buscarMayor :: [Integer]->Integer
buscarMayor [a]=a
buscarMayor (x:y:xs)| x>=y= buscarMayor (x:xs)
                    |otherwise = buscarMayor (y:xs)
