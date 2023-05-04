# Funciones sobre Iterables

## Creación y recorrido 

**Listas**
```python
    # Desde una Lista
    iterador = iter([1,2,3,4])
    # Desde una tupla
    iterador = iter((1,2,3,4))
    # Desde un conjunto
    iterador = iter({1,2,3,4})
    next(iterador)
    # 1
    next(iterador)
    # 2
```

**Diccionario**
```python
    iterador = iter({"a":1,"b":2,"c":3})
    next(iterador)
    # 'a'
    next(iterador)
    # 'b'
```

## Contar elementos

**Consultar ciertos**
```python
    lista = iter(('a','b','c','d'))
    len(lista)
    # 4
```

## Operar con los elementos

**Consultar ciertos**
```python
    lista = iter(("","1","2"))
    all(lista)  # True si todos True
    # False
    any(lista)  # True si alguno True
    # True
    lista = ("","1","2")
```

**Máximo y mínimo**

Tras la ejecución de min o max el iterador se "vacía", es decir, esas funciones lo recorren y dejan el puntero al final
```python
    lista = iter((1,2,3,4,9,4,5))
    max(lista)
    # 9
    lista = iter((1,2,3,4,9,4,5))
    min(lista)
    # 1
```

**Sumar elementos**
```python
    l=iter(range(10))
    sum(l)
    # 45
```

filter()	Use a filter function to exclude items in an iterable object
map()	Returns the specified iterator with the specified function applied to each item
reversed()	Returns a reversed iterator
zip()	Returns an iterator, from two or more iterators