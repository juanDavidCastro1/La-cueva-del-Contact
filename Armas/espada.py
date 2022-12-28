
class Espada():
    def __init__(self, nombre, daño_base):
        self.nombre = nombre
        self.daño_base = daño_base

class Espada_de_hielo(Espada):
    def __init__(self, nombre, daño_base):
        super().__init__(nombre, daño_base)
    
    def congelar(self):
        self.daño_base = self.daño_base + 20
        return self.daño_base


#Espadas
espada_de_hielo = Espada_de_hielo("Espada de hielo", 30)


