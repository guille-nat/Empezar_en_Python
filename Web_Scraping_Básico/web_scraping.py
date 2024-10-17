import bs4
import requests

#resultado = requests.get('https://escueladirecta-blog.blogspot.com/2022/11/formato-de-fechas-en-strings.html') # de donde busca

#sopa = bs4.BeautifulSoup(resultado.text,'lxml') # para buscar la etiqueta

#print(sopa.select('title')[0].getText()) # pasarle el nombre de la etiqueta

#columna_lateral = sopa.select('.widget-content  a')
#for a in columna_lateral:
#    print(a.getText())

resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']

print(imagenes)

imagene_1 = requests.get(imagenes)
'''
f = open('C:\\Users\\maria\\OneDrive\\guille\\Escritorio\\mi_imagen.jpg', 'wb' )
f.write(imagene_1.content)
f.close()
'''