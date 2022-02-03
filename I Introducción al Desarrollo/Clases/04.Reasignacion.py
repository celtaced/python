# Programa para operadores de reasignación

n = input('Ingrese un número: ')
print(type(n))
print('El valor ingresado es: ' + n)

n = int(n)
n += 10 # n = n + 10
print(n)
n -= 5 # n = n - 5

# Otros simbolos de reasignación:
# n *= 5 || # n = n * 5
# n /= 5 || # n = n / 5
# n //= 5 || # n = n // 5
# n %= 5 || # n = n % 5
# n **= 5 || # n = n ** 5

m = 10

print(f'el valor de n es {n} y el valor de m es {m}')
# Modo de formateo de todo el parámetro como texto