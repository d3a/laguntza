# Paquetes
```
paquete/
    __init__.py
    subpqt_1/
        __init__.py
        mod_1_1.py
        mod_1_2.py
        mod_1_3.py
    subpqt_2/
        __init__.py
        mod_2_1.py
        mod_2_2.py
        mod_2_3.py
```

```python
import paquete.subpq_1.mod_1_1
paquete.subpq_1.mod_1_1.funcion(a,b,c)

from paquete.subpq_1 import mod_1_1
mod_1_1.funcion(a,b,c)

from paquete.subpq_1.mod_1_1 import funcion
funcion(a,b,c)

from . import modulo_en_la_misma_carpeta
modulo_en_la_misma_carpeta.funcion()
```
