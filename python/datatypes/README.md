# Estructuras de Datos

## Tipos de Datos simples
- Secuencias binarias
  - boolean
  - byte
  - bytearray
  - memoryview
- Numéricos
  - int
  - float
  - complex
  - range
- Cadenas de carateres
  - str
    - [Métodos](https://www.w3schools.com/python/python_ref_string.asp) :arrow_upper_right:


## Tipos de Datos complejos

| Datatype     | Constructor |    | Unico     | Varios                     | Idx | Dup | Mut |
|:-------------|:------------|:---|:----------|:---------------------------|:----|:----|:----|
| lista        | `list()`    | [] | [elem]    | [elem1, elem2, ..., elemN] | int | :ballot_box_with_check: | :ballot_box_with_check:  |
| tupla        | `tuple()`   | () | (elem,)   | (elem1, elem2, ..., elemN) | int | :ballot_box_with_check: | :x: |
| diccionario  | `dict()`    | {} | {key:val} | {k1:v1, k2:v2, ..., kN:vN} | key | :x: | :ballot_box_with_check:  |
| conjunto     | `set()`     | -- | {elem}    | {elem1, elem2, ..., elemN} | :x: | :x: | :ballot_box_with_check:  |

- [Listas](listas.md)
  - [Declarar Listas](listas.md#declarar-listas)
  - [Recorrer Listas](listas.md#recorrer-listas)
  - [Acceder a los Elementos de una Lista](listas.md#acceder-a-los-elementos-de-una-lista)
  - [Operar con Listas](listas.md#operar-con-listas)
  - [Métodos de Listas](https://www.w3schools.com/python/python_ref_list.asp) :arrow_upper_right:
  - [Ejemplos](https://github.com/d3a/laguntza/blob/main/python/datatypes/code/listas.py) :arrow_upper_left:
- [Tuplas](tuplas.md)
  - [Declarar Tuplas](tuplas.md#declarar-tuplas)
  - [Métodos](https://www.w3schools.com/python/python_ref_tuple.asp) :arrow_upper_right:
- [Diccionarios](diccionarios.md)
  - [Declarar Diccionarios](diccionarios.md#declarar-diccionarios)
  - [Métodos](https://www.w3schools.com/python/python_ref_dictionary.asp) :arrow_upper_right:
- [Conjuntos](conjuntos.md)
  - [Declarar Conjuntos](conjuntos.md#declarar-conjuntos)
  - [Operaciones de Conjuntos](conjuntos.md#operaciones-de-conjuntos)
  - [Métodos](https://www.w3schools.com/python/python_ref_set.asp) :arrow_upper_right:
  - [Ejemplos](https://github.com/d3a/laguntza/blob/main/python/datatypes/code/conjuntos.py) :arrow_upper_left:

## Estructuras de Datos
[Código](https://github.com/d3a/laguntza/blob/main/python/datatypes/code/)
- [Árboles](https://github.com/d3a/laguntza/blob/main/python/datatypes/code/Arboles.py)
- [Colas](https://github.com/d3a/laguntza/blob/main/python/datatypes/code/Colas.py)
- [Pilas](https://github.com/d3a/laguntza/blob/main/python/datatypes/code/Pilas.py)
