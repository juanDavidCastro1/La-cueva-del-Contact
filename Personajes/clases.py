#Importaciones
import random

#Clase del Jugador
class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 10

    #Ataque del jugador
    def atacar(self, enemigo, jugador):
        probabilidad_ataque_jugador = random.randint(1,10)
        probabilidad_ataque_enemigo = random.randint(1, enemigo.probabilidad_de_ataque)

        if probabilidad_ataque_jugador > probabilidad_ataque_enemigo:
            enemigo.vida = enemigo.vida - self.ataque
            return print(f"La vida restante del {enemigo.nombre} es {enemigo.vida}")
        else:
            print("Fallaste!!")
            print(f"El {enemigo.nombre} ataco!!")
            enemigo.atacar(jugador)
        
    
    #Huir del jugador
    def huir(self, probabilidad_enemigo):
        probabilidad_jugador = random.randint(1,10)
        if probabilidad_jugador > probabilidad_enemigo:
            print("Escapaste!!")
            return True
        else:
            print(f"Tu probabilidad de escape es {probabilidad_jugador} y la del tu enemigo es {probabilidad_enemigo}. No puedes escapar!!")
            return False
        
        
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
        return print(f"La vida restante de {jugador.nombre} es {jugador.vida}")

    


#NPCS y Enemigos
duende = Enemigo("Duende", 50, 6, 4, 5)