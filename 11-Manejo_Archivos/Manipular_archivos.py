mi_archivo = open('prueba.txt') #para abrir un archivo, se escribe open() y dentro el nombre del archivo entre comillas ''
    #si el archivo se encuentra en otro lugar que no sea donde guardo mi codigo se pone la direccion del archivo.

            #siempre que abramos un archivo al final cerrarlo.

#print(mi_archivo.read())    #para leer mi archivo se usa .read() y para mostrarrlo solo ponemos un print.
'''una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)'''

'''for l in mi_archivo:
    print('Aqui dice: '+l)'''

#todas_las_lineas = mi_archivo.readlines() #lo combierte en lista, podemos usar las propiedades de listas.
#print(todas_las_lineas)


mi_archivo.close()
