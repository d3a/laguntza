# Estructuras de control

## Condicionales

### if
```if list; then list; [ elif list; then list; ] ... [ else list; ] fi```

```bash	
	if condicion; then
		-- bloque para condicion --
	elif condicion2; then
		-- bloque para condicion 2 --
	else
		-- bloque por defecto --
    fi
```

###case
```case word in [ [(] pattern [ | pattern ] ... ) list ;; ] ... esac```

```bash	
	case ${variable} in
		"valor")
			-- bloque para valor --
			;;
		"valor2" | "v2")
			-- bloque para valor 2, dos posibles valres con el mismo bloque --
			;;
		*)
			-- bloque por defecto --
			;;
	esac
```


## Bucles

### for
```for name [ in word ] ; do list ; done```

```bash
	for host in maquina1 maquina2 maquina3; do
	    ssh ${host} "<acciones>; <acciones>; ..."
	    scp ${host}:/fichero .
	done
```

```for (( expr1 ; expr2 ; expr3 )) ; do list ; done```

### while/until
```while list; do list; done```

```until list; do list; done```



## Condiciones
```test <comparacion>```

```[ <comparacion> ]```
- Las comparaciones se acumulan con "-a" (and) y "-o" (or).

- Expande nombres de ficheros:

	```[ -e *.sh ]```: Devuelve cierto si hay un fichero con extensión "sh". Si hay varios dará error

```[[ <comparacion> ]]```
- Las comparaciones se acumulan con "&&" (and) y "||" (or).
- Permite shell globbing:

	```[[ "$cadena" == *[aA]bc* ]]``` Cadena puede ser cualquier cadena que contenga "Abc" o "abc".
	
- Evita separado de palabras. No es necesario poner comillas en las variables, pero sigue siendo una buena práctica.
- No expande nombres de ficheros:

	```[[ -e *.sh ]]```: Devuelve cierto si y solo si existe el fichero "*.sh".

- Permite comparaciones de patrones regex mediante el operador “=~"
	
```(( <comparacion> ))```
- Solo comparaciones numéricas.
- Las comparaciones se acumulan con "&&" (and) y "||" (or).


### Condiciones con cadenas
Operador	Verdad ( valor TRUE )  si
caena1=cadena2	cadena1 es igual a cadena2
cadena1!=cadena2	cadena es diferente a cadena2
cadena1<cadena2	cadena1 es menos que cadena2
cadena1>cadena2	cadena1 es mayor que cadena2
-n cadena1	cadena1 no es nula (longitud mayor que 0)
-z cadena1	cadena1 tiene un valor nulo (longitud 0)

### Condiciones numéricas
Operador	Verdad ( valor TRUE )  si
varx -lt vary	varx menor que vary
varx -le vary	varx menos o igual que vary
varx -eq vary	varx igual que vary
varx -ge vary	varx mayor o igual que vary
varx -gt vary	varx mayor que vary
varx -ne vary	varx diferente que vary

### Condiciones con ficheros
Operador	Verdad ( valor TRUE )  si
-a fichero	Fichero existe (cualquier tipo)
-b fichero	Fichero existe y es un fichero especial de bloques
-c fichero	Fichero existe y es un fichero especial de caracteres
-d fichero	Fichero existe y es un directorio
-e fichero	Fichero existe (cualquier tipo) (igual que -a)
-f fichero	Fichero existe y es un fichero regular (no un directorio, u otro tipo de fichero especial)
-r fichero	Tienes permiso de lectura en fichero
-s fichero	Fichero existe y no esta vacío
-w fichero	Tienes permiso de escritura en fichero
-x fichero	Tienes permiso de ejecución en fichero (o de búsqueda si es un directorio)
-L fichero	El fichero es un link simbólico
-O fichero	Eres el dueño del fichero
-G fichero	El grupo del fichero es igual al tuyo
fichero1 -nt fichero2	Fichero1 es más reciente que fichero2
fichero1 -ot fichero2	Fichero1 es más antiguo que fichero2

