# Recursividad es una función que se llama a si misma
# Siempre debe haber un caso base que detiene las llamadas recursivas
# Recursividad es una alternativa a las estructuras repetitivas
# Consumen muchos recursos de procesamiento 

'''
Este ejempolo generar un error de que se llama la función muchas veces
def sum():
    sum()
sum()
'''

# Ejercicio de factorial
# 5! = 5x4x3x2x1 = 120

def factorial(n):
    if n==1:
        return 1
    return factorial(n-1)*n

print(factorial(5))