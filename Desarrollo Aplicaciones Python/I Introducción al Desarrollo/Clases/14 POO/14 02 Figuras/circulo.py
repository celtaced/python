from figura import Figura

class Circulo(Figura):
    def __init__(self, nombre, diametro) -> None:
        super().__init__(nombre)
        self.diametro = diametro
        self.radio = diametro/2
        self.circunferencia = diametro * 3.1416

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio
