import os 
import shutil
#archivo = open('curso.txt','w')
#archivo.write('Texto de prueba')
#archivo.close()

#print(os.listdir())
#print(os.getcwd())

#shutil.move('curso.txt','C:\\Users\\maria\\OneDrive\\guille\\Escritorio')

#------- PARA ELIMINAR UN ARCHIVO Y MANDARLO A PAPELERA ------#
import send2trash

#send2trash.send2trash('curso.txt')
#------------------------------------------------------------#

# Almacena la ruta, luego las carpetas que halla en esa ruta y despues los archivos
#print(os.walk('C:\\Users\\maria\\OneDrive\\guille\\Escritorio\\pythonProject\\Día9'))  

ruta = 'C:\\Users\\maria\\OneDrive\\guille\\Escritorio\\pythonProject\\Día7'

for carprpeta,subcarpeta,archivo in os.walk(ruta):
	print(f'En la carpeta: {carprpeta}')
	print(f'Las subcarpeta son:')
	for sub in subcarpeta:
		print(f't{sub}')
	print(f'Los archivos son:')
	for arch in archivo:
		print(f'\t{arch}')
	print('\n')