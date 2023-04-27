# Tipos numéricos

## Enteros

```python
entero=int()
# 0
entero=int(65)
# 65
entero=int('65')
# 65
entero=int(6.5)
# 65
entero=int(0b11)
# 3
entero=int('11',2)
# 3
entero=int(0o77)
# 63
entero=int('77',8)
# 63
entero=int(0xAA)
# 170
entero=int('AA',16)
# 170
```

## Reales

```python
real=float()
# 0.0
real=float(65)
# 65.0
real=float(6.5)
# 6.5
real=float(6.5E2)
# 650.0
real=float('6.5E2')
# 650.0
```

## Complejos

```python
img=complex()
# 0j
img=complex(3)
# (3+0j)
img=complex(3,5)
# (3+5j)
img=complex(3+5j) 
# (3+5j)
img=complex('3+5j') 
# (3+5j)
```

## Rangos

```python
rango=range(10)
# 0 1 2 3 4 5 6 7 8 9
rango=range(1,10)
# 1 2 3 4 5 6 7 8 9
rango=range(1,10,3)
# 1 4 7
```

# Cambios de Base
```python
binario=bin(989)
# '0b1111011101'
octal=oct(989)
# '0o1735'
haxadecimal=hex(989)
# '0x3dd'
```

## Funciones
```python
entero=abs(7)
# 7
entero=abs(-7)
# 7
real=abs(-7.5)
# 7.5

numero=round(7.5)
# 8
numero=round(7.455)
# 7
numero=round(7.455,2)
# 7.46

numero=pow(3,2)
# 9
numero=pow(3.3,2.2)
# 9
numero=pow(3.3,2.2)
# 13.827086118044146
numero=pow(3+3j,2)
# 18j
numero=pow(3+3j,2+2j)
# (-0.9301698201642012-3.6243749286074007j)
```
