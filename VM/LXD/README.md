# LXD/LXC

## Home
- [Linux Containers](https://linuxcontainers.org/)
- [LXD Docs](https://linuxcontainers.org/lxd/docs/latest/)

## Comandos
**lxd**: demonio
**lxc**: cliente

## Instalación
```bash
snap install lxd
lxd init
lxd --version
```

## Consultas

### Plantillas

```bash
$ lxc image list
+---------------+--------------+--------+--------------------------------------+--------------+-----------+----------+-----------------------------+
|     ALIAS     | FINGERPRINT  | PUBLIC |             DESCRIPTION              | ARCHITECTURE |   TYPE    |   SIZE   |         UPLOAD DATE         |
+---------------+--------------+--------+--------------------------------------+--------------+-----------+----------+-----------------------------+
| Ubuntu2204SSH | 5721dd0e330c | no     | Ubuntu 22.04 LTS server (20221101.1) | x86_64       | CONTAINER | 602.55MB | Nov 8, 2022 at 8:05am (UTC) |
+---------------+--------------+--------+--------------------------------------+--------------+-----------+----------+-----------------------------+
```

### Contenedores
```bash
$ lxc list
+------------+---------+------+------+-----------+-----------+
|    NAME    |  STATE  | IPV4 | IPV6 |   TYPE    | SNAPSHOTS |
+------------+---------+------+------+-----------+-----------+
| Ubuntu2204 | STOPPED |      |      | CONTAINER | 0         |
+------------+---------+------+------+-----------+-----------+
| u1         | STOPPED |      |      | CONTAINER | 0         |
+------------+---------+------+------+-----------+-----------+
| u2         | STOPPED |      |      | CONTAINER | 0         |
+------------+---------+------+------+-----------+-----------+
| u3         | STOPPED |      |      | CONTAINER | 0         |
+------------+---------+------+------+-----------+-----------+
```

## Creación de Contenedores

Crear la máquina plantilla
```bash
lxc launch <imagen_os> <nombre_imagen>
# nombre_imagen     imagen_os
# Ubuntu2204        images:ubuntu/22.04/amd64
# RockyLinux8       images:rockylinux/8/amd64
# RockyLinux9       images:rockylinux/9/amd64
```
Crear la plantilla
```bash
lxc stop <nombre_imagen>
lxc publish <nombre_imagen> --alias=<alias_plantilla> description="<descripcion de la plantilla>"
```
Crear contenedores con la plantilla
```bash
lxc launch <alias_plantilla> <nombre_contenedor>
```

Ejemplo:
```bash
lxc launch  ubuntu:22-04 Ubuntu2204
lxc stop Ubuntu2204
lxc publish Ubuntu2204 --alias=Ubuntu2204Base description="Plantilla base para los contenedores con Ubuntu 22.04 y Ansible"
lxc launch Ubuntu2204Base u1
lxc launch Ubuntu2204Base u2
```


## Gestionar Contenedores
Borrado
```bash
lxc delete u1
```
Creación
```bash
lxc launch Ubuntu2204Base u1
```
Información
```bash
lxc info u1
```
Gestión
```bash
lxc start u1
lxc restart u1
lxc stop u1
```
Consola
```bash
lxc exec RockyLinux9 -- /bin/bash
```

