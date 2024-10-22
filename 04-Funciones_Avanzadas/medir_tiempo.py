import time
import timeit

# Medir el tiempo con time


def prueba_for(numero):
    lista = [num for num in range(1, numero + 1)]
    return lista


inicio = time.time()
prueba_for(100000)
final = time.time()
print(f'Tiempo con for: {final - inicio} segundos')

# Medir el tiempo con timeit
declaracion = 'prueba_for(10)'
mi_setup = '''
def prueba_for(numero):
    lista = [num for num in range(1, numero + 1)]
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print(f'Tiempo con timeit: {duracion} segundos')
