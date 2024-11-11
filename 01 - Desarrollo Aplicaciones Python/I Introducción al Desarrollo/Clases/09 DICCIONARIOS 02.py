u1 = {
    'id': 1,
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'token': 'akfhgwieurksdhfskdfhkdghdfkghdfgwiere',
    'rol': {
        1: 'gerente', 2: 'admin',
    }
}
u2 = {
    'id': 2,
    'usuario': 'beto',
    'correo': 'beto@gmail.com',
    'token': 'sdfhksdfhsdfs897fslfkjsldf9sfjlsfjslf',
    'rol': {
        3: 'ventas', 4: 'user',5: 'rrhh',
    }
}
lista_usuarios = []
lista_usuarios.append(u1)
lista_usuarios.append(u2)
# como imprimir el correo de beto
diccionario_beto = lista_usuarios[1]
print(diccionario_beto['correo'])
# imprimir el rol de llave 2 de alicia
print(lista_usuarios[0]['rol'][2])
# como imprimir los roles de beto (llave y valor)
for k, v in lista_usuarios[1]['rol'].items():
    print(f'{k}: {v}')

lista2 = [{k:v} for k, v in lista_usuarios[1]['rol'].items() if k in [3, 5]]
print(lista2)
