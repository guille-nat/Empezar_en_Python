"""Manejos de strings."""
"""Los manejos de los string son muy útiles a la hora de poder acceder a la informacion de una cadena de caracters, 
mutar su comportamiento para mostrarlo o guardarlo en algun tipo de dato"""

texto = 'Este'

# resultado = texto.upper()   # Este es un método que convierte todo en mayusdcula

# resultado = texto[2].upper() # Este es un método que convierte en mayuscula solo el índice 2

# resultado = texto.lower()   # Este es un método que convierte todo en minusculas

# resultado = texto.split()   # Separa elementos y los guarda dentro de una lista

# resultado = texto.split('t') # Toma a t como separador de elementos de la lisa
# a = 'Aprender'
# b = 'Python'
# c = 'es'
# d = 'genial'
# e = ' '.join([a,b,c,d])
# print(e)

# Busca el índice donde se encuentra el caracter como el método index
resultado = texto.find("s")

# resultado = texto.replace("e","x") #sirve para remplazar se le pasan 2 argumentos, el primero es cual vamos
# a remplazar y el segundo es por cual lo haremos

print(texto)

# * Formatear Strings
x = 10
y = 5
# Tecnicaa .format (respetar siempre el orden de los datos)
print("Mis numeros son {} y {}".format(x, y))
# , se pueden hacer operaciones matematicas

color = "azul"
matricula = 237491
# Solo se coloca una f delante de las comillas,
print(f"El auto es {color} y su maticula es {matricula}")
# las llaves donde iria cada variable y dentro de ellas el nombre de las variables

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(
    f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")
