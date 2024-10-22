class Pajaro:
    # Atributo de clase
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Método de instancia
    def piar(self):
        print(f'Pío, mi color es {self.color}')

    # Otro método de instancia
    def volar(self, metros):
        print(f'Voló {metros} metros')


# Crear instancia y usar métodos
piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(40)
