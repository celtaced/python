from factura import Factura

def main():
    f1 = Factura('A1','alicia',100)
    print(Factura.cantidad_facturas)
    f2 = Factura('A2','beto',200)
    print(Factura.cantidad_facturas)
    f3 = Factura('B1','eva',300)
    print(Factura.cantidad_facturas)

    print(f'f1: cant>{f1.cantidad_facturas} idfactura>{f1.factura}')
    print(f'f2: cant>{f2.cantidad_facturas} idfactura>{f2.factura}')
    print(f'f3: cant>{f3.cantidad_facturas} idfactura>{f3.factura}')

    Factura.mostrar_cantidad_facturas()

    lista = [f1,f2,f3]
    print(f'la suma es: {Factura.sumar_facturas(lista)}')

    

if __name__ == '__main__':
    main()

