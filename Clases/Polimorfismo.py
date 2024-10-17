# muchas formas

class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice muuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice beee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1 , oveja1]


#for animal in animales:
 #   animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)