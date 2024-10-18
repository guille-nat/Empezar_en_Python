''' como buscar un archivo en cualquier lugar
 en windows se debe escribir con dos \\
 en mack es con /
 metodo (os)    se debe importar'''
#una ruta puede tener dos elementos:
    #uno obligatorio es el nombre de base (EJ.('C:\Users\maria\OneDrive\guille\Documents\python ej practica'))
    #y dos el nombre del archivo (EJ.pruebas2)



    #-------------------------------------------------------------------------------#
#import os

# para obtener el directorio de trabajo actual
#ruta = os.getcwd()

    #-------------------------------------------------------------------------------#

# para cambiar de directorio, nos permite establecer una ruta nueva de trabajo
#ruta = os.chdir('C:\\Users\\maria\\OneDrive\\guille\\Documents\\python ej practica')

    #-------------------------------------------------------------------------------#

# para crear otra carpeta
#ruta = os.makedirs('C:\\Users\\maria\\OneDrive\\guille\\Documents\\python ej practica\\otra')

    #-------------------------------------------------------------------------------#

#ruta = 'C:\\Users\\maria\\OneDrive\\guille\\Documents\\python ej practica\\pruebas2.txt'

    #-------------------------------------------------------------------------------#

#sive para buscar el nombre del archivo en la ruta
#elemento = os.path.basename(ruta)

    #-------------------------------------------------------------------------------#
 
# es para saber el directorio de nuestar ruta
#elemento = os.path.dirname(ruta)

    #-------------------------------------------------------------------------------#

# sirve para traer una tupla con el nombre de directorio y el de base
#elemento = os.path.split(ruta)

    #-------------------------------------------------------------------------------#


#elimina la ultima carpeta
#os.rmdir('C:\\Users\\maria\\OneDrive\\guille\\Documents\\python ej practica\\otra')

    #-------------------------------------------------------------------------------#

#como abrir otro archivo que este en otro directorio

#otro_archivo =open('C:\\Users\\maria\\OneDrive\\guille\\Documents\\python ej practica\\pruebas2.txt')

#print(otro_archivo.read())


    #-------------------------------------------------------------------------------#


#esto es para que cualquier sistema operativo lo pueda leer

from pathlib import Path        # Path en mayusculas porque es un objeto

carpeta = Path('C:/Users/maria/OneDrive/guille/Documents/python ej practica')
archivo = carpeta / 'pruebas2.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()