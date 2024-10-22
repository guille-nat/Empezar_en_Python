# Ejemplo de uso de enumerate

lista = ['a', 'b', 'c']

# Enumerar los elementos de la lista
for indice, item in enumerate(lista):
    print(f"Índice: {indice}, Elemento: {item}")

# También se puede enumerar rangos de números
for indice, numero in enumerate(range(50, 101)):
    print(f"Índice: {indice}, Número: {numero}")

lista_nombres = [
    "Marcos", "Laura", "Mónica",
    "Javier", "Celina", "Marta",
    "Darío", "Emiliano", "Melisa"
]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):  # .startswith()  significa comienza con
        print(indice)
