<div align="center">

# 🎓 Algoritmos y Estructuras de Datos I
### *Introducción a la Programación — DC, FCEyN (UBA)*

[![UBA](https://img.shields.io/badge/UBA-Exactas%20(DC)-1b365d?style=for-the-badge&logo=google-scholar&logoColor=white)](https://www.dc.uba.ar/)
[![Haskell](https://img.shields.io/badge/Haskell-GHCi-5e5086?style=for-the-badge&logo=haskell&logoColor=white)](#1--parcial-de-haskell)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=ffd343)](#2--parcial-de-python)
[![Tests](https://img.shields.io/badge/Tests-unittest-2ea44f?style=for-the-badge&logo=pytest&logoColor=white)#](#-ejecución-rápida)

*Repositorio de guías prácticas, apuntes de clase, modelos de parcial y Trabajo Práctico del 2.º Cuatrimestre 2026.*

---

[📂 Estructura](#-estructura-del-repositorio) •
[📚 Progreso de Guías](#-progreso-de-guías-y-contenidos) •
[🚫 Funciones Permitidas e Inválidas](#-funciones-permitidas-y-prohibidas-en-parciales) •
[🚀 Ejecución Rápida](#-ejecución-rápida)

</div>

---

## 📂 Estructura del repositorio

```text
algoritmos_1/
├── 🟣 haskell/
│   └── Practicas/
│       ├── guia3/                      # Guía 3: Introducción a Haskell, tuplas y pattern matching
│       ├── guia4/                      # Guía 4: Recursión sobre números enteros
│       └── guia5/                      # Guía 5: Recursión sobre listas y polimorfismo
│
├── 🐍 python/
│   └── guias/
│       ├── guia6/                      # Guía 6: Introducción al lenguaje imperativo
│       ├── guia7/                      # Guía 7: Listas, matrices y pasaje de parámetros (+ unittest)
│       └── guia8/                      # Guía 8: Pilas (LifoQueue), Colas (Queue), Diccionarios y Archivos (+ unittest)
│
├── 📓 clases/
│   ├── haskell/                        # Prácticas en clase, funciones auxiliares y simulacros
│   │   ├── funcioneshs.hs              # Compendio de funciones de práctica
│   │   ├── SolucionT1(1).hs            # Resolución de tema de evaluación
│   │   └── parciales/                  # Modelos resueltos (2C2023, 1C2024, 2C2024, 1C2025)
│   └── python/                         # Apuntes de clase (clase5_10, clase7_10, clase19_10) y atajos
│
├── ♟️ tp/
│   ├── Enunciado_v1.2.pdf              # Especificación formal del Trabajo Práctico
│   └── 2c2026_tppython/                # TP de Python: Juego Arimaa (lógica, interfaz gráfica y suite de tests)
│
├── 📄 validas_parcial_hs.pdf           # Documento oficial: funciones permitidas en Haskell
└── 📄 validas_parcial_py.pdf           # Documento oficial: funciones permitidas en Python
```

---

## 📚 Progreso de Guías y Contenidos

| Módulo | Unidad / Archivo | Temas Principales | Tests | Estado |
| :---: | :--- | :--- | :---: | :---: |
| **Haskell** | [`guia3.hs`](./haskell/Practicas/guia3/guia3.hs) | Tipos básicos, guardas, *pattern matching* y tuplas | `GHCi` | ✅ Completada |
| **Haskell** | [`guia4.hs`](./haskell/Practicas/guia4/guia4.hs) | Recursión sobre enteros, divisibilidad, sumatorias | `GHCi` | ✅ Completada |
| **Haskell** | [`guia5.hs`](./haskell/Practicas/guia5/guia5.hs) | Recursión sobre listas, orden, strings | `GHCi` | ✅ Completada |
| **Haskell** | [`clases/haskell/parciales/`](./clases/haskell/parciales/) | Parciales `2C2023`, `1C2024`, `2C2024`, `1C2025` y simulacro | `GHCi` | ✅ Resueltos |
| **Python** | [`guia6.py`](./python/guias/guia6/guia6.py) | Funciones, condicionales, ciclos `while` / `for` | Manual | ✅ Completada |
| **Python** | [`guia7.py`](./python/guias/guia7/guia7.py) | Secuencias, listas, matrices, mutabilidad (`in`/`out`/`inout`) | [`tests_guia7.py`](./python/guias/guia7/tests_guia7.py) | ✅ Completada |
| **Python** | [`guia8.py`](./python/guias/guia8/guia8.py) | TAD Pila (`LifoQueue`), TAD Cola (`Queue`), Diccionarios y Archivos | [`tests_guia8.py`](./python/guias/guia8/tests_guia8.py) | 🔄 En curso (Pilas y Colas) |
| **TP** | [`tp/2c2026_tppython/`](./tp/2c2026_tppython/) | **Trabajo Práctico — Arimaa** (`arimaa.py`, `tests.py`, `cubrimiento.py`) | `unittest` + `coverage` | ✅ Entregado |

---

## 🚫 Funciones permitidas y prohibidas en parciales

> [!IMPORTANT]
> Cualquier función, método o construcción del lenguaje que **no figure explícitamente** en los listados oficiales ([`validas_parcial_hs.pdf`](./validas_parcial_hs.pdf) y [`validas_parcial_py.pdf`](./validas_parcial_py.pdf)) **debe ser implementada manualmente** como función auxiliar. El uso de funciones no permitidas **anula el ejercicio**.

---

### 1. 🟣 Parcial de Haskell ([`validas_parcial_hs.pdf`](./validas_parcial_hs.pdf))

#### ✅ Funciones y operadores permitidos

| Categoría | Funciones / Operadores |
| :--- | :--- |
| **División entera** | `mod :: Integral a => a -> a -> a`<br>`div :: Integral a => a -> a -> a` |
| **Tuplas** | `fst :: (a, b) -> a`<br>`snd :: (a, b) -> b` |
| **Listas** | `(:) :: a -> [a] -> [a]`<br>`(++) :: [a] -> [a] -> [a]`<br>`head :: [a] -> a`<br>`tail :: [a] -> [a]` |
| **Matemáticas y conversión** | `sqrt :: Floating a => a -> a`<br>`fromIntegral :: (Integral a, Num b) => a -> b`<br>`fromInteger :: Num a => Integer -> a`<br>Aritméticas: `+`, `-`, `*`, `/` · Potencia: `**`, `^` |
| **Lógicas y comparación** | `not :: Bool -> Bool`<br>`&&`, `||`, `==`, `/=`, `>`, `<`, `>=`, `<=` |
| **Definiciones locales** | ✔️ Uso de cláusulas `where` |

#### ❌ Construcciones y funciones INVÁLIDAS en Haskell (prohibidas salvo implementación propia)

| Prohibición / Restricción | Alternativa obligatoria en el parcial |
| :--- | :--- |
| ❌ Condicional `if ... then ... else ...` | Usar **guardas** (`\| condicion = ... \| otherwise = ...`) o ***pattern matching*** |
| ❌ Funciones de listas del Prelude: `length`, `elem`, `notElem`, `reverse`, `init`, `last`, `take`, `drop`, `(!!)` | Implementarlas recursivamente usando `head`, `tail` y `(:)` |
| ❌ Orden superior y plegados: `map`, `filter`, `foldr`, `foldl`, `zip`, `any`, `all` | Implementar recursión explícita |
| ❌ Funciones numéricas/comparación: `abs`, `max`, `min`, `even`, `odd`, `gcd`, `lcm`, `sum`, `product`, `maximum`, `minimum` | Implementarlas como funciones auxiliares con guardas y `mod`/`div` |
| ❌ Listas por comprensión (`[x \| x <- xs, ...]`) o rangos (`[1..n]`) | Construir las listas mediante funciones recursivas |

---

### 2. 🐍 Parcial de Python ([`validas_parcial_py.pdf`](./validas_parcial_py.pdf))

#### ✅ Funciones, tipos y métodos permitidos

| Categoría | Elementos permitidos |
| :--- | :--- |
| **Conversión de tipos** | `int`, `list`, `float`, `str`, `tuple`, `bool` |
| **Estructuras de control** | `if` / `elif` / `else`, `while`, `for ... in range(...)`, `for ... in secuencia` |
| **Rango** | `range(i, f, p)` *(con 1, 2 o 3 parámetros)* |
| **Aritméticas** | `+`, `-`, `*`, `/`, `//`, `%`, `sqrt`, `round`, `floor`, `ceil` |
| **Lógicas y comparación** | `and`, `or`, `not`, `==`, `!=`, `>`, `<`, `>=`, `<=` |
| **Secuencias** | Pertenencia: `in` · Concatenación: `+` · Repetición: `*` · Longitud: `len(s)` · Acceso por índice positivo: `s[elem]` |
| **Listas** | `append(e)`, `insert(p, e)`, `remove(e)`, `index(e)`, `count(e)`, `clear()`, `pop()`, `pop(n)`, `copy()` |
| **Diccionarios** | `items()`, `keys()`, `values()`, `pop(clave)`, `clear()` |
| **TAD Pila (`LifoQueue`)** | `from queue import LifoQueue as Pila` → `Pila()`, `put(e)`, `get()`, `empty()` |
| **TAD Cola (`Queue`)** | `from queue import Queue as Cola` → `Cola()`, `put(e)`, `get()`, `empty()` |
| **Archivos** | `open`, `read`, `readline`, `readlines`, `write`, `writelines`, `close`, `os.path.join()`, `os.path.exists()` |

#### ❌ Construcciones y funciones INVÁLIDAS en Python (prohibidas en parcial)

| Prohibición / Restricción | Detalle y alternativa válida |
| :--- | :--- |
| ❌ **Slicing de secuencias** (`s[i:f]`, `s[::-1]`, `s[:]`) | Recorrer con `for` / `while` e índices positivos `s[i]` |
| ❌ **Índices negativos** (`s[-1]`, `s[-i]`) | Usar `s[len(s) - 1]` o `s[len(s) - i]` |
| ❌ **Funciones built-in de agregación/orden** (`max()`, `min()`, `sum()`, `abs()`, `sorted()`, `reversed()`, `enumerate()`, `zip()`, `set()`) | Implementar función auxiliar iterativa |
| ❌ **Métodos de listas no listados** (`.sort()`, `.reverse()`, `.extend()`) | Implementar ordenamiento/inversión manual o usar `.append()` en ciclo |
| ❌ **Métodos de `str`** (`.split()`, `.strip()`, `.replace()`, `.lower()`, `.upper()`, `.join()`, `.find()`) | Recorrer el `str` carácter por carácter con un ciclo |
| ❌ **Métodos de `dict` no listados** (`.get()`, `.update()`, `.setdefault()`) | Verificar pertenencia con `clave in d.keys()` y acceder con `d[clave]` |
| ❌ **Inspección interna de Pila/Cola** (`pila.queue`, `pila.qsize()`) | Desapilar/desencolar en estructura auxiliar con `get()`/`put()` y restaurar el parámetro `in` |
| ❌ **Comprensiones** (`[x for x in s]`, `{k: v for ...}`) y expresiones `lambda` | Inicializar estructura vacía y poblarla con ciclo `for` / `while` |
| ⚠️ **Saltos incondicionales** (`break`, `continue`) | **No recomendados**; controlar la terminación mediante la condición lógica del `while` |
| 📌 **Omisión de tipado estático** | **Obligatorio** anotar tipos en parámetros, retorno de funciones y variables locales |

---

## 🚀 Ejecución rápida

### 🟣 Haskell (GHCi)

```bash
# Cargar una guía o modelo de parcial en el intérprete interactivo
ghci haskell/Practicas/guia5/guia5.hs
```

Comandos útiles dentro de `ghci`:
```haskell
:r          -- Recargar el archivo tras guardar cambios
:t funcion  -- Consultar la signatura de tipos de una función
:q          -- Salir de GHCi
```

### 🐍 Python (Guías y Tests Unitarios)

```bash
# Ejecutar los tests de la Guía 7 (Listas y Matrices)
python3 -m unittest python/guias/guia7/tests_guia7.py -v

# Ejecutar los tests de la Guía 8 (Pilas y Colas)
python3 -m unittest python/guias/guia8/tests_guia8.py -v
```

### ♟️ Trabajo Práctico (Arimaa)

```bash
cd tp/2c2026_tppython

# Ejecutar la suite de tests y medir el cubrimiento
python3 -m unittest tests.py -v
python3 cubrimiento.py
```
