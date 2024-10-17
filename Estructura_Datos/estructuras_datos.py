"""Estructuras de datos. (if, for, while)."""

lista = ['Argentina', 'Francia', 'Dinamarca', 'Brasil']

# * For:
for i in lista:
    print(i)

# * If:

if "Argentina" in lista:
    print(f'Argentian esta en el indice {lista.index("Argentina")}\n')

x = 0

while x != 20:
    x += 1
    print(x)
