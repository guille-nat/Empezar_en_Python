precios_cafe = [('capuchino',1.5),('exprresso',1.2),('moka',1.9)]

def cafe_mas_caro (lista_precios):
    band = True

    for cafe,precio in lista_precios:
        if band == True:
            precio_mayor = precio
            cafe_mas_costoso = cafe
            band = False

        elif precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_costoso = cafe
        else:
            pass
    return (cafe_mas_costoso,precio_mayor)

cafe,precio = cafe_mas_caro(precios_cafe)
print(f'El café mas caro es {cafe} cuyo precio es {precio}')


#las funciones pueden retornar dos valores