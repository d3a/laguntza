# Estructuras de Datos
- [Listas](#listas)
  - [Declarar Listas](#declarar-listas)
  - [Recorrer Listas](#recorrer-listas)
- [Tuplas](#tuplas)
  - [Declarar Listas](#declarar-tuplas)


## Listas
Las  _listas_ son como los _arrays_ de otros lenguajes. Adminten cualquier tipo de dato.

### Declarar Listas
```python
  lista = list()
  lista = [1, 2, 3, 4]
```
Los elementos pueden ser de cualquier tipo:
```python
  lista = list()
  for i in range(1, 5)
    obj = Objeto()
    lista.append(obj)
```

#### Recorrer Listas
```python
lista = [1, 2, 3, 4]
for elem in lista:
    print( f'Elemento: {elem}' )
```
```python
lista = [1, 2, 3, 4]
for i in range( 0, len(lista) ):
    print( f'Lista[{i}]: {lista[i]}' )
```
```python
lista = [1, 2, 3, 4]
for i, elem in enumerate(lista):
    print( f'Lista[{i}]: {elem}' )
```
```python
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
for elem1, elem2 in zip(list1, list2):
    print( f'{elem1}: {elem2}' )
```
```python
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
for i, elem in enumerate(zip(list1, list2)):
    print( f'list1[{i}]: {elem[0]}; list2[{i}]: {elem[1]}' )
```

#### Acceder a los Elementos de una Lista
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
| Elemento     | Descripción                                                | Ejemplo
| :----------- | :--------------------------------------------------------- | :------------------------- |
| lista[n]     | Devuelve n-esimo elemento de la lista                      | `lista[2]` -> 3   |
| lista[-n]    | Devuelve n-esimo elemento de la lista empezando por detrás | `lista[-1]` -> 4  |
| lista[:]     | Devuelve una **copia** de la lista                         | `lista[:]` -> [1, 2, 3, 4, ...] |
| lista[:m]    | Devuelve m elementos empezando por el principio            | `lista[:2]` -> [1, 2] |
| lista[n:]    | Devuelve todos los elementos desde el n-esimo              | `lista[7:]` -> [8, 9, 10] |
| lista[n:m]   | Devuelve m elementos empezando por el n-esimo              | `lista[1:2]` -> [2, 3] |
| lista[n:<zero-width space>m:p] | Devuelve m elementos empezando por el n-esimo tomando de p en p | `lista[1:8:2]` -> [2, 4, 6, 8] |
| a, b, c, d = lista | la lista debe tener exactamente el mismo númer ode elementos como variables haya en la asignación | 

Nota: el primer elemento de toda lista está indexado en el 0.

#### Operar con Listas
```python
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = ['A', 'B']
```

| Operacion    | Descripción                                                            | Ejemplo
| :----------- | :--------------------------------------------------------------------- | :------------------------- |
| lista        | Devuelve puntero a la lista                                            | `lista = list1` -> _lista_ apunta a losm mismos datos que _list1_ |
| lista[:]          | Devuelve un lista con todos los elementos de lista                     | `lista = list1` -> _lista_ es una lista diferente a _list1_ pero con los mismos elementos |
| lista1+lista2     | Devuelve un lista con todos los elementos de ambas listas           | `lista = list1 + list2` -> [1, 2, 3, 4, 'a', 'b', 'c', 'd']
| lista * n         |  Devuelve un lista con todos los elementos repetidos n veces              | `list3 * 3` -> ['A', 'B', 'A', 'B', 'A', 'B']
| elemento in lista | Devuelve _True_ si el _elemento_ está incluido en la lista        | `2 in list1` -> True
| elemento not in lista | Devuelve _True_ si el _elemento_ NO está incluido en la lista | `2 not in list2` -> True
| len(lista)   | Devuelve el número total de elemtnos en la lista           | `len(list1)` -> 4 |
| min(lista)   | Devuelve el el elemento manor de la lista           | `min(list1)` -> 4 |
| max(lista)   | Devuelve el el elemento mayor de la lista           | `max(list1)` -> 4 |
| del(lista[n:m] | elimina de las lista los elementos del n-esimo a m-esimo. | `del(list1[1,3])` -> [1, 4] |

#### Métodos de Listas
```python
lista = [1, 2, 3]
```
| Método                | Descripción                                                            | Ejemplo
| :-------------------- | :--------------------------------------------------------------------- | :------------------------- |
| clear()               | | |
| copy()                | | |
| index(elem[, i[, j]]) | | |
| count()               | | |
| append(elem)          | | |
| pop([i])              | | |
| insert(i, elem)       | | |
| remove(elem)          | | |
| extend(lista)         | | |
| reverse()             | | |
| sort()                | | |


## Tuplas
Las  _tuplas_ son como los _listas_ pero sus elementos no puden ser modificados.

### Declarar Tuplas
```python
  tupla = tuple()
  tupla = (1, 2, 3, 4)
```
Los elementos pueden ser de cualquier tipo:
```python
  tupla = tuple()
  for i in range(1, 5)
    obj = Objeto()
    tupla.append(obj)
```
