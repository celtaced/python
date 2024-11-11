from empleado import Empleado, EmpleadoPorComision, EmpleadoPorHora

def main():
    alicia = Empleado('alicia','123456789')
    beto = EmpleadoPorComision('beto','123456788',3000,0.3)
    eva = EmpleadoPorHora('eva','123456787',176,10.00,15)

    print(f'El sueldo de {alicia.nombre} es: {alicia.calcular_sueldo():.2f}')
    print(f'El sueldo de {beto.nombre} es: {beto.calcular_sueldo():.2f}')
    print(f'El sueldo de {eva.nombre} es: {eva.calcular_sueldo():.2f}')

    if isinstance(alicia,Empleado):
        print('alicia es de tipo Empleado')
    if isinstance(beto,Empleado):
        print('beto es de tipo Empleado')
    if isinstance(eva,Empleado):
        print('eva es de tipo Empleado')
    # Todos los objetos son instancia de de empleado, que es la clase padre

    if isinstance(eva, EmpleadoPorHora):
        print('eva es de tipo EmpleadoPorHora')
    # El objeto eva es instancia de EmpleadoPorHora

    if isinstance(eva,object):
        print('eva es de tipo object')
    # Todas las instancias de Python, son heredadas de Object


if __name__ == '__main__':
    main()