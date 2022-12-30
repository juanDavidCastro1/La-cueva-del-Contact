#Importaciones
from core.Personajes.enemigos import *
from core.Personajes.jugador import *
from core.engine import *

#Bucle principal
if __name__ == "__main__":

    print("Bienvenido a la cueva del Contact")
    nombre = input("Ingrese su nombre de jugador: ")

    #Personaje
    jugador = Jugador(nombre)

    print(f"Ha aparecido un {duende.nombre}. {jugador.nombre}, que deseas hacer?\n")
    
    activo = True
    
    #Bucle del menu de opciones
    while activo:

        activo = cursor_del_juego(jugador)

