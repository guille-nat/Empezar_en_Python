from random import *                    #con el * importa todo de la libreria
                                        #sino elegimos uno especifico

aleatorio = randint(1,50)   #desde donde a donde

aleatorio2 = round(uniform(1,5),1)      #uniform lo mismo que randint pero con num decimales

aleatorio3 = random()   #elije un numero decimal entre 0 y 1

colores = ['azul','gris','rojo','violeta']
aleatorio4 = choice(colores)                        #trabajar con elementos aleatorios con los elementos dentro de una lista


numeros = list(range(5,50,5))
shuffle(numeros)            #hace una mezcla aleatoria de numeros pero siempre respetando que pertenezcan a la lista
                            #genera una modificacion en el lugar

print(numeros)

