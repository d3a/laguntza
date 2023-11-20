# Entorno

## PIP
### Instalacion
```
python get-pip.py
python -m pip install -U pip
```

### Uso
Listar paquetes:
- `pip freeze`

Instalar paquetes:
- `pip install <pkg>`

Guardar paquetes instalador para instalar después:
```
pip freeze > req.txt
pip install -r req.txt
```

## virtualenv
### Instalacion
- `python -m pip install virtualenv`
- `pip install virtualenv`

### Uso
Crear entorno virtual:
- `python -m venv <nombre>`
- `virtualenv <nombre> --python=python`

Activar entorno virtual:
- `.\<nombre>\Scripts\activate`

Si sale error de ejecución de scripts powershell hay que ejecutar:
```PS1
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Get-ExecutionPolicy -List
```


