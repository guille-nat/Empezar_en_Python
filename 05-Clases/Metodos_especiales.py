class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # Método especial para mostrar información sobre el objeto
    def __str__(self):
        return f'Álbum: {self.titulo} de {self.autor}'

    # Método especial para devolver el número de canciones
    def __len__(self):
        return self.canciones

    # Método especial para ejecutar al eliminar el objeto
    def __del__(self):
        print(f'Se ha eliminado el CD {self.titulo}')


# Crear una instancia y usar métodos especiales
mi_cd = CD('Pink Floyd', 'The Wall', 24)
print(mi_cd)  # Usar __str__()
print(len(mi_cd))  # Usar __len__()
del mi_cd  # Usar __del__()
