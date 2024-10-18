#no se pueden modificar y ocupan m enos espacio en la memoria que las listas
#poseen índices (se cuentan de izquierda a derecha)

#mi_tuple = (1,2,(10,20),4)        #pueden tener cualquier tipo de objeto e incluso se pueden convinar

#mi_tuple = list(mi_tuple)  #se pueden modificar mediante asignacion como un tipo distinto

#print(mi_tuple[2][0])   #igual a listas y diccionarios


t = (1,2,3,1)


#print(t.count(1))           #permite contar cuantas veces esta ese objeto en tu tuple

print(t.index(2))