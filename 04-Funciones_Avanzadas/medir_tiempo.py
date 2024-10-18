
#import time
'''
def prueba_for(numero):
	lista = []
	for num in range(1,numero+1):
		lista.append(num)
	return lista

def prueba_while(numero):
	lista = []
	cont = 1
	while cont <= numero:
		lista.append(cont)
		cont += 1
	return lista

inicio = time.time()
prueba_for(100000)
final = time.time()

print(final - inicio)


inicio = time.time()
prueba_while(100000)
final = time.time()

print(final - inicio)
'''

import timeit

declaracion =  '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
	lista = []
	for num in range(1,numero+1):
		lista.append(num)
	return lista
'''

duracion = timeit.timeit(declaracion , mi_setup, number = 1000000)
#print(f'prueba for   --> {duracion}')

declaracion2 = '''
prueba_while(10)
'''
mi_setup2 = '''
def prueba_while(numero):
	lista = []
	cont = 1
	while cont <= numero:
		lista.append(cont)
		cont += 1
	return lista
'''
duracion2 = timeit.timeit(declaracion2 , mi_setup2, number = 1000000)
#print(f'prueba while --> {duracion2}')

if duracion2 < duracion:
	print(f'La funcion "prueba_while()" es la mas rapida con tiempo de: {duracion2}')
elif duracion2 > duracion:
	print(f'La funcion "prueba_for()" es la mas rapida con tiempo de: {duracion}')