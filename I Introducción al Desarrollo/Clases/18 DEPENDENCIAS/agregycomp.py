# agregacion
class Contacto:
    pass
class Agenda:
    def __init__(self, contactos: list) -> None:
        self.__contactos = contactos

c1 = Contacto()
c2 = Contacto()
c3 = Contacto()
lista = [c1,c2,c3]
agenda = Agenda(lista)
agenda2 = Agenda([c3, c1])
# composicion
class Contacto:
    pass
class Agenda:
    def __init__(self) -> None:
        self.__contactos = []
    def agregar_contacto(self, contacto: Contacto):
        self.__contactos.append(contacto)

c1 = Contacto()
c2 = Contacto()
c3 = Contacto()
agenda = Agenda()
agenda.agregar_contacto(c1)
agenda.agregar_contacto(c2)
agenda.agregar_contacto(c3)