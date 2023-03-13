class Jugador2:
    nombreJugador = "Cristian"
    nombrePokemon = "Charizard"
    saludPokemon = 100
    velocidadPokemon = 100
    
    def elegirPokemon(nombrePokemon):
        return f"{nombrePokemon}, yo te elijo!"
    
Cristian = Jugador2

print(Cristian.elegirPokemon(Cristian.nombrePokemon))