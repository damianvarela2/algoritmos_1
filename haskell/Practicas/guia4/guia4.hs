import GHC.Base (TrName(TrNameD))
import Text.Printf (FieldFormatter)
--Ejercicio 1
{-
problema fibonacci (n: Z) : Z {
requiere: { n ≥ 0 }
asegura: { resultado = f ib(n) }
}
-}
fibonacci :: Integer->Integer
fibonacci n| n==0=0
           | n==1=1
           |otherwise= fibonacci (n-1) + fibonacci (n-2)

--Ejercicio 2
{-
problema parteEntera (x: R) : Z {
requiere: { x ≥ 0 }
asegura: { resultado ≤ x < resultado + 1 }
}
-}
parteEntera :: Float ->Integer
parteEntera x| x<1=0
             |otherwise = parteEntera(x-1)+1

--Ejercicio 3
{-
problema esDivisible (n, m:N):Bool{
    requiere{}
    asegura{res es true si n es multiplo de m}
}-}
esDivisible :: Integer ->Integer ->Bool
esDivisible n m| n==0=True
               | n<0=False
               | otherwise = esDivisible (n-m) m

--Ejercicio 4
{-
problema sumaImpares (n:N):N{
    requiere{}
    asegura{res es la suma de los primeros n impares}
}
-}
sumaImpares :: Integer ->Integer
sumaImpares n| n==1=1
             | otherwise=sumaImpares(n-1)+ n_esimo_impar
             where n_esimo_impar=2*n-1

--Ejercicio 5
--medio factorial
medioFact :: Integer ->Integer
medioFact n|n==0=1
           |n==1=1
           |otherwise= n * medioFact(n-2)

--Ejercicio 6
todosDigitosIguales :: Integer ->Bool
todosDigitosIguales n|n<10=True
                     |digitoUnidades(todosalvoUnidades n)== (digitoUnidades n) && todosDigitosIguales (todosalvoUnidades n)=True
                     |otherwise=False

--Ejercicio 7
iesimoDigito :: Integer ->Integer ->Integer
iesimoDigito n i| n==0=0
                |otherwise= mod (div n (10^(cantDigitos n-i))) 10

cantDigitos :: Integer -> Integer
cantDigitos n|n<10=1
             |otherwise = 1+ cantDigitos (div n 10)

digitoUnidades :: Integer -> Integer
digitoUnidades n= mod n 10

todosalvoUnidades :: Integer -> Integer
todosalvoUnidades n= div n 10

--Ejercicio 8
sumaDigitos :: Integer ->Integer
sumaDigitos n|n<10=n
             |otherwise= sumaDigitos(todosalvoUnidades n) + digitoUnidades n

--Ejercicio 9
esCapicua :: Integer ->Bool
esCapicua n|n<10=True
           |otherwise= esCapicua (todosalvoMasGrande (div n 10)) && digitoUnidades n == masGrande n

todosalvoMasGrande :: Integer ->Integer
todosalvoMasGrande n= mod n (10^(cantDigitos n -1))

masGrande :: Integer ->Integer
masGrande n= div n (10^(cantDigitos n -1))
--Ejercicio 10a
f1 :: Integer -> Integer
f1 n|n==0=1
    |otherwise= f1(n-1)+2^n

--Ejercicio 10b
f2 :: Integer->Float->Float
f2 n q|n==1=q
      |otherwise= q^n +f2 (n-1) q
--Ejercicio 10c
f3:: Integer -> Float -> Float
f3 n q|n==0=1
      |otherwise = f2 (2*n) q
--Ejercicio 10d
f4::Integer -> Float -> Float
f4 n q= (sumatoriaDesde (2*n) n  q)

sumatoriaDesde :: Integer -> Integer -> Float -> Float
sumatoriaDesde n k q| n<k=0
                    |otherwise = q^k + sumatoriaDesde n (k+1) q
--Ejercicio 11

eAprox :: Integer ->Float
eAprox 0=1
eAprox n = eAprox (n-1)+ 1/(factorial n)

factorial :: Integer -> Float
factorial 0=1
factorial n= (fromIntegral n)*factorial (n-1)

--b
e= eAprox 10

--Ejercicio 12
serieRaiz2 :: Integer ->Float
serieRaiz2 0=1/2
serieRaiz2 n= 2+(1/(serieRaiz2(n-1)))

