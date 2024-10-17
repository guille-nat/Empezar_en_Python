'''
CAR          DESCRIPCION                EJEMPLO
\d          Dígito numérico             v\d.\d\d
\w          Caracter alfanumérico       \w\w\w-\w\w
\s          Espacio en blanco           numero\s\d\d
\D          No numérico                 \D\D\D\D\D
\W          No alfanumérico             \W\W\W
\S          no espacio en blanco        \S\S\S\S
'''
'''
CUANTIFICADORES

CAR         DESCRIPCION                 EJEMPLO
+           1 o más veces               código_\d-\d+
{n}         se repite n veces           \d-\d{4}
{n,m}       se repite de n a m veces    \w{3,5}
{n,}        desde n hacia arriba        -\d{4,}-
*           0 ó más veces               \w\s*\w
?           1 ó 0 (puede o no estar)    casas?
^           empieza con                 ^hola
'''

import re



texto = 'Si necesitas ayuda llama al 658-598-9977 las 24 horas al servicio de ayuda online'

#patron = 'ayuda'

#busqueda = re.search(patron,texto) #Busca la palabra ayuda en el txto
#print(busqueda)

patron = re.compile( r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)

#print(resultado.group(2))   #da el segundo termino

texto2 = 'No atendemos los Lunes por la mañana'
buscar = re.search(r'Lunes|Martes',texto2)  # | <-- significa O
print(buscar)