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

## Operar en los elementos
**Filtrar elementos (_filter_)**
```python
def pares(n):
    if divmod(n,2)[1]:
        return False
    else:
        return True

lista = iter(range(20))
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
lista2 = filter(pares, lista)
# 0 2 4 6 8 10 12 14 16 18
```

**Procesar elementos (_map_)**
```python
def doblar(n):
    return n * 2

lista = iter(range(10))
# 0 1 2 3 4 5 6 7 8 9
lista2 = map(doblar, lista)
# 0 2 4 6 8 10 12 14 16 18
```

**Invertir elementos (_reversed_)**
```python
lista = iter(range(10))
# 0 1 2 3 4 5 6 7 8 9
lista2 = reversed(lista)
# 9 8 7 6 5 4 3 2 1
```

**Combinar dos iterables (_zip_)**
```python
lista = iter([1,2,3,4]))
lista2 = iter(['a','b','c','d']))
zip(lista, lista2)
# (1,'a'),(2,'b'),(3,'c'),(4,'d')
```
