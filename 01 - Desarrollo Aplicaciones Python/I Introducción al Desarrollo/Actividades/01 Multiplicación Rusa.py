# Ejercicio de Multiplicación Rusa
multiplicando = int(input('Ingrese multiplicando: '))
multiplicador = int(input('Ingrese multiplicador: '))
impar = 0
resultado = 0

print(multiplicando*multiplicador)

while multiplicando >= 1:
    impar = multiplicando % 2
    if impar != 0:
        resultado += multiplicador
    multiplicando //= 2
    multiplicador *= 2

print(f'resultado = {resultado}') 