# Métodos de cadenas de caracteres

## Minúsculas/Mayúsculas
```python
>>> cadena_min="una cadena de texto"
>>> cadena_may="CADENA EN MAYÚSCULAS"
>>> cadena_mix="Cadena cOn ToDo mezclado."

>>> print(cadena_min.capitalize())
Una cadena de texto
>>> print(cadena_may.capitalize())
Cadena en mayúsculas
>>> print(cadena_mix.capitalize())
Cadena con todo mezclado.

>>> print(cadena_min.upper())
UNA CADENA DE TEXTO
>>> print(cadena_may.lower())
cadena en mayúsculas
>>> print(cadena_may.casefold())
cadena en mayúsculas

>>> print(cadena_min.title())
Una Cadena De Texto
>>> print(cadena_may.title())
Cadena En Mayúsculas
>>> print(cadena_mix.title())
Cadena Con Todo Mezclado.

>>> print(cadena_mix.swapcase())
cADENA CoN tOdO MEZCLADO.


```

## Otros

```python
>>> cadena="una cadena de texto"
>>> cadmay="OTRA CADENA en MAYÚSCULAS"
>>> cadtab="Cadena\tcon\ttabuladores."
>>> print(cadmay.center(80))
                           OTRA CADENA en MAYÚSCULAS                            
>>> print(cadmay.count('a'))
0
>>> print(cadmay.count('A'))
5
>>> print(cadmay.count('CA'))
1
>>> print(cadmay.encode())
b'OTRA CADENA en MAY\xc3\x9aSCULAS'
>>> print(cadena.endswith('.'))
False
>>> print(cadena.endswith('to'))
True
>>> print(cadena.endswith('ca',4,5))
False
>>> print(cadena.endswith('ca',4,6))
True
>>> print(cadtab.expandtabs(1))
Cadena con tabuladores.

```