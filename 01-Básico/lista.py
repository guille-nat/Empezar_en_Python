# Operaciones básicas con listas

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

# Modificar un elemento en la lista
mi_lista3[0] = 'alfa'

# Agregar un nuevo elemento
mi_lista3.append('g')

# Eliminar el primer elemento
mi_lista3.pop(0)

print(mi_lista3)

# Ordenar una lista
lista = ['g', 'o', 'b', 'm', 'c']
lista.sort()  # Ordena la lista
print(lista)
