from operator import concat
from re import A


class Cuentas:
    
    def __init__(self):
        pass
    
    def crear_cuenta(self, dui, nombre, tipo):
        self.dui = dui
        self.nombre = nombre
        self.tipo = tipo
        self.numeroCuenta = concat(self.tipo,self.dui)
        self.saldo = 0
        self.estado = 'A'

    def cerrarCuenta(self):
        self.estado = 'C'
    
    def retirar(self,monto):
        if self.saldo > monto:
            self.saldo -= monto
            return ('OK')
        else:
            return('ERROR')
    def abono(self,monto):
        self.saldo += monto
    




        
    