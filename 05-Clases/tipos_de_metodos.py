class Pajaro:
    # Atributo de clase
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Método de instancia (modifica atributos de instancia)
    def volar(self, metros):
        print(f'Voló {metros} metros')

    # Método de clase (modifica atributos de clase)
    @classmethod
    def cambiar_alas(cls, estado):
        cls.alas = estado

    # Método estático (no accede a ningún atributo)
    @staticmethod
    def mirar():
        print('El pájaro está mirando')


# Usar métodos
Pajaro.mirar()  # Método estático
Pajaro.cambiar_alas(False)  # Método de clase
print(Pajaro.alas)
