#Importaciones
from Personajes.enemigos import *
from Personajes.jugador import *

    
#Bucle principal
if __name__ == "__main__":

    print("Bienvenido a la cueva del Contact")
    nombre = input("Ingrese su nombre de jugador: ")

    #Personaje
    jugador = Jugador(nombre)

    print(f"Ha aparecido un {duende.nombre}. {jugador.nombre}, que deseas hacer?\n")
    
    activo = True
    
    #Bucle del menu de opciones
    while activo == True:

        #Comprobando si tiene arma equipada
        try:
            if jugador.arma_actual == None:
                arma = "No tiene arma equipada"
            else:
                arma = jugador.arma_actual.nombre
            
            #Pidiendo respuesta
            print(f"Jugador: {jugador.nombre} (Vida:{jugador.vida} - {jugador.vida_maxima} | Energia: {jugador.energia} - {jugador.energia_maxima} | Arma actaul: {arma})")
            respuesta = int(input("-- 1.Atacar 2.Huir 3.Inventario: "))
        except:
            respuesta = 0
        
        #Comprobacion de respuesta
        if type(respuesta) == int:
            if respuesta == 1:
                jugador.atacar(duende, jugador)
                if duende.vida <= 0:
                    activo = False
            elif respuesta == 2:
                if jugador.huir(duende):
                    activo = False
                else:
                    duende.atacar(jugador)
            elif respuesta == 3:
                jugador.inventario()
            else:
                print("Respuesta no valida")
            
        else:
            print("Respuesta no valida")

