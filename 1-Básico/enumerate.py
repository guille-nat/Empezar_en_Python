lista = ['a','b','c']
#for indice,item in enumerate(lista):       #enumera los items, en una especie e tupla
#    print(indice,item)
#for indice,item in enumerate(range(50,101)):       # se puede convinar
#    print(indice,item)

#mis_tuples = list(enumerate(lista))
#print(mis_tuples[1][0])
#print(mis_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):      #.startswith()  significa comienza con
        print(indice)