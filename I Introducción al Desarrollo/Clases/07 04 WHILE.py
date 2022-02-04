# Programa para calcular el factorial de un numero
# 5! = 5x4x3x2x1 = 120
numero = int(input('digite un numero: '))
factorial = 1

i = 1
while i<=numero:
    factorial *= i
    i+= 1

print(f'El factorial de {numero} es: {factorial}')