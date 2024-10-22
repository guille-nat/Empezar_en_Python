# Clase base (padre)
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

# Clase derivada (hija)


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pío')

    def volar(self, metros):
        print(f'El pájaro vuela {metros} metros')


# Prueba de herencia
piolin = Pajaro(2, 'amarillo', 100)
piolin.nacer()  # Método heredado
piolin.hablar()  # Método sobrescrito
