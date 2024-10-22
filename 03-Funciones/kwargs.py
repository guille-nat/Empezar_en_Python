# Uso de **kwargs para aceptar argumentos de palabra clave

def prueba(num1, num2, *args, **kwargs):
    """Imprime los argumentos regulares, *args y **kwargs"""
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    # Imprimir los argumentos adicionales
    for arg in args:
        print(f'arg = {arg}')

    # Imprimir las palabras clave
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


# Prueba de la función con *args y **kwargs
args = [12, 4033, 22, 22222, 100]
kwargs = {'x': 'uno', 'g': 'cuatro', 'z': 'tres'}
prueba(12, 4033, *args, **kwargs)
