'''Qué es un decorador: Los decoradores son funciones que modifican otras funciones, añadiendo funcionalidad sin modificar el código original de la función decorada. Esto es útil para la reutilización y el código limpio.
Uso del @: El símbolo @ es una forma más directa de aplicar el decorador a una función sin tener que hacerlo manualmente.'''


# Ejemplo básico de un decorador en Python
def DecorarSaludo(funcion):
    """Un decorador que añade un saludo y una despedida"""
    def OtraFuncion(palabra):
        print('Holaaaa')
        funcion(palabra)
        print('Adiós')
    return OtraFuncion

# Funciones para ser decoradas


def Mayusculas(palabra):
    print(palabra.upper())


def Minuscula(palabra):
    print(palabra.lower())


# Usando el decorador manualmente
Mayuscula_Decorada = DecorarSaludo(Mayusculas)
Mayuscula_Decorada('hola soy guillermo')

# Usando el decorador con la sintaxis @


@DecorarSaludo
def Saludar(palabra):
    print(palabra)


# Llamada a la función decorada
Saludar('Decoradores son geniales')

# Decorador con múltiples funciones


@DecorarSaludo
def MinusculasDecoradas(palabra):
    print(palabra.lower())


MinusculasDecoradas('¡Python es poderoso!')
