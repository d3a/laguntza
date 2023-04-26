# Métodos de cadenas de caracteres

## Información sobre la cadena
```python
cadena="una cadena de texto"
```

**Contar ocurrencias de una subcadena dentro de la cadena**
```python
cadena.count('de')
# 1
```

**Buscar subcadena**
```python
#La primera ocurrencia
cadena.index('de')
# 6
cadena.find('de')
# 6
#La última ocurrencia
cadena.rindex('de')
# 11
cadena.rfind('de')
# 11
```

**Verificar si la cadena empieza o termina en una subcadena determinada**
```python
cadena.startswith('Una')
# False
cadena.startswith('una')
# True
cadena.startswith('una',0,10)   # Se puede especificar un rango 
# True

cadena.endswith('.')
# False
cadena.endswith('na')
# True
```

**Verificar si tiene formatos determinados**
```python
"aplha_²_123".isprintable()
# True
"aplha_?_123".isascii()
# True
"aplha__123".isidentifier()
# True
"alpha123".isalnum()
# True
"alpha".isalpha()
# True
"  \t".isspace()
# True

"1234".isdecimal()
# True
"1234²".isdigit()
# True
"1234¾²".isnumeric()
# True
 
"Titulo Valido".istitle()
# True
"todo  minus".islower()
# True
"TODO MAYUS".isupper()
# True
```

## Minúsculas/Mayúsculas

```python
cadena_min="una cadena de texto"
cadena_may="CADENA EN MAYÚSCULAS"
cadena_mix="Cadena cOn ToDo mezclado."
```

**Primera letra en mayúsculas**
```python
cadena_min.capitalize()
# Una cadena de texto
cadena_may.capitalize()
# Cadena en mayúsculas
cadena_mix.capitalize()
# Cadena con todo mezclado.
```

**Primera letra de cada palabra en mayúsculas**
```python
cadena_min.title()
# Una Cadena De Texto
cadena_may.title()
# Cadena En Mayúsculas
cadena_mix.title()
# Cadena Con Todo Mezclado.
```

**Todo en mayúsculas**
```python
cadena_min.upper()
# UNA CADENA DE TEXTO
```

**Todo en minúsculas**
```python
cadena_may.lower()
# cadena en mayúsculas
cadena_mix.casefold()
# cadena con todo mezclado.
```

**Cambiar mayúsculas por minúsculas y minúsculas por mayúsculas**
```python
cadena_mix.swapcase()
#cADENA CoN tOdO MEZCLADO.
```

## Transformar una cadena
**Crear cadena desde iterable**
```python
lista=('1','2','3','4')
separador="-"
separador.join(lista)
# '1-2-3-4'
```

**Dividir cadena**
```python
cadena="1-2-3-4"
cadena.split("-",2)
# ['1', '2', '3-4']
cadena.rsplit("-",2)
# ['1-2', '3', '4']

cadena= "Linea1\rLinea dos\n3ra linea"
cadena.splitlines()
# ['Linea1', 'Linea dos', '3ra linea']

cadena="una cadena xx con una linea xx dentro"
cadena.partition('xx')
# ('una cadena ', 'xx', ' con una linea xx dentro')
cadena.rpartition('xx')
# ('una cadena xx con una linea ', 'xx', ' dentro')
```

**Justificar**
```python
cadena="12345"

cadena.ljust(10)
# '12345     '
cadena.rjust(10,'_')
# '_____12345'
cadena.center(20,'-')
# '-------12345--------'

cadena.zfill(10)
# '0000012345'
```

**Eliminar caracteres al principio y/o al final**
```python
cadena="   Cadena   "
cadena.rstrip()
# '   Cadena'
cadena.strip()
# 'Cadena'
cadena.lstrip()
# 'Cadena   '
```

**Reemplazar**
```python
cadena="un texto que vamos a cambiar"

cadena.replace('vamos a', 'tenemos que')
# 'un texto que tenemos que cambiar'
```

## Otros

```python
"áéñçÍÓ".encode()
# b'\xc3\xa1\xc3\xa9\xc3\xb1\xc3\xa7\xc3\x8d\xc3\x93'

"cadena\tcon\ttabuladores".expandtabs()
# 'cadena  con     tabuladores'

"cadena con {var1} y una {var2}".format(var1 = "variable", var2 = "segunda variable")
# 'cadena con variable y una segunda variable'

tabla_trans = str.maketrans("12345", "67890", "ABCD")
"1A2B3C4D5: 67890".translate(tabla_trans)
# '67890: 67890'
```