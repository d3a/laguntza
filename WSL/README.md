# Notas WSL

## Básico
- ```wsl [-d <inst> [--cd <dir_trabajo>] [--user <usuario>]]``` Ejecuta la instancia indicada

- ```wsl -l [-v]``` Listar instancias/distribuciones instaladas 

- ```wsl -l --online``` Listar distribuciones disponibles 

- ```wsl --install -d <distro>``` Instalar distribución 

- ```wsl --unregister <distro>``` Eliminar distribución 

- ```wsl -t <inst>``` Parar una instancia

- ```wsl --shutdown``` Finaliza de inmediato todas las distribuciones en ejecución

## Cambiar hostname
1. Crear fichero ```/etc/wsl.conf```

```
[network]
hostname = <nuevo-nombre>
generateHosts = false
```

2. Editar fichero ```/etc/hosts```
```
127.0.0.1       localhost
127.0.1.1       <nuevo-nombre>.localdomain     <nuevo-nombre>
```

3. Editar fichero ```/etc/hostname``` (opcional)
```
<nuevo-nombre>
```

4. Reiniciar WSL
```
PS> wsl --shutdown
```

## Crear dos instancias de la misma ditribucion
1. Exportar distribución base
```
PS> wsl --install -d Ubuntu-20.04
PS> wsl --export Ubuntu-20.04 Ubuntu-20.04.tar
```

2. Importar 
```
PS> wsl --import UbuntoInst1 <ruta>\UbuntoInst1 Ubuntu-20.04.tar
PS> wsl --import UbuntoInst2 <ruta>\UbuntoInst2 Ubuntu-20.04.tar
```

3. Cambiar nombres de máquinas

4. Estableces usuario por defecto. Editar ```/etc/wsl.conf```
```
[user]
default=<username>
```
