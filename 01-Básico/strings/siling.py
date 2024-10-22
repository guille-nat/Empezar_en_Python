
# * Siling:
# Se accede a una porción de la cadena
texto = "Python es genial"
# Asi lo quie le estoy diciendo es que extraiga todos los carateres que van desde el índice 2 y
# hasta pero no incluyendo el índice número 5
fragmento = texto[2:5]
print(fragmento)
# si yo le saco el ultimo índice despues de los dos puntos python interpreta que agarra desde el
# índice 2 hasta el final
fragmento = texto[2:]
print(fragmento)
# interpreta de esta manera desde el índice inical hasta en este caso el índice 5 (sin incluir)
fragmento = texto[:5]
print(fragmento)
# Extrae caracteres desde la posición 2 a la 10, saltando de 2 en 2
fragmento = texto[2:10:2]
print(fragmento)  # Resultado: 'to s'

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(len(frase))
# Invertir una cadena usando slicing
frase = "Es genial trabajar con ordenadores"
print(frase[::-1])  # Invierte toda la cadena


"""listas, Tuplas, sets, diccionarios. (indices, elimincacion, cambios, ordenar, separar)"""
# * Listas
# funciona con los mismos metodos del string
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista+mi_lista2
# en las listas se puede modificar y sobre escribir cada uno de sus elementos
mi_lista3[0] = 'alfa'
print(mi_lista3)
# sirve para agregar un elemento
mi_lista3.append('g')
print(mi_lista3)
# elimina elementos, un parentesis sin nada es igual a eliminar el ultimo elemento
mi_lista3.pop(0)
print(mi_lista3)


list = ['g', 'o', 'b', 'm', 'c']
list.sort()  # Ordena la lista
list.reverse()  # voltea el orden de la lista
print(list)
