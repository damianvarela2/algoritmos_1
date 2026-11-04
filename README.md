# Algoritmos y Estructuras de Datos I

Resoluciones de guías prácticas, apuntes de clase y modelos de examen de la materia **Algoritmos y Estructuras de Datos I** (equivalente a *Introducción a la Programación*), dictada en el Departamento de Computación de la Facultad de Ciencias Exactas y Naturales, Universidad de Buenos Aires (FCEyN - UBA).

---

## Tabla de contenidos

1. [Descripción general](#descripción-general)
2. [Estructura del repositorio](#estructura-del-repositorio)
3. [Contenidos por módulo](#contenidos-por-módulo)
   - [Programación Funcional (Haskell)](#1-programación-funcional-haskell)
   - [Programación Imperativa (Python)](#2-programación-imperativa-python)
   - [Clases y material de evaluación](#3-clases-y-material-de-evaluación)
4. [Lineamientos de cátedra para evaluaciones](#lineamientos-de-cátedra-para-evaluaciones)
   - [Especificación de funciones permitidas en Haskell](#especificación-de-funciones-permitidas-en-haskell)
   - [Especificación de funciones permitidas en Python](#especificación-de-funciones-permitidas-en-python)
5. [Entorno y ejecución](#entorno-y-ejecución)
6. [Información académica](#información-académica)

---

## Descripción general

Este repositorio centraliza el desarrollo práctico de la asignatura a lo largo del cuatrimestre. El programa aborda la resolución de problemas a partir de especificaciones formales (contratos con precondiciones `requiere` y postcondiciones `asegura`) bajo dos paradigmas de programación:

- **Paradigma funcional (Haskell):** Tipos básicos, funciones, recursión sobre enteros y listas, polimorfismo y *pattern matching*.
- **Paradigma imperativo (Python):** Estado, control de flujo, pasaje de parámetros por valor y referencia (`in`, `out`, `inout`), secuencias, matrices, tipos abstractos de datos (Pilas y Colas), diccionarios, manejo de archivos y pruebas unitarias (`unittest`).

---

## Estructura del repositorio

```text
algoritmos_1/
├── haskell/
│   └── Practicas/
│       ├── guia3/                      # Guía 3: Introducción a Haskell y tipos básicos
│       ├── guia4/                      # Guía 4: Recursión sobre números enteros
│       └── guia5/                      # Guía 5: Recursión sobre listas
│
├── python/
│   └── guias/
│       ├── guia6/                      # Guía 6: Introducción a la programación imperativa
│       ├── guia7/                      # Guía 7: Secuencias, listas y matrices (+ tests)
│       └── guia8/                      # Guía 8: Pilas, colas, diccionarios y archivos (+ tests)
│
└── clases/
    ├── haskell/
    │   ├── Practicas/                  # Ejercicios desarrollados durante las clases prácticas
    │   ├── parciales/                  # Exámenes parciales resueltos de cuatrimestres anteriores
    │   ├── funcioneshs.hs              # Funciones auxiliares y de repaso general
    │   ├── SolucionT1(1).hs            # Resolución de tema de evaluación
    │   └── nota_practica_ip_26-08.txt  # Apuntes de clase práctica
    └── python/
        ├── clase28_9.py                # Introducción a pruebas unitarias con unittest
        ├── clase5_10python.py          # Ejercicios de secuencias y ciclos
        ├── clase7_10.py                # Práctica sobre listas y mutabilidad
        ├── clase19_10.py               # Práctica sobre TAD Pila y Cola
        ├── claseDiccionarios.py        # Práctica sobre diccionarios y manejo de archivos
        ├── test.py                     # Casos de prueba desarrollados en clase
        └── atajos_python               # Notas de referencia rápida del lenguaje
```

---

## Contenidos por módulo

### 1. Programación Funcional (Haskell)

Resoluciones ubicadas en [`haskell/Practicas/`](./haskell/Practicas/):

| Guía | Archivo principal | Contenidos abordados |
| :--- | :--- | :--- |
| **Guía 3** | [`guia3.hs`](./haskell/Practicas/guia3/guia3.hs) | Definición de funciones, signaturas de tipos, guardas, *pattern matching* y operaciones con tuplas. |
| **Guía 4** | [`guia4.hs`](./haskell/Practicas/guia4/guia4.hs) | Esquemas de recursión sobre números enteros, divisibilidad, extracción de dígitos y sumatorias. |
| **Guía 5** | [`guia5.hs`](./haskell/Practicas/guia5/guia5.hs) | Recursión estructural sobre listas, polimorfismo, predicados sobre secuencias y manipulación de cadenas de caracteres (`[Char]`). |

---

### 2. Programación Imperativa (Python)

Resoluciones y suites de pruebas ubicadas en [`python/guias/`](./python/guias/):

| Guía | Código fuente | Suite de pruebas | Contenidos abordados |
| :--- | :--- | :--- | :--- |
| **Guía 6** | [`guia6.py`](./python/guias/guia6/guia6.py) | — | Funciones en Python, tipado estático, estructuras condicionales e iteración mediante `while` y `for`. |
| **Guía 7** | [`guia7.py`](./python/guias/guia7/guia7.py) | [`tests_guia7.py`](./python/guias/guia7/tests_guia7.py) | Recorrido y modificación de listas y matrices, aliasing, mutabilidad y cumplimiento de contratos `in`, `out` e `inout`. |
| **Guía 8** | [`guia8.py`](./python/guias/guia8/guia8.py) | [`tests_guia8.py`](./python/guias/guia8/tests_guia8.py) | Tipos Abstractos de Datos (`LifoQueue` y `Queue`), preservación de parámetros de entrada, diccionarios (`dict`) y lectura/escritura de archivos de texto. |

---

### 3. Clases y material de evaluación

El directorio [`clases/`](./clases/) reúne resoluciones hechas durante el cursado y entrenamientos para las instancias de evaluación:

- **Modelos de primer parcial (Haskell):** Disponibles en [`clases/haskell/parciales/`](./clases/haskell/parciales/):
  - [`parcial2C2023.hs`](./clases/haskell/parciales/parcial2C2023.hs) — Segundo cuatrimestre 2023
  - [`1C2024.hs`](./clases/haskell/parciales/1C2024.hs) — Primer cuatrimestre 2024
  - [`parcial2C2024.hs`](./clases/haskell/parciales/parcial2C2024.hs) — Segundo cuatrimestre 2024
  - [`parcial1C2025.hs`](./clases/haskell/parciales/parcial1C2025.hs) — Primer cuatrimestre 2025
  - [`ejerciciosTipoParcial.hs`](./clases/haskell/parciales/ejerciciosTipoParcial.hs) — Ejercicios integradores adicionales
- **Entregas y simulacros de Haskell:** En [`clases/haskell/`](./clases/haskell/) se incluyen las resoluciones y reportes de corrección automática del simulacro y de la evaluación parcial.
- **Prácticas de clase en Python:** En [`clases/python/`](./clases/python/) se encuentran los scripts trabajados en laboratorio sobre testing unitario ([`clase28_9.py`](./clases/python/clase28_9.py)), listas ([`clase7_10.py`](./clases/python/clase7_10.py)), pilas y colas ([`clase19_10.py`](./clases/python/clase19_10.py)) y diccionarios/archivos ([`claseDiccionarios.py`](./clases/python/claseDiccionarios.py)).

---

## Lineamientos de cátedra para evaluaciones

En las evaluaciones parciales de la materia rige una restricción estricta sobre las primitivas del lenguaje que pueden utilizarse. Cualquier función, método o construcción que no se encuentre en el listado oficial de la cátedra debe ser implementada manualmente como función auxiliar; de lo contrario, el ejercicio se considera inválido.

### Especificación de funciones permitidas en Haskell

#### Primitivas permitidas

| Categoría | Funciones y operadores |
| :--- | :--- |
| **División entera** | `mod :: Integral a => a -> a -> a`<br>`div :: Integral a => a -> a -> a` |
| **Tuplas** | `fst :: (a, b) -> a`<br>`snd :: (a, b) -> b` |
| **Listas** | `(:) :: a -> [a] -> [a]`<br>`(++) :: [a] -> [a] -> [a]`<br>`head :: [a] -> a`<br>`tail :: [a] -> [a]` |
| **Aritmética y conversión** | `sqrt :: Floating a => a -> a`<br>`fromIntegral :: (Integral a, Num b) => a -> b`<br>`fromInteger :: Num a => Integer -> a`<br>Operadores: `+`, `-`, `*`, `/`, `**`, `^` |
| **Lógica y comparación** | `not :: Bool -> Bool`<br>Operadores: `&&`, `||`, `==`, `/=`, `>`, `<`, `>=`, `<=` |
| **Definiciones locales** | Cláusula `where` |

#### Construcciones y funciones no permitidas en Haskell

| Restricción | Criterio de resolución |
| :--- | :--- |
| Expresión condicional `if ... then ... else ...` | Utilizar exclusivamente guardas (`\|`) o *pattern matching*. |
| Funciones de listas del `Prelude` (`length`, `elem`, `reverse`, `init`, `last`, `take`, `drop`, `(!!)`) | Implementarlas de forma recursiva mediante `head`, `tail` y `(:)`. |
| Funciones de orden superior (`map`, `filter`, `foldr`, `foldl`, `zip`, `any`, `all`) | Desarrollar la recursión explícitamente. |
| Funciones numéricas auxiliares (`abs`, `max`, `min`, `even`, `odd`, `gcd`, `lcm`, `sum`, `maximum`, `minimum`) | Definirlas manualmente como funciones auxiliares. |
| Listas por comprensión (`[x \| x <- xs]`) y rangos (`[1..n]`) | Generar las secuencias mediante funciones recursivas. |

---

### Especificación de funciones permitidas en Python

#### Primitivas y métodos permitidos

| Categoría | Elementos habilitados |
| :--- | :--- |
| **Conversión de tipos** | `int`, `list`, `float`, `str`, `tuple`, `bool` |
| **Estructuras de control** | `if`, `elif`, `else`, `while`, `for ... in range(...)`, `for ... in secuencia` |
| **Rango** | `range(i, f, p)` (con 1, 2 o 3 argumentos) |
| **Operaciones aritméticas** | `+`, `-`, `*`, `/`, `//`, `%`, `sqrt`, `round`, `floor`, `ceil` |
| **Lógica y comparación** | `and`, `or`, `not`, `==`, `!=`, `>`, `<`, `>=`, `<=` |
| **Secuencias** | Pertenencia (`in`), concatenación (`+`), repetición (`*`), longitud (`len(s)`), indexación positiva (`s[i]`) |
| **Métodos de `list`** | `append(e)`, `insert(p, e)`, `remove(e)`, `index(e)`, `count(e)`, `clear()`, `pop()`, `pop(n)`, `copy()` |
| **Métodos de `dict`** | `items()`, `keys()`, `values()`, `pop(clave)`, `clear()` |
| **TAD Pila (`queue.LifoQueue`)** | `LifoQueue()`, `put(e)`, `get()`, `empty()` |
| **TAD Cola (`queue.Queue`)** | `Queue()`, `put(e)`, `get()`, `empty()` |
| **Manejo de archivos** | `open`, `read`, `readline`, `readlines`, `write`, `writelines`, `close`, `os.path.join()`, `os.path.exists()` |

#### Construcciones y funciones no permitidas en Python

| Restricción | Criterio de resolución |
| :--- | :--- |
| *Slicing* de secuencias (`s[i:f]`, `s[::-1]`, `s[:]`) | Recorrer la secuencia mediante ciclos e indexación positiva `s[i]`. |
| Indexación negativa (`s[-1]`, `s[-i]`) | Utilizar índices calculados a partir de la longitud: `s[len(s) - i]`. |
| Funciones *built-in* de agregación u orden (`max`, `min`, `sum`, `abs`, `sorted`, `reversed`, `enumerate`, `zip`, `set`) | Implementar funciones auxiliares iterativas. |
| Métodos de listas no listados (`sort()`, `reverse()`, `extend()`) | Implementar el algoritmo correspondiente o agregar elementos con `append()`. |
| Métodos de cadenas (`split()`, `strip()`, `replace()`, `lower()`, `upper()`, `join()`, `find()`) | Procesar el `str` carácter por carácter mediante iteración. |
| Métodos de diccionarios no listados (`get()`, `update()`, `setdefault()`) | Consultar existencia mediante `clave in d.keys()` y acceder con `d[clave]`. |
| Acceso a atributos internos de `Queue` / `LifoQueue` (`.queue`, `.qsize()`) | Operar únicamente con `put()`, `get()` y `empty()`, utilizando una estructura auxiliar para reconstruir el parámetro de entrada. |
| Comprensiones de listas/diccionarios y expresiones `lambda` | Instanciar la estructura vacía y poblarla mediante un ciclo `for` o `while`. |
| Sentencias `break` y `continue` | No recomendadas por la cátedra; estructurar la condición de corte en el encabezado del ciclo `while`. |
| Omisión de anotaciones de tipo | Todas las firmas de funciones y variables deben contar con su anotación de tipo estática. |

---

## Entorno y ejecución

### Requisitos

- **GHC / GHCi** (Glasgow Haskell Compiler) para los módulos de programación funcional.
- **Python 3.10+** para los módulos de programación imperativa (se requiere soporte para anotaciones de tipos nativas como `list[int]`, `tuple[str, int]`, `dict[str, float]`).

### Ejecución de guías en Haskell

Iniciar el intérprete interactivo cargando el archivo deseado desde la raíz del repositorio:

```bash
ghci haskell/Practicas/guia5/guia5.hs
```

Comandos habituales dentro de `GHCi`:

```text
:r            Recarga el módulo actual tras modificar el archivo.
:t <funcion>  Muestra la signatura de tipos de una función.
:q            Finaliza la sesión del intérprete.
```

### Ejecución de pruebas unitarias en Python

Las guías 7 y 8 cuentan con suites de pruebas automatizadas implementadas con el módulo estándar `unittest`. Para ejecutarlas desde la raíz del repositorio:

```bash
# Pruebas de la Guía 7 (Listas y matrices)
python3 -m unittest python/guias/guia7/tests_guia7.py -v

# Pruebas de la Guía 8 (Pilas, colas y diccionarios)
python3 -m unittest python/guias/guia8/tests_guia8.py -v
```

---

## Información académica

- **Asignatura:** Algoritmos y Estructuras de Datos I / Introducción a la Programación
- **Departamento:** Departamento de Computación (DC)
- **Facultad:** Facultad de Ciencias Exactas y Naturales (FCEyN)
- **Universidad:** Universidad de Buenos Aires (UBA)
