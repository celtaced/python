from persona import Persona

def main():
    alicia = Persona('alicia', 'diaz', 25, '8343274982')
    beto = Persona('beto', 'garcia', 27, '34782375289')

    print(f'nombre: {alicia.nombre}') # publico
    print(f'apellido: {alicia._apellido}') # protegido
    # print(f'edad: {alicia.__edad}') # privado no accesible fuera de la clase

    beto.mostrar_datos()
    # beto.__es_adulto() # metodo privado

if __name__=='__main__':
    main()