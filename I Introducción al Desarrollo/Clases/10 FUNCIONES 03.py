# programa para returnos multiples y multiples valores de retorno

def dias_mes(mes):
    if mes==12 or mes==7 or mes==8:
        return 31
    elif mes==4 or mes==6 or mes==11:
        return 30
    elif mes==2:
        return 28
    else:
        return 0

print(dias_mes(12))

def aritme(a, b):
    return a+b, a-b, a*b, a/b, 'hola', True, [2,3]

resultado = aritme(10,3)
print(type(resultado))
print(resultado[5])
