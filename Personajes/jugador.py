#Importaciones
import random
from Armas.espada import *

#Clase del Jugador
class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.vida_maxima = 100
        self.ataque = 10
        self.energia = 50

    #Ataque del jugador
    def atacar(self, enemigo, jugador):
        probabilidad_ataque_jugador = random.randint(1,10)
        probabilidad_ataque_enemigo = random.randint(1, enemigo.probabilidad_de_ataque)

        if probabilidad_ataque_jugador > probabilidad_ataque_enemigo:
            print("Atacaste!!")
            enemigo.vida = enemigo.vida - self.ataque 
            return print(f"La vida restante del {enemigo.nombre} es {enemigo.vida}\n")
        else:
            print("Fallaste!!")
            print(f"El {enemigo.nombre} ataco!!")
            enemigo.atacar(jugador)
        
    
    #Huir del jugador
    def huir(self, enemigo):
        probabilidad_jugador = random.randint(1,10)
        if probabilidad_jugador > enemigo.probabilidad_de_escape:
            print("Escapaste!!")
            return True
        else:
            print(f"Esacape fallido!!")
            print(f"El {enemigo.nombre} ataco!!")
            return False
    
    def inventario():
        inventario = {
            "armas": {
                "espadas":{
                    "espada_basica": espada_basica
                }
            },
            "objetos":{

            } 
        }