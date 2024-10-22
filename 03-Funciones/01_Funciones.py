# como crear una función
# siempre escribir en minusculas
# ej:--> def hablar():

# Función básica para saludar a una persona

def saludar_persona(nombre):
    """Saluda a la persona cuyo nombre se pasa como argumento"""
    print(f'Hola, {nombre}')


# Solicitamos el nombre al usuario
nombre = input('Introduce tu nombre: ')
saludar_persona(nombre)
