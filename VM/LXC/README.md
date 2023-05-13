# LXC/LXD

## Home
[Linux Containers](https://linuxcontainers.org/)

## Instalación

```bash
snap install lxd
lxd init
lxd --version
```



```bash
$ lxc image list
+---------------+--------------+--------+--------------------------------------+--------------+-----------+----------+-----------------------------+
|     ALIAS     | FINGERPRINT  | PUBLIC |             DESCRIPTION              | ARCHITECTURE |   TYPE    |   SIZE   |         UPLOAD DATE         |
+---------------+--------------+--------+--------------------------------------+--------------+-----------+----------+-----------------------------+
| Ubuntu2204SSH | 5721dd0e330c | no     | Ubuntu 22.04 LTS server (20221101.1) | x86_64       | CONTAINER | 602.55MB | Nov 8, 2022 at 8:05am (UTC) |
+---------------+--------------+--------+--------------------------------------+--------------+-----------+----------+-----------------------------+

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

## Gestionar VM
```bash
lxc info u1
lxc start u1
lxc restart u1
lxc stop u1

lxc delete u1
```


## Crear Máquians RockyLinux
Crear la máquina plantilla
```bash
lxc launch images:rockylinux/9/amd64 RockyLinux9
```

Configurar SSH
```bash
lxc exec RockyLinux9 -- /bin/bash
```
https://linuxstoney.com/enable-ssh-service-on-rocky-linux-8-centos-8/
https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-rocky-linux-8-quickstart

Crear máquinas
```bash
lxc stop RockyLinux9
lxc publish RockyLinux9 --alias=RockyLinux9SSH description="RockyLinux con ssh key"
lxc launch RockyLinux9SSH r1
lxc launch RockyLinux9SSH r2
```

Ver plantillas
```bash
lxc list images
```