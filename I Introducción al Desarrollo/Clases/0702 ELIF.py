# Condicionales varias

edad = int(input('Digite su edad: '))

if edad > 0 and edad < 18:
    print('Es menor de edad')
elif edad >= 18 and edad < 60:
    print('Es mayor de edad')
elif edad >= 60 and edad < 115:
    print('Es de la tercera edad')
else:
    print('la edad no es válida')
