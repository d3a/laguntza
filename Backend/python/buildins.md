# Build-ins
```
compile()    Returns the specified source as an object, ready to be executed
divmod()     Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()  Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()       Evaluates and executes an expression
exec()       Executes the specified code (or object)
format()     Formats a specified value
frozenset()  Returns a frozenset object
globals()    Returns the current global symbol table as a dictionary
hash()       Returns the hash value of a specified object
help()       Executes the built-in help system
id()         Returns the id of an object
input()      Allowing user input
len()        Returns the length of an object
locals()     Returns an updated dictionary of the current local symbol table
open()       Opens a file and returns a file object
print()      Prints to the standard output device
property()   Gets, sets, deletes a property
sorted()     Returns a sorted list
```

## zip(lista1, lista2, ...)
Mezcla las listas dadas
```python
l1=[1,2,3,4]
l2=['a','b','c','d']
l3=['AA','BB','CC']

zip(l1,l2,l3)
# ((1,'a','AA')...
```

## map(func, lista)
Aplica la funcion indicada a todos los elementos de la lista
```python
names = ['Ana', 'Juan', 'Maria', 'Jose', 'Rafa']

count_list = list(map(len, names))
print(count_list)
```

## filter(func_filtrado, lista)
Devuelve la lista de los elelmentos que cumplen con la funcion dada
```python
```

## reduce(func_reducir, lista)
Va aplicando la funcion a los elementos de la lista. Empenzando por los dos primeros y luego tommando el resultado y el siguiente elementos.
```python
def func_reducir(prev, elem[, init])
  return x

from functools import reduce

def mayor_reduce(a, b):
    return a if a > b else b

numbers = [1, 12, 3, 34, 45, 68, 25, 14, 26, 78, 96]

max_number = reduce(mayor_reduce, numbers)
print(max_number)
```
