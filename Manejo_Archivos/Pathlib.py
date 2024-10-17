'''nos permite manipular rutas de sistemas de archivos de forma rapida en cualquier sistema operativo.'''
    #-------------------------------------------------------------------------------#

#de esta forma no tenemos ni que abrir ni cerrar el archivo
from pathlib import Path,PureWindowsPath

carpeta = Path('C:/Users/maria/OneDrive/guille/Documents/python ej practica/pruebas2.txt')

    #-------------------------------------------------------------------------------#

#para leeer un archivo
#print(carpeta.read_text())

    #-------------------------------------------------------------------------------#

#extrae el nombre del archivo
#print(carpeta.name)

    #-------------------------------------------------------------------------------#

#nos da la terminacion del archivo o extencion del archivo en este caso .txt
#print(carpeta.suffix)

    #-------------------------------------------------------------------------------#

# nos da el nombre sin la terminacion en este caso pruebas2
#print(carpeta.stem)

    #-------------------------------------------------------------------------------#

#ver si el archivo existe o no
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial existe')

    #-------------------------------------------------------------------------------#

#PureWindowsPath quiere decir ruta de windows pura, se importa de os junto con Path
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)