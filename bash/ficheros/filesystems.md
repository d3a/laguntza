# Filesystems
- pvdisplay
- vgdisplay
- lvdisplay
- mount

## df
```bash
$ df -h [/var]
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/sdb        251G  5.6G  233G   3% /
```

## fdisk
Para ver información de todos los discos \[o de un disco concreto\]:
```bash
$ fdisk -l [/dev/sda]
  Disk /dev/sda: 60 GiB, 64424509440 bytes, 125829120 sectors
  Units: sectors of 1 * 512 = 512 bytes
  Sector size (logical/physical): 512 bytes / 512 bytes
  I/O size (minimum/optimal): 512 bytes / 512 bytes
  Disklabel type: dos
  Disk identifier: 0xcc0a154f

  Device     Boot   Start       End   Sectors Size Id Type
  /dev/sda1  *       2048   2099199   2097152   1G 83 Linux
  /dev/sda2       2099200 125829119 123729920  59G 8e Linux LVM
```
Para gestionar las particiones de un disco (comando interactivo):
```bash
$ fdisk /dev/sda
```
