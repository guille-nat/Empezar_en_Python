"""Qué son los módulos en Python: Los módulos permiten dividir el código en varios 
archivos más manejables. Puedes importar funciones, clases, 
o variables de otros archivos en tu script actual, 
lo que facilita la organización y reutilización del código.

Organización: Si planeas tener varios módulos, 
es recomendable que los agrupes en una carpeta con un archivo __init__.py,
convirtiendo la carpeta en un paquete.
"""

# Importar la función saludar desde ModuloOcupado
from ModuloOcupado import saludar, despedirse

# Llamar a la función saludar
saludar()

# Llamar a la función despedirse (si se agregó)
despedirse()
