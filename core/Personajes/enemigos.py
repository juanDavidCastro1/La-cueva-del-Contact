#Importaciones      
        
#Clase del Enemigo
class Enemigo():
    def __init__(self, nombre, vida, ataque, probabilidad_escape , probabilidad_ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.probabilidad_de_escape = probabilidad_escape
        self.probabilidad_de_ataque = probabilidad_ataque
    
    #Ataque del enemigo
    def atacar(self, jugador):
        jugador.vida = jugador.vida - self.ataque
        return print(f"La vida restante de {jugador.nombre} es {jugador.vida}\n")

    

#NPCS y Enemigos
