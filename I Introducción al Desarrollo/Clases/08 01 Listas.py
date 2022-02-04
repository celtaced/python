# Listas en python

nombres = ['diana', 'sanchez','carlos','dubon']

# Obtener el tamaño de la lista
print(nombres)
print(len(nombres))

# Acceder elementos por su posición 
print(nombres[1])

# Modificar un elemento
nombres[2] = 'carlitos'
print(nombres)

# Agregar elementos
nombres.append('James')

# Eliminar elementos
nombres.remove('carlitos') # remove indicar el valor
nombres.pop(2) # por posición
print(nombres)
# del(nombres[2]) # Otra función de Python y no del objeto

# Recorrer el array
for nombre in nombres:
    print(nombre)

# Limpiar una lista
nombres.clear()
print(nombres)

# Eliminar una lista
del(nombres)
print(nombres)