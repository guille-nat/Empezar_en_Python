import zipfile
import shutil

# Comprimir archivos con zipfile


def comprimir_zip():
    mi_zip = zipfile.ZipFile('mi_archivo_comprimido.zip', 'w')
    mi_zip.write('texto_A.txt')
    mi_zip.write('texto_B.txt')
    mi_zip.close()

# Extraer archivos con zipfile


def extraer_zip():
    zip_abierto = zipfile.ZipFile('mi_archivo_comprimido.zip', 'r')
    zip_abierto.extractall()

# Comprimir con shutil


def comprimir_shutil():
    origen = 'C:\\ruta\\a\\la\\carpeta'
    destino = 'Todo_comprimido'
    shutil.make_archive(destino, 'zip', origen)

# Extraer con shutil


def extraer_shutil():
    shutil.unpack_archive('Todo_comprimido.zip', 'Nueva_carpeta', 'zip')


comprimir_zip()
extraer_zip()
comprimir_shutil()
extraer_shutil()
