# Uso de pathlib para trabajar con rutas
from pathlib import Path

# Definir la carpeta y archivo
carpeta = Path('C:/Users/user//Documents/python ej practica')
archivo = carpeta / 'pruebas2.txt'

# Abrir y leer el archivo
with open(archivo) as mi_archivo:
    print(mi_archivo.read())
