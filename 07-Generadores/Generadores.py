'''
def MiFuncion():
	lista = []
	for x in range(1,5):
		lista.append(x*10)
	return lista

def MiGenerador(): # ventaja lo genera al momento y se acuerda de donde lo dejo.
	for x in range(1,5):
		yield x *10 	#<-- se debe usar -yield- y no return.
								No se puede ejecutar más de las veces que 
									se planeo en este caso no más de 4 veces.

print(MiFuncion())

g = MiGenerador() #<-- se debe guardar en una variable.
 
print(next(g))#<-- se usa para llamr que genere el siguiente termino.
print(next(g))	
'''

# se pueden poner varios -yield- .
# pero se debe llamar la cantidad de veces a ejecutar. 
	# EJ:
def MiGenerador():
	x = 1
	yield x

	x += 1
	yield x

	x += 1
	yield x

g = MiGenerador()		

# En este caso para tener los 3 yield se debe llamar 3 veces.
	# el generador se "acuerda" hasta donde llego la ultima ejecución.
print(next(g))
print(next(g))
print(next(g))


