# Abrir el archivo y leer todas las líneas
with open('prueba.txt', 'r') as mi_archivo:
    print(mi_archivo.read())  # Leer todo el archivo

# Leer el archivo línea por línea
with open('prueba.txt', 'r') as mi_archivo:
    for linea in mi_archivo:
        print(f'Aquí dice: {linea.strip()}')
