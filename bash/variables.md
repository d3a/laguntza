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

```${parameter#word}``` ```${parameter##word}```	The word is expanded to produce a pattern just as in pathname expansion.  If the pattern matches the beginning of the value  of  parameter, then  the  result  of  the  expansion is the expanded value of parameter with the shortest matching pattern (the ''#'' case) or the longest matching pattern (the ''##'' case) deleted.  If parameter is @ or *, the pattern removal operation is applied to each positional  parameter in turn, and the expansion is the resultant list.  If parameter is an array variable subscripted with @ or *, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

```${parameter%word}```	The word is expanded to produce a pattern just as in pathname expansion.  If the pattern matches a trailing portion of the  expanded  value of  parameter,  then  the result of the expansion is the expanded value of parameter with the shortest matching pattern (the ''%'' case) or the longest matching pattern (the ''%%'' case) deleted.  If parameter is @ or *, the pattern removal operation is  applied  to  each  positional  parameter in turn, and the expansion is the resultant list.  If parameter is an array variable subscripted with @ or *, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.
```${parameter%%word}```

```${parameter/pattern/string}```	The pattern is expanded to produce a pattern just as in pathname expansion.  Parameter is expanded and the longest match of pattern against its  value  is  replaced with string.  If Ipattern begins with /, all matches of pattern are replaced with string.  Normally only the first match is replaced.  If pattern begins with #, it must match at the beginning of the expanded value of parameter.  If pattern begins with %, it must match at the end of the expanded value of parameter.  If string is null, matches of pattern are deleted and the / following pattern may be omitted.  If parameter is @ or *, the substitution operation is applied to each positional parameter in turn, and the  expansion  is the resultant list.  If parameter is an array variable subscripted with @ or *, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list.

```${variable^}```	A mayúsculas el primer carácter

```${variable^^}```	Todo a mayúsculas

```${variable,}```	A minúsculas primer carácter

```${variable,,}```	Todo a minúsculas 

##Ejemplos práticos
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
