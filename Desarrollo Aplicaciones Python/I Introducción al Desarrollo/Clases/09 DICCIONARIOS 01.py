# Diccionarios: par llave-valor
# nombre: 'alicia'

diccionario = {
    'usuario':'alicia',
    'correo': 'alicia@alicia.com',
    'token': 'asjasjalksjalkllksa'
}

print(diccionario)
print(len(diccionario))
print(diccionario['usuario'])

# Modificar Elementos
diccionario['usuario'] = 'eva'
print(diccionario['usuario'])

#Agregar Elementos
diccionario['Telefono'] = '22222222'
print(diccionario['Telefono'])

# Recorrer el diccionario
for valor in diccionario.values():
    print('-',valor)

# Eliminar elementos
diccionario.pop('usuario')

for llave in diccionario.keys():
    print('*',llave)

for k, v in diccionario.items():
    print(f'{k}: {v}')

# Validamos si usuario esta en diccionario
print('usuario' in diccionario)