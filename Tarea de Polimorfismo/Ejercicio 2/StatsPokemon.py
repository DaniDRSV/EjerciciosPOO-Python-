from Pokemon import Pokemon
from Pokemon import Pkmn0001

class statsPokemon(Pokemon):
    def mostrarInfoPokemon():
        return f"STATS POKEMON \nNombre: {Pkmn0001.nombrePokemon} \nTipo: {Pkmn0001.tipoPokemon}"
    
DanexPKSTA = statsPokemon

print(DanexPKSTA.mostrarInfoPokemon())