#* args    #lo que hace es aceptar la cantidad cualquiera de argumentos que le pase el usuario



#ejemplo
def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(12,22,3,444,5,0))