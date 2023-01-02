class Espada():
    def __init__(self, nombre, daño_base):
        self.nombre = nombre
        self.daño_base = daño_base
        self.movimiento = None

class Espada_de_hielo(Espada):
    def __init__(self, nombre, daño_base, movimiento):
        super().__init__(nombre, daño_base)
        self.movimiento = movimiento
    
    def congelar(self):
        self.daño_base = self.daño_base + 20
        return self.daño_base, self.movimiento

class Espada_de_fuego(Espada):
    def __init__(self, nombre, daño_base, movimiento):
        super().__init__(nombre, daño_base)
        self.movimiento = movimiento
    
    def quemar(self):
        self.daño_base = self.daño_base + 20
        return self.daño_base, self.movimiento
    
    
    


#Espadas
espada_basica = Espada("Espada basica", 20)
espada_de_hielo = Espada_de_hielo("Espada de hielo", 20, "Congelar")
espada_de_fuego = Espada_de_fuego("Espada de fuego", 40, "Quemar")


list = []
list.append(espada_de_fuego.quemar.__name__)

print(list)