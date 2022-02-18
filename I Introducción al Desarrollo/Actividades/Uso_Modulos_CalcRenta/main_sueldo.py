from calculos import isr
from utilerias.variables import mensaje_menu, mensaje_introductorio

def main():
    print(mensaje_introductorio)
    print(mensaje_menu)
    op = int(input('Digite una opción: '))

    if op>=1 and op<=6:
        sueldo = float(input('Digite el Sueldo: '))
        if op==1:
            ISSS = isr.isss(sueldo)
            print(f'El descuento de ISSS es: $ {ISSS:.2f}')
        elif op==2:
            AFP = isr.afp(sueldo)
            print(f'El descuento de AFP es: $ {AFP:.2f}')
        elif op==3:
            ISR = isr.isr(sueldo)
            print(f'El descuento de ISR es: $ {ISR:.2f}')
        elif op==4:
            Descuentos = isr.descuentos(sueldo)
            print(f'El total de descuentos es: $ {Descuentos:.2f}')
        elif op==5:
            SG = isr.sueldo_gravable(sueldo)
            print(f'El sueldo gravable es: $ {SG:.2f}')
        elif op==6:
            SP = isr.sueldo_a_pagar(sueldo)
            print(f'El salario a pagar es: $ {SP:.2f}')
    else:
        print('Saliendo...')

if __name__ == '__main__':
    main()