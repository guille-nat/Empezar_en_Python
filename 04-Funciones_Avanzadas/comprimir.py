#import zipfile
'''
#------- Comprimir archivo con zip ------------#
mi_zip = zipfile.ZipFile('mi_archivo_comprimido.zip','w')

mi_zip.write('texto_A.txt')
mi_zip.write('texto_B.txt')

mi_zip.close()
#---------------------------------------------#
'''
'''
#------- Extraer archivo con zip ------------#
zip_abierto = zipfile.ZipFile('mi_archivo_comprimido.zip','r')
zip_abierto.extractall()    #extrae todo

#---------------------------------------------#
'''
import shutil

'''
#------- Comprimir archivo con shutil ------------#

origen = 'C:\\Users\\maria\\OneDrive\\guille\\Escritorio\\Nueva carpeta'

archivo_destino = 'Todo_comprimido'
shutil.make_archive(archivo_destino,'zip',origen)
#---------------------------------------------#
'''
#------- Extraer archivo con shutil ------------#

shutil.unpack_archive('Todo_comprimido.zip','Nueva_carpeta', 'zip')