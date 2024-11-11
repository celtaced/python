# Programa para calcular el factorial de un numero
# 5! = 5x4x3x2x1 = 120
numero = int(input('digite un numero: '))
factorial = 1

for i in range(1, numero+1):
    factorial *= i

print(f'El factorial de {numero} es: {factorial}')
