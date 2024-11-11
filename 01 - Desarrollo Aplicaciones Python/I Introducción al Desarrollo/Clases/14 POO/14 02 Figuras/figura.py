class Figura:
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(f'la figura es: {self.nombre}')