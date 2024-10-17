'''mi_lista =[1,1,1,1,1,1,1]
#print(len(mi_lista))
print(mi_lista)


class Objeto:
	pass

mi_objeto = Objeto()
#print(len(mi_objeto)) <-- NO SE PUEDE
print(mi_objeto)'''


class CD:

	def __init__(self, autor,titulo,canciones):
		self.autor = autor
		self.titulo = titulo
		self.canciones = canciones

	def __str__(self):	# <-- sirve para poder mostrar el contenido de la clase mediante un print.
		return f'Album: {self.titulo} de {self.autor}\n'

	def __len__(self):	# <-- donde nosotros definimos el largo en este caso cantidad de canciones.
		return self.canciones

	def __del__(self):
		print(f'\nSe ha eliminado el CD {self.titulo}\n')


mi_cd = CD('Pink Floyd','The Wall',24)

print(mi_cd)

print(len(mi_cd))

del mi_cd