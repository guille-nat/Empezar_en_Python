"""Estructuras de control en Python: if, for, while"""

# Lista de países
lista = ['Argentina', 'Francia', 'Dinamarca', 'Brasil']

# * For loop: Recorre una lista e imprime cada país
for pais in lista:
    print(f"País: {pais}")

# * If statement: Verifica si "Argentina" está en la lista
if "Argentina" in lista:
    print(f'Argentina está en el índice {lista.index("Argentina")}\n')

# * While loop: Cuenta del 1 al 20
x = 0
while x < 20:
    x += 1
    print(x)

# * If-elif-else: Verificación múltiple
numero = 10
if numero > 10:
    print("El número es mayor a 10")
elif numero == 10:
    print("El número es exactamente 10")
else:
    print("El número es menor a 10")

# * Listas por comprensión: Crear una lista de cuadrados
cuadrados = [x**2 for x in range(1, 11)]
print(f"Cuadrados del 1 al 10: {cuadrados}")
