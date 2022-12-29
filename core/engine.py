from .Personajes.jugador import *
from .Personajes.enemigos import *

def curso_del_juego(jugador):
    
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
                    return False
                else:
                    return True
            elif respuesta == 2:
                if jugador.huir(duende):
                    return False
                else:
                    duende.atacar(jugador)
                    return True
            elif respuesta == 3:
                jugador.inventario(jugador)
                return True
            else:
                print("Respuesta no valida")
                return True
            
        else:
            print("Respuesta no valida")
            return True