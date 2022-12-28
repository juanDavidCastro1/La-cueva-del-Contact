#Importaciones
import random

#Clase del Jugador
class Jugador():
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 10
        self.energia = energia

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