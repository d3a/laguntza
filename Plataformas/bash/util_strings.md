# Utilidades para manupular cadenas

## cut

Procesa líneas separando campos por un delimitador dado.

```cut [-s] -d'<separador>' -f<campos> <fichero>```

```cut -c<caracteres>|-b<bytes> <fichero>```

```-s``` Solo muestra las líneas en las que haya separador

```bash
  VAR1="c1:c2:c3:c4:c5"
  VAR2="123456789"
  
  echo ${VAR1} | cut -d':' -f 1
  # c1
  echo ${VAR1} | cut -d':' -f 1,5
  # c1:c5
  echo ${VAR1} | cut -d':' -f 2-3
  # c2:c3:c4

  echo ${VAR2} | cut -c 2
  # 2
  echo ${VAR2} | cut -c 1,5,7
  # 157
  echo ${VAR2} | cut -c 4-8
  # 45678
``` 

## tr
Manupular caracteres de una cadena de entrada

```tr [-t] [-s] <conjunto1> <conjunto2>```

Sustituye la ocurencias de los carateres en el ```conjunto1``` por el correspondiente carácter del ```conjunto2```. Si el ```conjunto1``` es más largo que ```conjunto2``` este se alarga hasta la longitud de ```conjunto2``` repitiendo el último carácter.

Si se usa ```-t``` el ```conjunto1``` se trunca a la longitud de ```conjunto2```.

Si se usa ```-s``` las secuencias de caracteres repetidos se reducen a un ínico carácter.

```tr -d <conjunto>```
Borrará todas la ocurrencias de los elementos de ```conjunto1```

### Elementos de los conjuntos da sustitución
- ```\n```              new line
- ```\r```              return
- ```\t```              horizontal tab
- ```CHAR1-CHAR2```     todos los caracteres de de CHAR1 a CHAR2 en orden ascendente
- ```[:alnum:]```       todas las letras y dígitos
- ```[:alpha:]```       todas las letras
- ```[:digit:]```       todas los dígitos
- ```[:print:]```       todos los caracteres imprimibles incluyendo espacios
- ```[:blank:]```       espacios en blanco horizontales
- ```[:space:]```       espacios en blanco horizontales o verticales
- ```[:lower:]```       minúsculas
- ```[:upper:]```       mayúsculas

### Ejemplos
```bash
  echo "aaabbbccc" | tr 'a' 'x'
  # xxxbbbccc
  echo "aaabbbccc" | tr 'ab' 'xz'
  # xxxzzzccc
  echo "aaabbbcccddd" | tr 'abd' 'x'
  # xxxxxxcccxxx
  echo "aaabbbcccddd" | tr -s '[:lower:]' '[:upper:]'
  # ABCD
  echo "aaabbbcccddd" | tr -d 'bd'
  # aaaccc
```

## sort

```sort [opciones] [ficheros]```

Ordena lineas

### Opciones más utiles
- ```-f``` no distingue may y min.
- ```-r``` ordena en orden inverso
- ```-u``` imprime una copia de las lineas que se repitan
- ```-n``` comapra valor numerico de la linea, todas las cadenas tienen el mismo valor. Si se pone ```-u``` solo imprime la primera linea no numérica.
- ```-h``` compara numeros <i>human readable</i> (2K, 1G, ...)

## uniq

```uniq [opciones] [entrada [salida]]```

Filtra lineas adjacentes que sean iguales

### Opciones más utiles
- ```-c``` muestra el numero de ocurrencias
- ```-d``` imprime solo las lineas que se repiten
- ```-u``` imprime solo las lineas que no se repiten
- ```-s=n``` ignora los ```n``` primeros caracteres



## wc

```wc [opciones] [fichero]```

Cuenta palabras

### Opciones más utiles
- ```-m``` cuenta caracteres
- ```-w``` cuenta palabras
- ```-l``` cuenta lineas
- ```-L``` anchora maxima

