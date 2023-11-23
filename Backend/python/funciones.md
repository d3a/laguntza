# Funciones

```python
def funcion():
  pass

def funcion(param1, param2, ...):
  v1 = param1
  v2 = param2
  pass
```

Parametros de entrada ala funciones en una lista
```python
def funcion(*args):
  v1 = args[0]
  v2 = args[1]

fun(1, 2, 3, ...)
```

Parametros de entrada ala funciones en un diccionario
```python
def funcion(**kwargs):
  a = kwargs['a']
  b = kwargs['b']

fun(a=1, b=2)
```


## Generadores
```python
def generador(n):
  yield 1
  yeild 2
  ....

a = generador()
next(a)
```
