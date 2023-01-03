
class Espada():
    def __init__(self, nombre, daño_base):
        self.nombre = nombre
        self.daño_base = daño_base
        self.movimientos = None

class Espada_de_hielo(Espada):
    def __init__(self, nombre, daño_base):
        super().__init__(nombre, daño_base)
        self.movimientos = [
            [self.congelar.__name__],
            [self.congelar]
        ]
    
    def congelar(self):
        self.daño_base = self.daño_base + 20
        return self.daño_base


class Espada_de_fuego(Espada):
    def __init__(self, nombre, daño_base):
        super().__init__(nombre, daño_base)
        self.movimientos = [
            [self.quemar.__name__],
            [self.quemar]
        ]
    
    def quemar(self):
        self.daño_base = self.daño_base + 20
        return self.daño_base


#Espadas
espada_basica = Espada("Espada basica", 20)
espada_de_hielo = Espada_de_hielo("Espada de hielo", 20)
espada_de_fuego = Espada_de_fuego("Espada de fuego", 40)
