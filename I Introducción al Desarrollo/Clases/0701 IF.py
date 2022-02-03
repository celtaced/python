# Programa para determinar si una persona es adulta
edad = int(input('Digite su edad: '))
if edad >= 18:
    print('Es mayor de edad')
    if edad >= 60:
        print('y es de la tercera edad')
    print('Saliendo del programa...')
else:
    print('Es menor de edad')
    print('Programa terminado')