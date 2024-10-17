class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    # -------------------------------------------------------------------------------#
#siempre acordarse de llamar a las instancias con self. + valor de la instancia
        #crea un metodo
    def piar(self):
        print('pío, mi color es {}'.format(self.color))     

    # -------------------------------------------------------------------------------#
        #crea otro metodo
    def volar(self,metros):
        print(f'Voló {metros}mts')

    # -------------------------------------------------------------------------------#

piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(40)
