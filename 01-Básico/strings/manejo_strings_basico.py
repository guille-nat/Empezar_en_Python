"""Manejos de strings."""
"""Los manejos de los string son muy útiles a la hora de poder acceder a 
la informacion de una cadena de caracters, 
mutar su comportamiento para mostrarlo o guardarlo en algun tipo de dato"""

# Convertir a mayúsculas
texto = 'Este'
resultado = texto.upper()  # Convierte todo a mayúsculas
print(resultado)

# Convertir un carácter específico a mayúsculas
print(texto[2].upper())  # Solo el tercer carácter (índice 2)

# Dividir cadenas
print(texto.split())  # Divide por espacios
print(texto.split('t'))  # Divide usando 't' como delimitador

# Reemplazar caracteres en una cadena
print(texto.replace("e", "x"))  # Reemplaza 'e' por 'x'

# Formateo de cadenas
x = 10
y = 5
print(f"Mis números son {x} y {y}")  # Formateo con f-strings
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
