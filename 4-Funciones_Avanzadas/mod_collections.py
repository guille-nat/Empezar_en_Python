#.------ Cuenta los caracteres -------.#

#from collections import Counter	

#lista = [1,1,2,2,3,3,4,55,5,6,6,6,7,7,6]
#repetidos = Counter(lista)
#print(repetidos)
#print(Counter.most_common(repetidos))	#caracter más común.
#print(list(repetidos))	#trasforma en una lista solo los caracters sin repetirlos.


#------ Puede agregar una calve vacia cuando no exista a un diccionario----#
'''
from collections import defaultdict

mi_dic = defaultdict(lambda: 'nada')	# lo que queremos que diga 
										 #cuando no exista la calve.
mi_dic['uno'] = 'azul'

print(mi_dic['dos'])	# aunque no exista la agrega con el valor que le dijimos.

print(mi_dic)
'''

#------- Puede asignarle nombre a los indices de las tuplas ----#

from collections import namedtuple

persona = namedtuple('persona',['Nombre','Altura','Peso'])

guillermo = persona('Guillermo',1.76,110)

print(guillermo.Peso) # Acceso a travez del nombre

print(guillermo[2])	# Acceso a travez del indice

