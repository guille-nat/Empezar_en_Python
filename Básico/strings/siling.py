
# * Siling:
texto = "ABCDEFGHIJKLM"
# fragmento = texto[2:5]  # Asi lo quie le estoy diciendo es que extraiga todos los carateres que van desde el índice 2 y
# hasta pero no incluyendo el índice número 5

# fragmento = texto[2:] # si yo le saco el ultimo índice despues de los dos puntos python interpreta que agarra desde el
# índice 2 hasta el final

# fragmento = texto[:5]   #interpreta de esta manera desde el índice inical hasta en este caso el índice 5 (sin incluir)

# Lo que hace este tercer factor es hacer saltear en este caso de dos en dos
fragmento = texto[2:10:2]

# print(fragmento)
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
# print(len(frase))
# sirve para obtener la cadena de caracteres pero al revez
print((frase[::-1]))


"""listas, Tuplas, sets, diccionarios. (indices, elimincacion, cambios, ordenar, separar)"""
# * Listas
mi_lista = ['a', 'b', 'c']  # funciona con los mismos metodos del string
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista+mi_lista2

# mi_lista3[0] = 'alfa'           #en las listas se puede modificar y sobre escribir cada uno de sus elementos

# mi_lista3.append('g')   #sirve para agregar un elemento
# mi_lista3.pop(0)       #elimina elementos, un parentesis sin nada es igual a eliminar el ultimo elemento

# print(mi_lista3)


list = ['g', 'o', 'b', 'm', 'c']
# list.sort()         #Ordena la lista
# list.reverse() #voltea el orden de la lista
print(list)
