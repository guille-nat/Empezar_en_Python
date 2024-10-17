# 'w' --> para escribir el archivo, vaciando su in terior.  Ej. archivo = open('prueba.txt', 'w')
# 'r' --> para solo leer el archivo, con este no se puede escribir en él. Ej. archivo = open('prueba.txt', 'r')
# 'a' --> lee el archivo y se posiciona al final del mismo para continuar escribiendo y asi no perder nada. Ej. archivo = open('prueba.txt', 'w')

archivo = open('prueba.txt', 'a')

#lista = ['hola','mundo','aqui','estoy']

#archivo.write('\n biembenido')



'''for p in lista:
    archivo.writelines(p + '\n')
archivo.write('Soy el nuevo texto')     # sirve para escribir en un archivo
'''

archivo.close()