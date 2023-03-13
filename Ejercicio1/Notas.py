from Estudiantes import Estudiante
from Materias import Materia
from Estudiantes import alumno01
from Materias import materia1

class notas(Estudiante, Materia):
    def __init__(self, notaLaboratorio, notaParcial):
        self.notaLaboratorio = notaLaboratorio
        self.notaParcial = notaParcial

    def notasFinales(self):
        return f"\n{alumno01.carrera}  Estudiante: {alumno01.nombre} {alumno01.apellido} \nMateria: {materia1.nombreMateria} \nNota Laboratorio: {self.notaLaboratorio} \nNota Parcial: {self.notaParcial}"


Matematica = notas(8, 10)

print(Matematica.notasFinales())