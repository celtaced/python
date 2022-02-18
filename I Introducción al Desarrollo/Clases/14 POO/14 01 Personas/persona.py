# class Persona:
#     pass

# print(Persona)

# p = Persona()
# print(type(p)) # las clases son tipos definidos por el usuario

class Persona:
# Los nombres de las clases deben iniciar con mayuscula. 

    def __init__(self, nombre, apellido, edad, dui):
        self.nombre = nombre
        self._apellido = apellido
        self.__edad = edad
        self.__dui = dui

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}\n'
                f'Apellido: {self._apellido}\n'
                f'Edad: {self.__edad}, Adulto: {self.__es_adulto()}\n'
                f'DUI: {self.__dui}'
        )

    def __es_adulto(self):
        if self.__edad>=18:
            return True
        else:
            return False

