# Algoritmos y Estructuras de Datos I (Introducción a la Programación)

Repositorio de prácticas, apuntes de clase, modelos de parcial y trabajo práctico de **Algoritmos y Estructuras de Datos I / Introducción a la Programación** — Departamento de Computación, Facultad de Ciencias Exactas y Naturales (UBA).

---

## 📁 Estructura del repositorio

```text
algoritmos_1/
├── haskell/
│   └── Practicas/
│       ├── guia3/                  # Guía 3: Introducción a Haskell y pattern matching
│       ├── guia4/                  # Guía 4: Recursión sobre números enteros
│       └── guia5/                  # Guía 5: Recursión sobre listas
├── python/
│   └── guias/
│       ├── guia6/                  # Guía 6: Introducción a Python imperativo
│       └── guia7/                  # Guía 7: Listas, matrices y pasaje de parámetros (+ tests)
├── clases/
│   ├── haskell/                    # Código de clases prácticas, simulacros y parciales resueltos
│   │   └── parciales/              # Modelos de parcial (2C2023, 1C2024, 2C2024, 1C2025)
│   └── python/                     # Ejercicios de clase y notas de Python
├── tp/                             # Trabajo Práctico de Python (Arimaa)
├── validas_parcial_hs.pdf          # Listado oficial de funciones permitidas en Haskell
└── validas_parcial_py.pdf          # Listado oficial de funciones permitidas en Python
```

---

## ✅ Funciones permitidas para los parciales

> **Importante:** Cualquier función que no figure en los listados oficiales ([`validas_parcial_hs.pdf`](./validas_parcial_hs.pdf) y [`validas_parcial_py.pdf`](./validas_parcial_py.pdf)) **debe ser implementada manualmente**. El uso de una función no permitida anula el ejercicio.

### 1. Parcial de Haskell ([`validas_parcial_hs.pdf`](./validas_parcial_hs.pdf))

| Categoría | Funciones / Operadores permitidos |
| :--- | :--- |
| **División entera** | `mod :: Integral a => a -> a -> a`<br>`div :: Integral a => a -> a -> a` |
| **Tuplas** | `fst :: (a, b) -> a`<br>`snd :: (a, b) -> b` |
| **Listas** | `(:) :: a -> [a] -> [a]`<br>`(++) :: [a] -> [a] -> [a]`<br>`head :: [a] -> a`<br>`tail :: [a] -> [a]` |
| **Matemáticas y conversión** | `sqrt :: Floating a => a -> a`<br>`fromIntegral :: (Integral a, Num b) => a -> b`<br>`fromInteger :: Num a => Integer -> a`<br>Aritméticas: `+`, `-`, `*`, `/`<br>Potencia: `**`, `^` |
| **Lógicas y comparación** | `not :: Bool -> Bool`<br>`&&`, `||`, `==`, `/=`, `>`, `<`, `>=`, `<=` |

**Aclaraciones de Haskell:**
- ❌ **No está permitido** el uso del condicional `if ... then ... else ...` (utilizar guardas `|` o *pattern matching*).
- ✔️ **Está permitido** el uso de `where`.

---

### 2. Parcial de Python ([`validas_parcial_py.pdf`](./validas_parcial_py.pdf))

| Categoría | Funciones / Estructuras permitidas |
| :--- | :--- |
| **Conversión de tipos** | `int`, `list`, `float`, `str`, `tuple`, `bool` |
| **Estructuras de control** | `if` / `elif` / `else`, `while`, `for ... in range(...)`, `for ... in secuencia` |
| **Rango** | `range(i, f, p)` *(con 1, 2 o 3 parámetros)* |
| **Aritméticas** | `+`, `-`, `*`, `/`, `//`, `%`, `sqrt`, `round`, `floor`, `ceil` |
| **Lógicas y comparación** | `and`, `or`, `not`, `==`, `!=`, `>`, `<`, `>=`, `<=` |
| **Secuencias** | Pertenencia: `in`<br>Concatenación: `+`<br>Repetición: `*`<br>Longitud: `len(s)`<br>Acceso por índice positivo: `s[elem]` |
| **Listas** | `append(e)`, `insert(p, e)`, `remove(e)`, `index(e)`, `count(e)`, `clear()`, `pop()`, `pop(n)`, `copy()` |
| **Diccionarios** | `items()`, `keys()`, `values()`, `pop(clave)`, `clear()` |
| **TAD Pila (`queue.LifoQueue`)** | `from queue import LifoQueue`<br>`pila = LifoQueue()`, `put(e)`, `get()`, `empty()` |
| **TAD Cola (`queue.Queue`)** | `from queue import Queue`<br>`cola = Queue()`, `put(e)`, `get()`, `empty()` |
| **Archivos** | `open`, `read`, `readline`, `readlines`, `write`, `writelines`, `close`, `os.path.join()`, `os.path.exists()` |

**Aclaraciones de Python:**
- ❌ **No está permitido** el uso de *slicing* ni índices negativos (`s[i:f]`, `s[-i]` o similares).
- ⚠️ **No se recomienda** el uso de `break` ni `continue`.
- 📌 **Tipado obligatorio:** Todas las variables y firmas de funciones deben ir anotadas con su tipo correspondiente (`typing`).

---

## 🚀 Uso rápido

### Ejecutar guías o parciales de Haskell
```bash
ghci haskell/Practicas/guia5/guia5.hs
```
Dentro de `ghci`, para recargar cambios tras editar el archivo:
```haskell
:r
```

### Ejecutar guías y tests de Python
```bash
python3 -m unittest python/guias/guia7/tests_guia7.py
```
