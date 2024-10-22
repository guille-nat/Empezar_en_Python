from random import shuffle

# Mezclar una lista de palitos


def mezclar(lista):
    """Mezcla aleatoriamente la lista de palitos"""
    shuffle(lista)
    return lista

# Solicitar al usuario que elija un número entre 1 y 4


def probar_suerte():
    """Solicita al usuario que elija un número del 1 al 4"""
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)

# Verificar si el intento es el palito más corto


def chequear_intento(lista, intento):
    """Comprueba si el usuario eligió el palito más corto"""
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Te salvaste')
    print(f'Te ha tocado {lista[intento-1]}')


# Ejecución
palitos = ['-', '--', '---', '----']
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)
