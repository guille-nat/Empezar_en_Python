import os
import shutil
import send2trash

# Mover un archivo


def mover_archivo(origen, destino):
    shutil.move(origen, destino)

# Eliminar un archivo


def eliminar_archivo(archivo):
    send2trash.send2trash(archivo)

# Explorar una ruta


def explorar_ruta(ruta):
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        print(f'En la carpeta: {carpeta}')
        print(f'Subcarpetas: {subcarpetas}')
        print(f'Archivos: {archivos}')


# Ejecuciones
mover_archivo('curso.txt', 'C:\\ruta\\a\\destino')
eliminar_archivo('curso.txt')
explorar_ruta('C:\\ruta\\a\\explorar')
