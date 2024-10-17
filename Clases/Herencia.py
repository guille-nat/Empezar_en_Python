

# -------------------------------------------------------------------------------#
     #----------------#
    #HERENCIA EXTENDIDA#
     #----------------#


#clase padre

class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

# -------------------------------------------------------------------------------#

#clase hija, esta hereda los atributos de la clase padre y tambien dentro de la clase hija los puede modificar

class Pajaro(Animal):

    # agrega atributos a la anterior
    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)        #con supper se hace todas los atributos heredados
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self,metros):
        print(f'el pajaro vuela {metros} metros')

#print(Pajaro.__bases__) <---- Indica de quien hereda 

#print(Animal.__subclasses__()) <--- A quien le transmite la Herencia

#piolin = Pajaro(2, 'amarillo')
#print(piolin.color)
#piolin.nacer()

# -------------------------------------------------------------------------------#


#piolin = Pajaro(2, 'amarillo',60)

#mi_animal = Animal(5, 'negro')

#piolin.hablar() #SOBRE ESCRIBIO SU HERENCIA

#piolin.volar(1000)


# -------------------------------------------------------------------------------#
         #---------------#
        #HERENCIA MULTIPLE#
         #---------------#
class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja Ja')

    def hablar(self):
        print('que tal')
#hay un orden de busqueda si dos metodos se repiten en dos clases a los que se heredan se ejecuta el metodo de la primera herencia en este caso Padre

class Hijo(Padre,Madre):    #hereda de dos clases, pueden ser dos o mas
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

#mi_nieto.hablar()
#mi_nieto.reir()

print(Nieto.__mro__) # <--- orden en que se resuelve la herencia.