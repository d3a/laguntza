# Gestión de ficheros

## Texto  plano
```python
from io import open

# Abrir
file_handler = open(ruta_fichero, modo, newline = ''', encoding='UTF-8')
  #modos: r, w, a, x

# Posicionar el puntero
file_handler.seek(caracteres)
  
# Leer
texto = file_handler.read([caracteres])
lista = file_handler.readlines()

# Escribir
file_handler.write(datos)

# Cerrar
file_handler.close()
```

```python
from io import open

# Abrir
with open(ruta_fichero, modo) as file_handler
  # Tratar el fichero
```


## CSV

### Lectura
```python
from io import open
import csv

with open('some.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

with open(file_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['campo'])
```

### Escritura
```python
from io import open
import csv

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
myFile = open('example2.csv', 'w')
writer = csv.writer(myFile)
writer.writerows(myData)
myFile.close()
print("Writing complete")


csvfile = open('example.csv', 'w')
fieldnames = ['first_name', 'last_name', 'Grade']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
```



## JSON

### Lectura
```python
from io import open
import json

f = open(filename, 'r')
dict = json.load(f)
```

### Escritura
```python
from io import open
import json

f = open(filename, 'w')
dict = json.dumps(f)
```
