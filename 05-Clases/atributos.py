class Pajaro:
    # Atributo de clase (compartido por todas las instancias)
    alas = True

    # Atributos de instancia (específicos para cada instancia)
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


# Crear instancias de la clase
mi_pajaro = Pajaro('rojo', 'Tucán')
otro_pajaro = Pajaro('azul', 'Loro')

# Imprimir atributos de instancia y de clase
print(f'Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')
print(f'Todos los pájaros tienen alas: {mi_pajaro.alas}')
