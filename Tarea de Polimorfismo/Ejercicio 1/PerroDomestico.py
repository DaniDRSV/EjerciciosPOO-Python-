from Perro import Perro
from Perro import Perrito1

class perroDomestico(Perro):
    def acariciar():
        return f"Al acariciar a {Perrito1.nombre} se ha alegrado y te tiene mas confianza. Es un perro {Perrito1.estado}."

    def alimentar():
        return f"Alimentaste a {Perrito1.nombre}, ahora te tiene mas confianza."

DanielsDog = perroDomestico

print(DanielsDog.acariciar())
print(DanielsDog.alimentar())