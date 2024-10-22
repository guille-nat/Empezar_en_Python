mi_texto = "Esta es una prueba"
# puedes buscar palabras que te va a devolver el índice de donde empieza la palabra
resultado = mi_texto.index("a", 5, 15)
# con una coma lo que nos permite hacer es buscar a partir de ese índice que ponemos
print(resultado)
# si agregamos otra coma vamos indicar hasta que índice busca (ojo no incluye el ultimo índice)

# Ejemplo de indexación en cadenas
# Se accede al carácter en la posición 5 de la palabra
palabra = "Otorrinolaringologo"
print(palabra[5])  # Imprime 'r', que está en la posición 5

# Puedes usar también el método index para buscar la primera aparición de un carácter
print(palabra.index('r'))  # Devuelve la primera posición de 'r'
