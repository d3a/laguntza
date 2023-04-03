# Arrays

## Asignacion de Arrays

```bash
$ array=( cero uno dos tres cuatro )
$ array=( [0]=cero [1]=uno [2]=dos [3]=tres [4]=cuatro )
$ array[0]=cero
$ array[1]=uno
$ array[2]=dos
$ array+=( nuevo_elemento )
```

## Lectura de Arrays

```${array[@]}```	Escribe todo el array

```${array[*]}```	Escribe todo el array

```${array[0]}```	Escribe el primer elemento del arrays

```${array[1]}```	Escribe el segundo elemento del arrays

```${#array[@]}```	Escribe el número de elementos del array

```${#array[*]}```	Escribe el número de elementos del array

```${#array[0]}```	Escribe el número de caracteres del primer elemento del array

```${#array[1]}```	Escribe el número de caracteres del segundo elemento del array

```${array[@]:1:2}```	Muestra los elementos del 1 al 2 del array

```${!array[@]}```	

## Recorrer un array
```bash
for index in $(seq 0 $((${#array[@]} - 1))); do
  ${array[${index}]}
done
```
