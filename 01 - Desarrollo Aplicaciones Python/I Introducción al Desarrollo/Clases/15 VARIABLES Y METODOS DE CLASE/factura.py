class Factura:

    # Variable de Clase
    cantidad_facturas = 0

    def __init__(self, factura, cliente, total) -> None:
        self.factura = factura
        self.cliente = cliente
        self.total = total
        Factura.cantidad_facturas += 1

    # Este método de Clase es accedido desde las clases heredadas
    @classmethod
    def mostrar_cantidad_facturas(cls):
        print(f'se ha generado {cls.cantidad_facturas} factura(s)')
    
    #
    @staticmethod
    def sumar_facturas(lista_facturas):
        total = 0
        for factura in lista_facturas:
            total += factura.total
        
        return total
