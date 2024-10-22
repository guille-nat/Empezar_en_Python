'''
Explicación adicional:
Pruebas unitarias:

Las pruebas unitarias son una forma de verificar automáticamente que 
el código funcione como se espera.
unittest es una biblioteca estándar en Python que permite definir y 
ejecutar pruebas de forma sencilla.
assertEqual():

El método self.assertEqual() verifica que dos valores sean iguales. 
Si no lo son, la prueba falla.
Múltiples pruebas:

Se agregaron pruebas adicionales para cubrir más casos, 
como manejar cadenas vacías y texto ya en mayúsculas.
'''
import unittest
import Cambia_Texto  # Importamos el módulo que contiene la función a probar


class Comprobar(unittest.TestCase):  # Hereda de unittest.TestCase para crear pruebas

    def testMayuscula(self):
        """Prueba que convierte texto a mayúsculas"""
        texto = 'Buenos dias'
        resultado = Cambia_Texto.Cambia_Mayuscula(texto)
        # Verificamos si el resultado es el esperado
        self.assertEqual(resultado, 'BUENOS DIAS')

    def testTextoVacio(self):
        """Prueba que maneja una cadena vacía"""
        texto = ''
        resultado = Cambia_Texto.Cambia_Mayuscula(texto)
        # Una cadena vacía debería seguir siendo vacía
        self.assertEqual(resultado, '')

    def testMayusculas(self):
        """Prueba que el texto ya en mayúsculas permanece igual"""
        texto = 'HOLA'
        resultado = Cambia_Texto.Cambia_Mayuscula(texto)
        # El texto en mayúsculas no debería cambiar
        self.assertEqual(resultado, 'HOLA')


# Ejecutamos las pruebas
if __name__ == '__main__':
    unittest.main()
