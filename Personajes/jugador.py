#Importaciones
import random
from Armas.espada import *
from Objetos.pociones import *

#Clase del Jugador
class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.vida_maxima = 100
        self.ataque = 10
        self.energia = 50
        self.energia_maxima = 50
        self.arma_actual = None

    #Ataque del jugador
    def atacar(self, enemigo, jugador):

        #Calculando probabilidad de escape
        probabilidad_ataque_jugador = random.randint(1,10)
        probabilidad_ataque_enemigo = random.randint(1, enemigo.probabilidad_de_ataque)

        #Conparando las probabilidades
        if probabilidad_ataque_jugador > probabilidad_ataque_enemigo:
            print("Atacaste!!")
            try:
                enemigo.vida = enemigo.vida - (self.ataque + self.arma_actual.daño_base)
            except:
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
    
    #Inventario
    def inventario(self):
        inventario = {
            "armas": [
                espada_basica
            ],
            "pociones":[
                
            ]
        }


        activo = True

        #Bucle principal en el menu del inventario       
        while activo:

            print("\n--Inventario--")
            print("1.Armas 2.Pociones 3.Salir")

            #Pidiendo opcion del inventario
            try:
                opcion = int(input("Eliga una opcion: "))
            except:
                opcion = 0

            if type(opcion) == int:

                #Armas
                if opcion == 1:
                    

                    contador = 0

                    #Trayendo y mostrando armas del inventario
                    for armas in inventario["armas"]:
                        contador = contador + 1
                        print(f"{contador}-{armas.nombre}")

                    #Bucle secundario en el menu del inventario
                    while True:

                        #Elegiendo arma
                        try:
                            arma_elegida = int(input("Eliga un arma: "))
                        except:
                            arma_elegida = str
                            
                        if type(arma_elegida) == int and arma_elegida <= contador:
                            self.arma_actual = armas
                            break
                        else:
                            print("Opcion no valida")
                    

                #Pociones
                elif opcion == 2:
                    contador = 0

                    for pociones in inventario["pociones"]:
                        contador = contador + 1
                        print(f"{contador}-{pociones.nombre}")
                
                #Salir
                elif opcion == 3:
                    print("\n")
                    activo = False
                else:
                    print("Opcion no valida")
            else:
                print("Opcion no valida")