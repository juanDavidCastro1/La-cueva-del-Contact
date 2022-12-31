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
    slime = Enemigo("Slime", 50, 6, 4, 5)

    print(f"Ha aparecido un {slime.nombre} (vida:{slime.vida} | ataque:{slime.ataque}). {jugador.nombre}, que deseas hacer?\n")
    
    activo = True
    
    #Bucle del menu de opciones
    while activo:
        activo = batalla_jugador_enemigo(jugador, slime)

