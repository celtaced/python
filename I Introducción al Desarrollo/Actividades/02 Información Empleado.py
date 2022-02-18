mensaje_introductorio = '\n***********************************\n'
mensaje_introductorio += '*      INFORMACION DE EMPLEADOS    \n'
mensaje_introductorio += '*          by Carlos Dubón         \n'
mensaje_introductorio += '***********************************\n'
mensaje_introductorio += '* Op. 1. Agregar Empleado         \n'
mensaje_introductorio += '* Op. 2. Imprimir Lista           \n'
mensaje_introductorio += '* Op. 3. Salir         \n'
mensaje_introductorio += '***********************************\n'
print(mensaje_introductorio)

opcion_seleccionada = 0
lista_empleados = []


while opcion_seleccionada != 3:
    opcion_seleccionada = float(input('Ingresa una opción:'))
    if opcion_seleccionada == 1:
        
        nuevo_empleado = {
            'nombre':'',
            'cargo': '',
            'sueldo': 0
        }
        
        print('\nINGRESO DE EMPLEADO')
        nuevo_empleado['nombre'] = input("Ingrese el Nombre: ")
        nuevo_empleado['cargo'] = input("Ingrese el Cargo: ")
        nuevo_empleado['sueldo'] = float(input("Ingrese el Salario: $"))
        lista_empleados.append(nuevo_empleado)
        print("Empleado Ingresado\n")
    elif opcion_seleccionada == 2:
        for empleado in lista_empleados:
            print(empleado)
        print('\n')
    elif opcion_seleccionada == 3:
        print('Saliendo')
    else:
        print('Opción no valida')