raizDe2Aprox :: Integer ->Float
raizDe2Aprox n=serieRaiz2 n -1


--Ejercicio 13
f :: Integer -> Integer -> Integer
f 1 j= faux 1 j
f i j=faux i j + f (i-1) j


faux :: Integer -> Integer -> Integer
faux i 1 = i
faux i j=i^j + faux i (j-1)



--Ejercicio 14
sumaPotencias :: Integer ->Integer ->Integer ->Integer
sumaPotencias q 1 m = sumaPotenciasAux q 1 m
sumaPotencias q n m = sumaPotenciasAux q n m + sumaPotencias q (n-1) m

sumaPotenciasAux :: Integer ->Integer ->Integer ->Integer
sumaPotenciasAux q n 1= q^(n+1)
sumaPotenciasAux q n m= q^(n+m)+ sumaPotenciasAux q n (m-1)

--Ejercicio 15
sumaRacionales :: Integer ->Integer ->Float
sumaRacionales 1 q= sumaRacionalesAux 1 q
sumaRacionales p q= sumaRacionalesAux p q + sumaRacionales (p-1) q


sumaRacionalesAux :: Integer ->Integer ->Float
sumaRacionalesAux p 1=fromIntegral p
sumaRacionalesAux p q= fromIntegral p/fromIntegral q + sumaRacionalesAux p (q-1)


--Ejercicio 16a
menorDivisor :: Integer ->Integer
menorDivisor n|n==1=1
              |otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n k| mod n k == 0=k
                   |otherwise = menorDivisorDesde n (k+1)

--Ejercicio 16b
esPrimo :: Integer ->Bool
esPrimo n|n==1=False
         |menorDivisor n == n=True
         |otherwise = False
esPrimo2 :: Integer ->Bool
esPrimo2 n= n>1 && menorDivisor n == n

sonCoprimos :: Integer ->Integer ->Bool
sonCoprimos n m|n==1 || m==1 = True
               |1/=menorComunDivisorAux n m 2=False
               |otherwise = True


menorComunDivisorAux :: Integer -> Integer -> Integer -> Integer
menorComunDivisorAux n m k
  | (mod n k==0) && (mod m k ==0) = k
  | (k==n)||(k==m) = 1
  | otherwise = menorComunDivisorAux n m (k+1)

nEsimoPrimo :: Integer ->Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = siguientePrimoDesde (nEsimoPrimo (n-1)+1)

siguientePrimoDesde :: Integer -> Integer
siguientePrimoDesde n| esPrimo n = n
                     |otherwise =siguientePrimoDesde(n+1)

--Ejercicio 17

esFibonacci :: Integer ->Bool
esFibonacci n=esFibonacciAux n 0


esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n m|fibonacci m > n=False
                  |fibonacci m == n = True
                  |otherwise=esFibonacciAux n (m+1)

--Ejercicio 18
--mayorDigitoPar :: Integer ->Integer
--mayorDigitoPar n| meQuedoLosPares n==-1=-1
--                |otherwise=

recorrerCifras:: Integer-> Integer
recorrerCifras n i|recorrerCifras n 1=digitoUnidades n
                  |recorrerCifras n i

meQuedoLosPares :: Integer -> Integer
meQuedoLosPares n
  | n == 0    = -1
  | mod n 2 == 0 = juntar (digitoUnidades n) resto
  | otherwise    = resto
  where resto = meQuedoLosPares (div n 10)

juntar :: Integer -> Integer -> Integer
juntar d resto
  | resto == -1 = d
  | otherwise   = resto * 10 + d

--Ejercicio 19
esSumaInicialDePrimos :: Integer ->Bool
esSumaInicialDePrimos 0=True
esSumaInicialDePrimos n = esSumaDePrimerosKPrimos 1 n 

esSumaDePrimerosKPrimos :: Integer -> Integer -> Bool
esSumaDePrimerosKPrimos k n| (sumaKprimos k == n) = True
                           | (sumaKprimos k > n)=False
                           |otherwise= esSumaDePrimerosKPrimos (k+1) n


sumaKprimos :: Integer -> Integer
sumaKprimos i|i==0=0
             |otherwise= nEsimoPrimo i + sumaKprimos (i-1)
