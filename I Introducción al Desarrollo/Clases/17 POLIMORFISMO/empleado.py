'''
empleado: sueldo base
empleado por comision: ventas * comision
empleado por hora: valor_hora_trabajada * horas_trabajadas * he*valor_hora_trabajada*2
'''

class Empleado:
    def __init__(self, nombre, NIT) -> None:
        self.nombre = nombre
        self.NIT = NIT

    def calcular_sueldo(self):
        return 1000

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, NIT, ventas, comision):
        super().__init__(nombre,NIT)
        self.ventas = ventas
        self.comision = comision

    def calcular_sueldo(self):
        return self.ventas * self.comision

class EmpleadoPorHora(Empleado):
        def __init__(self, nombre, NIT, horas, he, valor) -> None:
            super().__init__(nombre, NIT)
            self.horas = horas
            self.he = he
            self.valor = valor

        def calcular_sueldo(self):
            return self.horas * self.valor + self.he * self.valor * 2