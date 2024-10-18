'''Hay 3 tipos de metodos :
                           - metodo de instancia
                           - metodo de clase
                           - metodo estaticos'''
    # -------------------------------------------------------------------------------#


class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie


        #crea un metodo
    def piar(self):
        print('pío, mi color es {}'.format(self.color))


        #crea otro metodo
    def volar(self,metros):
        print(f'Voló {metros}mts')
        self.piar()

    ''' metodos de instancia     acceden y modifican atributos del objeto
                                 acceden a otros metodos
                                 pueden modificar el estado de la clase'''
    def pintasr_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaros es {self.color}')
    # -------------------------------------------------------------------------------#
    ''' metodo de clase, no necesitan una instancia para ejecutarse, 
         no pueden acceder a los atributos de instancoia,
                                             pero si puede con los de clase'''

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    # -------------------------------------------------------------------------------#
    ''' metodos estaticos, o pueden acceder a los atributos de instancoia, 
         tampoco piede modificar atributos de la clase'''

    @staticmethod
    def mirar():
        print('El pajaro mira')

    # -------------------------------------------------------------------------------#


#piolin = Pajaro("amarillo", "canario")
#piolin.pintasr_negro()
#piolin.volar(80)
#piolin.alas = False
#print(piolin.alas)

#Pajaro.poner_huevos(3)
#Pajaro.mirar()
