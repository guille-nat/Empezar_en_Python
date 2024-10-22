'''nos permite manipular rutas de sistemas de archivos de 
forma rapida en cualquier sistema operativo.'''
# -------------------------------------------------------------------------------#
# para leeer un archivo
# print(carpeta.read_text())

# -------------------------------------------------------------------------------#

# extrae el nombre del archivo
# print(carpeta.name)

# -------------------------------------------------------------------------------#

# nos da la terminacion del archivo o extencion del archivo en este caso .txt
# print(carpeta.suffix)

# -------------------------------------------------------------------------------#

# nos da el nombre sin la terminacion en este caso pruebas2
# print(carpeta.stem)

# -------------------------------------------------------------------------------#
from pathlib import Path, PureWindowsPath

# Definir la ruta de un archivo
carpeta = Path('C:/Users/user/Documents/python ej practica/pruebas2.txt')

# Verificar si el archivo existe
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print(f'Archivo encontrado: {carpeta.name}')
    print(f'Termina en: {carpeta.suffix}')
    print(f'Nombre sin extensión: {carpeta.stem}')
