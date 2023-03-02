
# Crear un conjunto vacio
cto = set()

# Crear desde una lista
print('---------------------------------------------------')
lista=[1,2,3]
cto = set(lista)
print('Añadir una lista a ', cto)
try:
    cto.add(lista)
    print(cto)
except TypeError:
    print('no se puede')
finally:
    print(cto)

# Crear desde una tupla
print('---------------------------------------------------')
tupla=(1,2,3)
cto = set(tupla)
print('Añadir una tupla a ', cto)
cto.add(tupla)
print(cto)

