from Pokemon import Pokemon
from Pokemon import Pkmn0001

class Pokedex(Pokemon):
    def mostrarInfoPokemon():
        return f"POKEDEX \nNombre: {Pkmn0001.nombrePokemon} \nTipo: {Pkmn0001.tipoPokemon} \nDescripcion: {Pkmn0001.descripcionPokemon}"
    
DanexPKDEX = Pokedex

print(DanexPKDEX.mostrarInfoPokemon())