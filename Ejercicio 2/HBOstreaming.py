from Peliculas import peliculas
from Categorias import categorias
from Peliculas import catalogo
from Categorias import categoria

class HBOstreaming(peliculas, categorias):
    pass
    def infoPeliculas():
        return f"Pelicula: {peliculas.monja} \nCategoria: {categorias.catgTerror}"
    
HBOMax = HBOstreaming()

print(HBOMax.infoPeliculas())