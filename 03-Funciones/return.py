# Función para multiplicar dos números
def multiplicar(numero1, numero2):
    """Devuelve el resultado de multiplicar dos números"""
    return numero1 * numero2

# Función para convertir USD a EUR


def usd_a_eur(usd):
    """Convierte dólares a euros usando una tasa de conversión fija"""
    conversion = usd * 0.99  # Tasa de conversión
    return conversion


# Pruebas
resultado = multiplicar(2, 50)
print(f'Resultado de la multiplicación: {resultado}')

dolares = 55
print(f'{dolares} USD en EUR son {usd_a_eur(dolares)} EUR')
