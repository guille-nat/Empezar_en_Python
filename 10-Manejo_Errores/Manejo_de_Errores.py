"""
Bloque try-except: Utiliza el bloque try-except para capturar y 
manejar errores en tiempo de ejecución. Específicamente,
except captura el tipo de error, 
lo que te permite reaccionar de manera adecuada según el error.

finally: El bloque finally siempre se ejecuta, 
independientemente de si ocurre un error o no.
Es útil para cerrar archivos o liberar recursos, 
asegurando que ciertas acciones se realicen siempre.

Especificar excepciones: Evita usar except genéricamente,
a menos que sea absolutamente necesario. 
Capturar errores específicos hace que tu código sea más robusto 
y fácil de depurar.
"""
# Función para sumar dos números con manejo de errores


def suma():
    """Pide dos números y muestra su suma, manejando posibles errores."""
    try:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
        print(f'La suma es: {n1 + n2}')
    except TypeError:
        print('Error: Estás intentando concatenar tipos distintos.')
    except ValueError:
        print('Error: Ese no es un número válido.')
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
    else:
        print('Has sumado correctamente.')
    finally:
        print('Eso fue todo.')


# Llamar a la función suma
suma()


# Función para pedir un número con manejo de errores en un bucle
def pedir_numero():
    """Pide un número al usuario hasta que ingresa un valor válido."""
    while True:
        try:
            numero = int(input('Dame un número: '))
        except ValueError:
            print('Ese no es un número válido.')
        else:
            print(f'Ingresaste el número {numero}.')
            break
        finally:
            print('Intento de entrada completado.')


# Llamar a la función pedir_numero
pedir_numero()
