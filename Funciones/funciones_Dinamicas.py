def chequear_3_cifras(lista):
    lista3 = []
    for n in lista:
        if n in range(100,1000):
            lista3.append(n)


        else:
            pass        #pase
    print(f'los numero de 3 cifras son: {lista3}')

lista = [555,100,340,1000]
#resultado = chequear_3_cifras(lista)


def todos_positivos(lista):
    lista3 = []
    for g in lista:
        if g > 0:
            lista3.append(g)
        elif g < 0:
            return False
        else:
            pass
    return True


lista_numeros = [12, 22, 2, -32]
r = todos_positivos(lista_numeros)
print(r)