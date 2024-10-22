'''Qué son los generadores: Los generadores permiten producir una secuencia de valores "sobre la marcha" e
	n lugar de almacenar toda la secuencia en la memoria. Esto los hace útiles cuando trabajamos con grandes datasets 
	cuando necesitamos un flujo continuo de datos.

Uso de next(): next() se utiliza para obtener el siguiente valor de un generador. 
	Cada vez que se llama a next(), el generador reanuda su ejecución donde la dejó y produce el siguiente valor.

Generadores con bucles for: En lugar de usar next() manualmente, 
	podemos recorrer los valores de un generador usando un bucle for. 
	Esto es más eficiente y legible en la mayoría de los casos.'''


# Función normal que devuelve una lista completa
def MiFuncion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

# Generador que devuelve los valores uno a uno


def MiGenerador():
    for x in range(1, 5):
        yield x * 10  # Yield devuelve un valor y pausa la función hasta la siguiente llamada


# Usar la función normal
print("Resultado de MiFuncion:", MiFuncion())

# Usar el generador
g = MiGenerador()
print(next(g))  # Devuelve 10
print(next(g))  # Devuelve 20

# Generador con múltiples yields


def OtroGenerador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


# Llamar al generador
g2 = OtroGenerador()
print(next(g2))  # Devuelve 1
print(next(g2))  # Devuelve 2
print(next(g2))  # Devuelve 3

# Uso de un generador en un bucle for


def GeneradorConFor():
    for x in range(1, 5):
        yield x * 10


# El generador puede ser usado en un bucle for sin necesidad de llamar a next()
for valor in GeneradorConFor():
    print(f"Valor generado: {valor}")
