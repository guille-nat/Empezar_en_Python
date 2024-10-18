''''
existen dos tipos de atributos los de Clase y los de instancia
'''
#-------------------------------------------------------------------------------#


class Pajaro:
    alas = True #ATRIBUTOS DE CLASE

    # ATRIBUTO DE INSTANCIA
    def __init__(self, color,especie):      #definimos atributos de clase       #__init__ es el "constructor de la clase" sirve para asignarle atributos
        self.color = color  #self es la instancia del objeto, es una convencion
        self.especie = especie

mi_pajaro = Pajaro('rojo','Tucan')

print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

#-------------------------------------------------------------------------------#
