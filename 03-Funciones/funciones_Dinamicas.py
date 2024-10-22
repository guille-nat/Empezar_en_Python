def chequear_3_cifras(lista):
    """Devuelve una lista con los números de 3 cifras"""
    lista3 = []
    for n in lista:
        if n in range(100, 1000):
            lista3.append(n)
    print(f'los numero de 3 cifras son: {lista3}')


lista = [555, 100, 340, 1000]
# resultado = chequear_3_cifras(lista)


def todos_positivos(lista):
    """Devuelve True si todos los números son positivos, 
    False en caso contrario"""
    lista3 = []
    for g in lista:
        if g > 0:
            lista3.append(g)
        elif g < 0:
            return False

    return True


lista_numeros = [12, 22, 2, -32]
r = todos_positivos(lista_numeros)
print(r)
