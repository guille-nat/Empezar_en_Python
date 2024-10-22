# Definimos una variable llamada numero1 con un valor de 500
numero1 = 500

# Intentamos imprimir la variable, pero hay un error en la mayúscula.
# Pylint detectaría esto como un error de nombre de variable (no definido)
# El siguiente código debería corregirse para usar la variable correctamente:
print(numero1)  # Corregido: se usa "numero1" en lugar de "Numero1"
'''
Instalar y usar Pylint:
Instala Pylint con:
pip install pylint
Ejecuta Pylint en tu archivo:

pylint archivo1.py
Pylint te proporcionará una lista de advertencias y errores, 
como variables no definidas o problemas de estilo.'''
