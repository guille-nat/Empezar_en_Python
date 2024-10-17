# kwargs significa palabra clave, trabaja con diccionarios

#primer ejemplo:
#def suma(**kwargs):
    #print(type(kwargs)) #transforma en diccionario
    #total = 0

   # for clave,valor in kwargs.items():  #usa las propiedades de los diccionarios
     #   print(f'{clave} = {valor}')
    #    total += valor
   # return total
#print(suma(x=2,y=5,=3))z


def prueba(num1,num2,*args,**kwargs):     #si se quiere usar todos estos se colocan en este orden
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [12,4033,22,22222,100]
kwaegs = {'x':'uno', 'g':'cuatro', 'z':'tres'}
prueba(12,4033,*args,**kwaegs)




