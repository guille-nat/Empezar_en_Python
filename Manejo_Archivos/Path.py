# crea o mueve archivos

#enumera archivos

#crear rutas basadas en strings

#crea también rutas jerarquicas de carpeta


    #-------------------------------------------------------------------------------#

from pathlib import Path

    #-------------------------------------------------------------------------------#

#genera el home (DIRECTORIO PRINCIPAL)
base =Path.home()
#print(base)
    #-------------------------------------------------------------------------------#

#construye objetos que parecen una ruta de acceso
#guia =  Path('Barcelona','Sagrada_Faminia')


    #-------------------------------------------------------------------------------#

#crea UNA RUTA ABSOLUTA
#guia = Path(base,'Barcelona','Sagrada_Faminia.txt')

    #-------------------------------------------------------------------------------#

#ruta relativa
#acepta tanto cadenas como objetos de Path  los une y pone las barras segun el so que tengas
#guia = Path(base,'Europa','España',Path('Barcelona','Sagrada_Familia.txt'))


    #-------------------------------------------------------------------------------#

#con la misma ruta del objeto guia pero entrando a otro archivo
#guia2 = guia.with_name('La_Pedrera.txt')
#print(guia2)

    #-------------------------------------------------------------------------------#

# devuelve el antecesor más inmediato en este caso 'Barcelona'
#print(guia.parent) se puede llamar varias veces a .parent

    #-------------------------------------------------------------------------------#

'''espa = Path(base,'Europa','España',Path('Barcelona','Sagrada_familia.txt'))
espa2 = espa.with_name('La_Pedrera.txt')
europa = espa.parent.parent.with_name('Consejos.txt')
europa2 = europa.with_name('Normativas.txt')

print(europa)
print(espa)
print(espa2)'''


    #-------------------------------------------------------------------------------#

#siempre y cuando vayan desde el home
'''guia = Path(Path.home(),'Europa')

for txt in Path(guia).glob('**/*.txt'):
    print(txt)'''

    #-------------------------------------------------------------------------------#
#si se desea recuperar una porcion de una ruta de archivos larga
guia = Path('Europa','España','Barcelona','Sagarda_familia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa','España'))
print(en_europa)
print(en_espania)