# Conjuntos

## Declarar Conjuntos
```python
  cto = {1, 2, 3}
  cto = set([lista  | tupla])
```
Los elementos deben ser objetos _hashables_:
```python
  lista = [1, 2, 3]
  tupla = ('A', 'B', 'C')
  cto = set()
  cto.add(lista)  # Error ya que una lista no es hashable
  cto.add(tupla)  # No da error porque las tuplas son hashables si sus elementos lo son
```

## Operaciones de Conjuntos
```python
set = {1, 2, 3}
```

| Método                | Descripción                                                            | Ejemplo
| :-------------------- | :--------------------------------------------------------------------- | :------------------------- |
| elem in cto1          | `True` si elem en cto1      | |
| cto1 \| cto2          | Union de cto1 y cto2        | |
| cto1 & cto2           | Intersección de cto1 y cto2 | |
| cto1 - cto2           | Elementos de cto1 que no están en cto2. La operación no es conmutatiuva.         | |
| cto1 ^ cto2           | Elementos de que no son comunes entre cto1 y cto2. La operación es conmutatiuva. | |

## Métodos de Conjuntos

```python
set = {1, 2, 3}
```

| Método                | Descripción                                                            | Ejemplo
| :-------------------- | :--------------------------------------------------------------------- | :------------------------- |
| clear()               | | |
| add(elem)             | | |
| update(lista)         | | |
| remove(elem)          | Elimina el elemento _elem_. Si el elemento no existe lanza excepcion _KeyError_ | |
| discard(elem)         | Elimina el elemento _elem_. Si el elemento no existe no se lanza excepcion      | |
| union(cto2)           | Igual que `cto1 \| cto2` | |
| intersection(cto2)    | Igual que `cto1 & cto2` | |
| difference(cto2)          | Igual que `cto1 - cto2` | |
| symetric_difference(cto2) | Igual que `cto1 ^ cto2` | |
| isdisjoint(cto2) | `True` si no hay elementos comunes | |
| issubset(cto2) | `True` si todos los elementos de cto1 están dentro de cto2 | |
| issupperset(cto2) | `True` si cto1 contiene todos los elementos cto2 | |

