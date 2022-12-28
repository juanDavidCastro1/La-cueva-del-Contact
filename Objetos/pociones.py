class Pocion():
    def __init__(self, nombre, precio, curacion):
        self.nombre = nombre
        self.precio = precio
        self.curacion = curacion
    
    def curar(self, jugador):
        jugador.vida = jugador.vida + self.curacion
    

class Pocion_azul(Pocion):
    def __init__(self, nombre, precio, curacion):
        super().__init__(nombre, precio, curacion)
        self.curacion + 20


#Pociones
pocima_basica = Pocion("Pocion basica", 10, 20)
pocion_azul = Pocion_azul("Pocion azul", 20, 15)