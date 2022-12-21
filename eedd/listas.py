# Inicializar lista
lista = list()
print( type(lista) )

# Asignación
list1 = [1, 2, 3, 4 ]
list2 = [100, 200, 300, 400 ]

# Mostrar por elementos
for elem in lista:
    print( f'Elemento: {elem}' )

# Mostrar por indices:
for i in range( 0, len(lista) ):
    print( f'Lista[{i}]: {list1[i]}' )

# Mostrar por elementos enumerados
for i, elem in enumerate(list1):
    print( f'Lista[{i}]: {elem}' )

# Mostrar por elementos de dos listas usando zip
for elem, elem2 in zip(list1, list2):
    print( f'{elem}: {elem2}' )

# Mostrar por elementos de dos listas usando zip y enumerados
for i, elem in enumerate(zip(list1, list2)):
    print( f'{i}: {elem[0]}: {elem[1]}' )

# Mostrar elementos sueltos
print( f'List1: {list1}' )
print( f'List1[:]: {list1[:]}' )
print( f'List1[1]: {list1[1]}' )
print( f'List1[-1]: {list1[-1]}' )
print( f'List1[0:2]: {list1[0:2]}' )
print( f'List1[:2]: {list1[:2]}' )
print( f'List1[1:3]: {list1[1:3]}' )
print( f'List1[2:]: {list1[2:]}' )

# Copiar listas:
lista = list1
# lista se convierte en un puntero a list1
lista.append( "otro_elemento" )
print( f'lista.append="otro_elemento"' )
print( f'  Lista: {lista}' )
print( f'  List1: {list1}' )

lista = list1[:]
# lista se convierte en una copia de list1
lista.append( "otro_elemento" )
print( f'lista.append="otro_elemento"' )
print( f'  Lista: {lista}' )
print( f'  List2: {list1}' )

# Concatenar listas
lista = list1 + list2
print( f'list1 + list2: {lista}' )
