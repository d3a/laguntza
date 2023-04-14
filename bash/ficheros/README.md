# Gestion de ficheros

**Rutas y nombres**

```dirname``` y ```basename```
```bash
  file="/mnt/unidad/carpeta/fichero.txt"
  dirname ${file}
  # /mnt/unidad/carpeta
  basename ${file}
  # fichero.txt
  basename ${file} ".txt"
  # fichero
  
  
  file="data.ext"
  echo ${file%.*}
  # data
  echo ${file#*.}
  # ext
```

[Filesystems](filesystems.md)

[Carpetas](carpetas.md)

## Ficheros
- cp
- mv
- rm
- touch
- cat
- more
- less

## Utilidades
- du
- fuser
- lsof
