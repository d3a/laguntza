# Carpetas
Mostrar carpeta actual (-P resuelve enlaces simbólicos):
```bash
$ pwd [-P]
```
Crear carpeta (-p crea también las intermedias):
```bash
$ mkdir [-p] /ruta/a/la/carpeta
```
Ir a carpeta (si no se pone nada lleva a $HOME):
```bash
$ cd [/ruta/a/la/carpeta]
```
Borrar carpeta (-p borra los ancestros), solo funciona si las carpetas están vacías:
```bash
$ rmdir /ruta/a/la/carpeta
```
Borrar carpeta y todo su contenido:
```bash
$ rm -r /ruta/a/la/carpeta
```

Arbol de carpetas:
```tree [opts] [ruta]```

- -d       Solo carpetas
- -l       Links simbólicos
- -L level

```bash
$ tree /ruta/a/la/carpeta
/ruta/a/la/carpeta
├── bin
│   ├── script -> ../scripts/script.sh
│   ├── link2 -> /ruta/a/links2
│   └── link3 -> /ruta/a/links3
├── data
│   ├── sub1
│   │   ├── fich1.1
│   │   ├── fich1.2
│   │   └── fich1.3
│   └── sub2
│       ├── fich2.1
│       └── fich2.2
└── scripts
    └── script.sh
```
