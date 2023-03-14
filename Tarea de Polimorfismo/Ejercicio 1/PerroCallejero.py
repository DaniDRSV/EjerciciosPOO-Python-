from Perro import Perro
from Perro import Perrito2

class perroCallejero(Perro):
    def acariciar():
        return f"Al intentar acariciarlo te ha ladrado. Es un perro {Perrito2.estado}."

    def alimentar():
        return f"Alimentaste a {Perrito2.nombre}, ahora te tiene mas confianza."

callejero1 = perroCallejero

print(callejero1.acariciar())
print(callejero1.alimentar())