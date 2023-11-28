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


## Decoradores
```python
def funcion_decoradora(funcion_entrada):
  def nueva_funcion(a,b):
    # Se hacen cosas antes
    res = funcion_entrada(,a,b)
    # Se hacen otras cosas después
    return res
  return nueva_funcion

@funcion_decoradora
def funcion_decorada(a,b)
  pass
```

### Decoradores con paramtros
```python
def encapsulador(paramtro_decorador)
  def funcion_decoradora(funcion_entrada):
    def nueva_funcion(a,b):
      # Se hacen cosas antes
      res = funcion_entrada(,a,b)
      # Se hacen otras cosas después
      return res
    return nueva_funcion
  return funcion_decoradora

@funcion_decoradora( parametro )
def funcion_decorada(a,b)
  pass
```


## Funciones lambda
```python
lambda [params]: operacion

lambda x,y: x+y

a = lambda x,y: x+y
print(a(1,2))
```

