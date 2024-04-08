# Excepciones

## Captura de Excepciones

```python
try:
  # codigo
except ZeroDivisionError:
  # codigo si hay division por cero
except TypeError:
  # codigo si hay error de tipos
except Excepcion as alias:
  # inst.args

except:
  # cualquier otra excepcion
else:
  # codigo si no hay errores
finally:
  # codigo que se ejecutará siempre

```

## Elevar 
```python
raise Exception[('mensaje')]
```

## Crear Excepciones
Se suelen integrar en un fichero "errors.py" o "exceptions.py"
```python
class Error(Exception):
  # Clase base para nuestras excepciones
  pass
class ExcepcionPersonalizadaError(Error):
  # Una clase personalizada
  pass
class OtraExcepcionPersonalizadaError(Error):
  # Otra clase personalizada
  pass
```
