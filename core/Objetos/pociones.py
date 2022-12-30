class Pocion():
    def __init__(self, nombre, precio, curacion):
        self.nombre = nombre
        self.precio = precio
        self.curacion = curacion
    
    def curar(self, jugador):

        if jugador.vida < jugador.vida_maxima:
            if jugador.vida + self.curacion < jugador.vida_maxima:
                jugador.vida = jugador.vida + self.curacion
            else:
                jugador.vida = jugador.vida_maxima
            print("Se ha curado")
            return True
        else:
            print("Su vida esta llena")
            return False

        
    

class Pocion_azul(Pocion):
    def __init__(self, nombre, precio, curacion):
        super().__init__(nombre, precio, curacion)
        self.curacion + 20


#Pociones
pocima_basica = Pocion("Pocion basica", 10, 20)
pocion_azul = Pocion_azul("Pocion azul", 20, 25)