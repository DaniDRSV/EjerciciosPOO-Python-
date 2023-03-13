from Peliculas import peliculas
from Categorias import categorias

class HBOstreaming(peliculas, categorias):
    pass
    def infoPelicula(catalogo):
        print (f"\nMenu pelicula \nPelicula: {peliculas.monja} \nCategoria: {categorias.catgTerror}")
    
HBOMax = HBOstreaming()

HBOMax.infoPelicula()