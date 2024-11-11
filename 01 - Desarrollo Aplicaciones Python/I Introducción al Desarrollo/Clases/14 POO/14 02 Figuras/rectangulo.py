from figura import Figura
from color import Color

class Rectangulo(Figura, Color):
    def __init__(self, nombre, color, base, altura) -> None:
        Figura.__init__(self,nombre)
        Color.__init__(self,color)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura

    def calcular_perimetro(self):
        return 2*(self.base+self.altura)