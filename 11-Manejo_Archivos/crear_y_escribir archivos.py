# 'w' --> para escribir el archivo, vaciando su in terior.  Ej. archivo = open('prueba.txt', 'w')
# 'r' --> para solo leer el archivo, con este no se puede escribir en él. Ej. archivo = open('prueba.txt', 'r')
# 'a' --> lee el archivo y se posiciona al final del mismo para continuar escribiendo y asi no perder nada. Ej. archivo = open('prueba.txt', 'w')

# Abrir un archivo en modo 'a' para añadir contenido al final
with open('prueba.txt', 'a') as archivo:
    archivo.write('\nBienvenido')  # Añadir texto al final

# Alternativamente, podrías usar 'w' para sobrescribir todo el contenido
with open('prueba.txt', 'w') as archivo:
    archivo.write('Este es un nuevo texto que reemplaza el anterior')
