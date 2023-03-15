from abc import ABC, abstractmethod

class Pokemon(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.tipo = []

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def esquivar(self, atacante):
        pass

    @abstractmethod
    def pokemonStatus(self):
        print(f"\nNivel: {self.nivel}")

class Pikachu(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.puntosDeSalud = 35
        self.ataque = 55
        self.velocidad = 90
        self.tipo = ["Electrico"]

    def pokemonStatus(self):
        super().pokemonStatus()
        print(f"{self.nombre}:   PS: {self.puntosDeSalud}")

    def atacar(self, objetivo):
        objetivo.puntosDeSalud -= self.ataque*0.8
        print(f"{self.nombre} ha atacado a {objetivo.nombre}")

    def esquivar(self, objetivo):
        if objetivo.velocidad < self.velocidad:
            print(f"{self.nombre} ha esquivado el ataque")
        else:
            print(f"{self.nombre} no ha podido esquivar el ataque")

class Onix(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.puntosDeSalud = 35
        self.ataque = 45
        self.velocidad = 70
        self.tipo = ["Roca", "Tierra"]

    def pokemonStatus(self):
        super().pokemonStatus()
        print(f"{self.nombre}:   PS: {self.puntosDeSalud}")

    def atacar(self, objetivo):
        objetivo.puntosDeSalud -= self.ataque*0.8
        print(f"{self.nombre} ha atacado a {objetivo.nombre}")

    def esquivar(self, objetivo):
        if objetivo.velocidad < self.velocidad:
            print(f"{self.nombre} ha esquivado el ataque")
        else:
            print(f"{self.nombre} no ha podido esquivar el ataque")

onix = Onix("Chimpilim")
pikachu = Pikachu("Shirairaichu")

pikachu.pokemonStatus()
onix.pokemonStatus()

onix.atacar(pikachu)
pikachu.esquivar(onix)
