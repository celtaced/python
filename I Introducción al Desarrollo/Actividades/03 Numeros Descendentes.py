def numeros_desendentes(n):
    if n==1:
        print(1)
        exit(numeros_desendentes)
    print(n)
    numeros_desendentes(n-1)

n = int(input('Ingrese un numero entero: '))
numeros_desendentes(n)
