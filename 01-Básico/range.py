# Uso de range() en Python
# Recordar que Python comienza a contar desde el 0 y no incluye el ultimo número
# si queremos recorrer del 1 al 10 -> deberia de poner range(1,11) -> ya que no incluye el 11

# Generar números del 20 al 30, saltando de 2 en 2
for numero in range(20, 31, 2):
    print(numero)

# Crear una lista de números del 1 al 100
lista = list(range(1, 101))
print(lista)
