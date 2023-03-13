from Jugador1 import Jugador1
from Jugador2 import Jugador2

class Juego(Jugador1, Jugador2):
    def batallaPokemon():
        if(Jugador1.velocidadPokemon > Jugador2.velocidadPokemon):
            dmgRecibido = 30
            print(f"El {Jugador1.nombrePokemon} de {Jugador1.nombreJugador} ataca primero a {Jugador2.nombrePokemon} de {Jugador2.nombreJugador}")
            print(f"\n{Jugador1.nombrePokemon} \nSalud: {Jugador1.saludPokemon}")
            print(f"\n{Jugador2.nombrePokemon} \nSalud: {Jugador2.saludPokemon - dmgRecibido}")

        elif(Jugador2.velocidadPokemon > Jugador1.velocidadPokemon):
            dmgRecibido = 30
            print(f"El {Jugador2.nombrePokemon} de {Jugador2.nombreJugador} ataca primero a {Jugador1.nombrePokemon}  de {Jugador1.nombreJugador}")
            print(f"\n{Jugador1.nombrePokemon} \nSalud: {Jugador1.saludPokemon - dmgRecibido}")
            print(f"\n{Jugador2.nombrePokemon} \nSalud: {Jugador2.saludPokemon}")

batalla1 = Juego

batalla1.batallaPokemon()