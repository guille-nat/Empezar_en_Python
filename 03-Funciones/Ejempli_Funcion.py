# Buscar el café más caro en una lista de precios

precios_cafe = [('capuchino', 1.5), ('espresso', 1.2), ('moka', 1.9)]


def cafe_mas_caro(lista_precios):
    """Devuelve el café más caro y su precio"""
    cafe_mas_costoso, precio_mayor = lista_precios[0]  # Inicializamos con el primer café
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            cafe_mas_costoso = cafe
            precio_mayor = precio
    return cafe_mas_costoso, precio_mayor


# Prueba de la función
cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El café más caro es {cafe} con un precio de {precio}')

# las funciones pueden retornar dos valores
