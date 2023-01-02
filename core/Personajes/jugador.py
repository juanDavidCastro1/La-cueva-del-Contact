#Importaciones
import random
from ..Armas.espada import *
from ..Objetos.pociones import *

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

        global inventario
        inventario = {
            "armas": [
                
            ],
            "pociones":[

            ]
        }

    #Ataque del jugador
    def atacar(self, enemigo, jugador):

        #Calculando probabilidad de ataque
        probabilidad_ataque_jugador = random.randint(1,10)
        probabilidad_ataque_enemigo = random.randint(1, enemigo.probabilidad_de_ataque)

        #Conparando las probabilidades
        if probabilidad_ataque_jugador > probabilidad_ataque_enemigo:
            
            #if self.arma_actual != None:


            try:
                enemigo.vida = enemigo.vida - (self.ataque + self.arma_actual.daño_base)
            except:
                enemigo.vida = enemigo.vida - self.ataque

            if enemigo.vida <= 0:
                print(f"El {enemigo.nombre} ha muerto")
            else:
                print(f"La vida restante del {enemigo.nombre} es {enemigo.vida}\n")
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
    def inventario(self, jugador):


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
                    armas = ""
                    for armas in inventario["armas"]:
                        contador = contador + 1
                        if armas.movimiento == None:
                            armas.movimiento = "No tiene movimiento"
                        else:
                            pass
                        print(f"{contador}-{armas.nombre} (ataque: {armas.daño_base} | movimiento especial: {armas.movimiento})\n")

                    if armas == "":
                        print("No tiene armas en el inventario")
                    else:
                        #Bucle secundario en el menu del inventario
                        while True:

                            #Elegiendo arma
                            try:
                                print(f"Para salir escriba: {contador + 1}")
                                arma_elegida = int(input("Eliga un arma: "))
                            except:
                                arma_elegida = str
                                
                            if type(arma_elegida) == int and arma_elegida <= contador:
                                self.arma_actual = inventario["armas"][arma_elegida - 1]
                                break
                            elif arma_elegida == contador + 1:
                                break
                            else:
                                print("Opcion no valida")
                    

                #Pociones
                elif opcion == 2:
                    contador = 0
                    pociones = ""

                    for pociones in inventario["pociones"]:
                        contador = contador + 1
                        print(f"{contador}-{pociones.nombre} (coste: {pociones.precio}, curacion: {pociones.curacion})\n")
                    
                    if pociones == "":
                        print("No tiene pociones en el inventario")
                    else:
                        #Bucle secundario en el menu del inventario
                        while True:

                            #Elegiendo pociones
                            try:
                                print(f"Para salir escriba: {contador + 1}")
                                pocion_elegida = int(input("Eliga una pocion: "))
                            except:
                                pocion_elegida = str
                                
                            if type(pocion_elegida) == int and pocion_elegida <= contador:
                                if pociones.curar(jugador) == True:
                                    inventario["pociones"].pop(pocion_elegida - 1)
                                else:
                                    pass
                                
                                break
                            elif pocion_elegida == contador + 1:
                                break
                            else:
                                print("Opcion no valida")
                
                #Salir
                elif opcion == 3:
                    print("\n")
                    activo = False
                else:
                    print("Opcion no valida")
            else:
                print("Opcion no valida")