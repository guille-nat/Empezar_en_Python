def suma():
	n1 = int(input('número 1: '))
	n2 = int(input('número 2:'))
	print(n1+n2)
	print('\ngracias por sumar\n')

'''
try: 	#Para poner el codigo que queresmos probar.
	suma()

except TypeError:		#except seguido de algun nombre de error 
						#es para hacer algo si ese error pasa.
	print('Estas intentando concatenar tipos distintos.\n')

except ValueError:
	print('Ese no es un número\n')

except:		#Para poner el codigo a ejecutar si hay un error.
	print('Algo ha salido mal\n')
	
else:	# Codigo a ejecutar si no hay un error.
	print('Has hecho correctamente\n')
	

finally:	# Codigo qe se va a ejecutar de todos mosdos.
	print('Eso fue todo\n')
'''

#--------------------------------------------------------------#

def pedir_numero():

	while True:

		try:
			numero = int(input('Dame un número: '))
		except:
			print('Ese no es un número.')
		else:
			print(f'Ingresaste el número {numero}')
			break

pedir_numero()