def DecorarSaludo(funcion):
	
	def OtraFuncion(palabra):
		print('Holaaaa')
		funcion(palabra)
		print('Adios')
	return OtraFuncion

def Mayusculas(palabra):
	print( palabra.upper())

def Minuscula(palabra):
	 print(palabra.lower())

# @DecorarSaludo ---> es una forma de llamar al decorado. 
						# ya que las funciones son objetos tambien.

Mayuscula_Decorada = DecorarSaludo(Mayusculas)

Mayuscula_Decorada('hola soy guillermo')  # <--- "Mayuscula_Decorada" 
												# se convierte en función
												 # En esta caso la función
												  # Mayusculas
