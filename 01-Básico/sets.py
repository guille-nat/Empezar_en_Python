# son una coleccion de elementos como por ejemplo las listas
# se pueden declarar de dos formas usando la palabra set([1,2,3,4,5,6]) o solo entre llaves {1,2,3,4,5,6}
# los elementos no se pueden repetir
# los elementos no estan ordenados en índices
# sus elementos son inmutables
# las listas ni diccionarios se pueden poner dentro de un set
# si admite tuple (ya que son inmutables y no estan ordenados)

# Conjuntos en Python (sets)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Unión de conjuntos
s3 = s1.union(s2)
print(f"Unión de s1 y s2: {s3}")

# Agregar un elemento
s1.add(4)

# Eliminar un elemento
s1.remove(2)

# Limpiar el conjunto
s1.clear()

print(s1)
