# Módulos

## Comandos
- command # default
    - Módulo por defecto. Se puede cambiar en ```ansible.cfg```
    - No admite _pipes_ ni redirecciones
- shell
- raw
- script

## Paquetes
- package
- apt
- yum
- dnf

## Ficheros

### Búsqueda
- find

### Gestion
- file
  - path: ruta del fichero
  - owner
  - group
  - mode
  - recurse: para carpetas
  - src: para enlaces
  - state: acción
    - absent -> que no exista
    - directory -> que sea una carpeta
    - file -> que sea un fichero
    - hard -> que sea un enlace 
    - link -> qe sea un enlace simbólico
    - touch -> tocar

### Copia de Ficheros
- copy
- template

