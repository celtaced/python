# Programa para funciones de argumentos variables

# Argumentos variables con lista
def listar_nombres(*nombres):
    print(nombres)
    for nombre in nombres:
        print(nombre)

listar_nombres('Alicia', 'Beto')
print('------------------------------------------------')
listar_nombres('Alicia', 'Beto', 'Eva','Camila','Diana')

# Argumentos variables con diccionario
def listar_terminos(**terminos):
    for k,v in terminos.items():
        print(f'Llave: {k}, valor: {v}')

print('------------------------------------------------')
listar_terminos(PK='Primary Key', FK='Foreing Key', UQ='Unique')