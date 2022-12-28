#Importaciones
from Personajes.enemigo import *
from Personajes.jugador import *

    
#Bucle principal
if __name__ == "__main__":

    print("Bienvenido a la mazmorra")
    nombre = input("Ingrese su nombre de jugador: ")

    #Personaje
    jugador = Jugador(nombre)

    print(f"Ha aparecido un {duende.nombre}. {jugador.nombre}, que deseas hacer?:")
    
    activo = True
    
    #Bucle del menu de opciones
    while activo == True:

        #Pidiendo respuesta
        try:
            print(f"Jugador: {jugador.nombre} (Vida:{jugador.vida} - {jugador.vida_maxima})")
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
            elif respuesta ==3:
                print("Inventario")
            else:
                print("Respuesta no valida")
            
        else:
            print("Respuesta no valida")

