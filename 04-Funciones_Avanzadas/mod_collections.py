from collections import Counter, defaultdict, namedtuple

# Contar elementos en una lista con Counter
lista = [1, 1, 2, 2, 3, 4, 5, 6, 6]
repetidos = Counter(lista)
print(f'Contador: {repetidos}')

# Usar defaultdict para valores por defecto
mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'azul'
print(mi_dic['dos'])  # Devuelve 'nada' porque la clave no existe

# Usar namedtuple para definir un tipo de dato
Persona = namedtuple('Persona', ['Nombre', 'Altura', 'Peso'])
guillermo = Persona('Guillermo', 1.76, 88)
print(guillermo.Nombre, guillermo.Peso)
