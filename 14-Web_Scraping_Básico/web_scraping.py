# Importamos las bibliotecas necesarias:
# pip install beautifulsoup4 lxml
# pip install requests
# O en una sola linea: pip install requests beautifulsoup4 lxml
# - requests: Para hacer solicitudes HTTP y obtener el contenido de la página web.
# - bs4 (BeautifulSoup): Para analizar el HTML de la página y extraer datos.
import bs4
import requests

# Hacemos una solicitud GET para obtener el contenido de una página web.
# Cambia la URL a la página web que quieres analizar.
resultado = requests.get('https://www.escueladirecta.com/courses')

# Creamos un objeto BeautifulSoup con el contenido de la página web descargada.
# Usamos el analizador 'lxml' para procesar el HTML.
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Usamos BeautifulSoup para buscar la primera imagen de los cursos.
# '.course-box-image' es una clase CSS en la página web que contiene las imágenes de los cursos.
# '[0]' selecciona la primera imagen encontrada.
imagenes = sopa.select('.course-box-image')[0]['src']

# Imprimimos la URL de la primera imagen encontrada.
print(imagenes)

# Hacemos otra solicitud GET para descargar el contenido de la imagen.
# 'imagenes' contiene la URL de la imagen que queremos descargar.
imagene_1 = requests.get(imagenes)

# El siguiente código (comentado) guarda la imagen descargada en tu computadora.
# Descoméntalo para guardar la imagen.

'''
Explicación paso a paso:
Librerías:

requests: Se utiliza para hacer solicitudes HTTP y 
obtener el contenido de la página web.
BeautifulSoup (de bs4): Esta librería facilita el análisis de HTML y 
la búsqueda de elementos dentro de una página web.

Hacer una solicitud HTTP:

La función requests.get() realiza una solicitud a la URL proporcionada 
y descarga el contenido de la página.
Procesar el HTML con BeautifulSoup:

BeautifulSoup convierte el HTML descargado en un objeto que puede ser analizado. Usamos 'lxml' como analizador para trabajar con HTML y XML.

Buscar elementos HTML:

sopa.select('.course-box-image') busca todos los elementos en la página web 
que tienen la clase course-box-image. Esta clase contiene las imágenes 
de los cursos.
imagenes = sopa.select('.course-box-image')[0]['src'] obtiene la URL 
de la primera imagen (el primer elemento encontrado) y guarda su atributo src.
Descargar la imagen:

requests.get(imagenes) descarga la imagen desde la URL obtenida 
en el paso anterior.
El contenido de la imagen se guarda en imagene_1.content.
Guardar la imagen (opcional):

El código comentado guarda la imagen descargada en un archivo en tu computadora.
Cambia la ruta del archivo a donde quieras guardar la imagen antes 
de descomentar esta sección.
'''
