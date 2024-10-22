from random import randint, uniform, choice, shuffle, random

# Generar un número aleatorio entero entre 1 y 50
aleatorio = randint(1, 50)
print(f"Número aleatorio entero: {aleatorio}")

# Generar un número decimal entre 1 y 5 con un decimal
aleatorio2 = round(uniform(1, 5), 1)
print(f"Número aleatorio decimal: {aleatorio2}")

# Generar un número decimal entre 0 y 1
aleatorio3 = random()
print(f"Número aleatorio entre 0 y 1: {aleatorio3}")

# Elegir un color al azar de una lista
colores = ['azul', 'gris', 'rojo', 'violeta']
aleatorio4 = choice(colores)
print(f"Color aleatorio: {aleatorio4}")

# Mezclar una lista de números
numeros = list(range(5, 50, 5))
shuffle(numeros)
print(f"Números mezclados: {numeros}")
