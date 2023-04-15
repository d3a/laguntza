# Variables

## Asignacion de Variables

```bash
$ variable=cadena

$ variable='cadena'

$ variable="cadena"

$ read -r -d '' VAR << EOM
This is line 1.
This is line 2.
Line 3.
EOM

$ read VAR < fichero-entrada
```

## Variables predefinidas

```bash
    $?	# Código de salida del ultimo comando ejecutado
    $_  # Último argumento del comando anterior
    $-  # option flags establecidas para el proceso en curso
    $#	# Número de parámetros entregados
    $*  # Argumentos del comando, "$*" = "$1 $2 $3 ..."
    $@  # Argumentos del comando, "$@" = "$1" "$2" "$3" "..."
    $$	# PID del proceso en ejecución
    $!	# PID del proceso en background
```

## Modificadores de Variables

```${parameter}```	Variable Normal

```${parameter:-word}```	Devuelve word si parameter no está definido o es nulo.

```${parameter:=word}```	Asigna el valor de word a parameter si parameter no está definido o es nulo.

```${parameter:?word}```	Muestra word en la salida de error si parameter no está definido o es nulo.
	
```${parameter:+word}```	Si parameter no está definido o es nulo no devuelve nada, en caso contrario devuelve word .

```${parameter:offset[:length]}``` Substring. Si offset es negativo, se corta desde atrás.

```${!nombre_variable}``` Muestra el contenido de la variable cuyo nombre sea el contenido de la variable indicada.

```bash
$ variable="Contenido"
$ nombre_variable=variable
$ echo ${!nombre_variable}
Contenido
```

```${!patron*}``` ```${!patron@}```	Muestra los nombres de la variables que empiezan por 'patron', IFS define el separador de la lista.
	
```${#parameter}```	Numero de caracteres o elementos del array

```${parameter#word}``` ```${parameter##word}``` Se expande 'word' como una patrón de expanción de rutas (*,?,...). Si hay coincidencia con el principio del parametro el resultado será el parametro con la parte coincidenctra borrada. Si se usa # se usará el patron mas pequeño, si se usa ## se usará el patrónm ás largo.
```bash
    var="uno-dos-tres"
    echo ${var#*-}
    # dos-tres; el patron mas corto que cumple es "uno-"
    echo ${var##*-}
    # tres; el patron mas corto que cumple es "uno-dos-"
```

```${parameter%word}``` ```${parameter%%word}``` Igual que antes pero por detrás
```bash
    var="uno-dos-tres"
    echo ${var%-*}
    # uno-dos; el patron mas corto que cumple es "-tres"
    echo ${var%%-*}
    # uno; el patron mas corto que cumple es "-dos-tres"
```

```${parameter/pattern/string}```	Sustitucion parecida a expresiones regulares. Si patron empeiza por # se aplica al principio. Si empeiza por % se aplica al final. Si empeiza por / se sustuyen todas la ocurrencias.
```bash
    var="uno-dos-tres"
    echo ${var/#u/U}
    # Uno-dos-tres
    echo ${var/%tres/3}
    # uno-dos-3
    echo ${var/-/}
    # unodos-tres
    echo ${var//-/;}
    # uno;dos;tres
```

```${variable^}```	A mayúsculas el primer carácter

```${variable^^}```	Todo a mayúsculas

```${variable,}```	A minúsculas primer carácter

```${variable,,}```	Todo a minúsculas 

## Ejemplos práticos
Descomponer un nombre de fichero
```bash
    files=data.txt
    echo ${file%.*}
    # data
    echo ${file#*.}
    # txt
```	

Host Corto
```bash
    ${HOSTNAME%%.*}
```
