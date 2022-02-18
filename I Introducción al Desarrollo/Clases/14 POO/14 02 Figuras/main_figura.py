from rectangulo import Rectangulo
from circulo import Circulo

def main():
    r = Rectangulo('Rectangulo','rojo', 20, 10)
    c = Circulo('Circulo',4)
    r.mostrar_nombre()
    c.mostrar_nombre()
    print(f'el area del {r.nombre} es: {r.calcular_area()}')
    print(f'el perimetro del {r.nombre} es: {r.calcular_perimetro()}')
    print(f'el perimetro del {c.nombre} es: {c.calcular_perimetro()}')
    r.mostrar_color()

if __name__=='__main__':
    main()