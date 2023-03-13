class Jugador1:
    nombreJugador = "Daniel"
    nombrePokemon = "Blastoise"
    saludPokemon = 100
    velocidadPokemon = 78
    
    def elegirPokemon(nombrePokemon):
        return f"{nombrePokemon}, yo te elijo!"
    
Daniel = Jugador1

print(Daniel.elegirPokemon(Daniel.nombrePokemon))