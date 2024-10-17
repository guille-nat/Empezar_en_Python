# entrelaza los elementos de dos o más (listas, tuples,diccionarios,o mezclas) en tuples.
nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']
                                        #si las listas o lo cualquier cosa a combinar son de diferente tamaños,
                                        #el tamaño que respeta es el de la lista mas corta (los que sigue y sobren
                                                                                            # los ignora).
combinados = list(zip(nombres,edades,ciudades))      #siempre se deben convertir en lista para para poder mostrarlo.

print(combinados)
for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

