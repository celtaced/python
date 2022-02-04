# SET 
nombres = {'alicia', 'beto', 'camila', 'diana'}

print(nombres)
print(len(nombres))

# Son de tamaño estático
nombres.add('eva')
print(nombres)

nombres.discard('camila')
print(nombres)

# No se puede modificar, es inmutable
#nombres[0] = 'fran'

for nombre in nombres:
    print(nombre)

nombres.clear()
print(nombres)

# Frozenset
lenguajes = frozenset({1,2,5})
for leng in lenguajes:
    print('-',leng)


# Los set no aceptan valores
lista = [1,2,7,9,4,1,5,1]
conjunto = set(lista)
print(conjunto)