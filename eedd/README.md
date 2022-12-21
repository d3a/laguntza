# Estructuras de Datos
[Arrays](arrays)

## [Arrays][arrays]
Los arrays de Python se llaman _listas_ (elementos editables) o _tuplas_ (elementos no editables).

```python
  lista = list()
  lista = [1, 2, 3, 4]
```

Los elementos pueden ser de cualquier tipo:
```python
  lista = list()
  for i in range(1, 5)
    obj = Objto()
    lista.append(obj)
```

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
    print( f'Lista[{i}]: {lista[i]}' )
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
