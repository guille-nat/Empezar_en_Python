
# Uso de *args para aceptar múltiples argumentos

def suma(*args):
    """Suma todos los números que se pasen como argumento"""
    total = 0
    for arg in args:
        total += arg
    return total


# Prueba de la función con varios números
print(suma(12, 22, 3, 444, 5, 0))
