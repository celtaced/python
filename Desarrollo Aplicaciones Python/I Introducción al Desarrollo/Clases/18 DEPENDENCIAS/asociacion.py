class Cliente:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

class Prestamo:
    def __init__(self, interes: float, plazo:int, monto: float, cliente: Cliente) -> None:
        self.__interes = interes
        self.__plazo = plazo
        self.__monto = monto 
        self.__cliente = cliente
    def calcular_cuota(self):
        pass

c = Cliente('alicia')
p = Prestamo(0.1, 12, 2000, c)