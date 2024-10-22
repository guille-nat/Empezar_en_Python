# Entrelaza los elementos de dos o más (listas, tuples,diccionarios,o mezclas) en tuples.
# Uso de zip() para combinar listas
# si las listas o lo cualquier cosa a combinar son de diferente tamaños,
# El tamaño que respeta es el de la lista mas corta (los que sigue y sobren
# Los ignora).

nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Lima', 'Madrid', 'México']

# Combinar listas usando zip
# Siempre se deben convertir en lista para para poder mostrarlo.
combinados = list(zip(nombres, edades, ciudades))

# Imprimir los resultados
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
