import unittest
import Cambia_Texto

class Comprobar(unittest.TestCase): 	#Hereda todo de unittest

	def testMayuscula(self):
		texto = 'Buenos dias'
		resultado = Cambia_Texto.Cambia_Mayuscula(texto)
		self.assertEqual(resultado,'BUENOS DIAS')	#Lo que hace es comprobar si 
													# el primer argumento resulta
													#  igual al segundo
													#   (para comprobar)

	#-------- TIENE QUE IR SI O SI ----------#
if __name__ == '__main__':
	unittest.main()