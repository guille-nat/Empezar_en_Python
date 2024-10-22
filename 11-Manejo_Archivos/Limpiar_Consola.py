import os

# Función para limpiar la consola en cualquier sistema operativo


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


# Solicitar información al usuario
nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')

# Limpiar la consola
limpiar_consola()

print(f'Tu nombre es {nombre} y tienes {edad} años')
