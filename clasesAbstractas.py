from abc import ABC, abstractclassmethod

class Persona (ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,trabajo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.trabajo = trabajo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacerActividad(self):
        pass
    
    def precentarse(self):
        print(f'Hola,me llamo:{self.nombre} y tengo {self.edad}años')
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacerActividad(self):
        print(f"Estoy estudianto: {self.actividad}")


dalto = Estudiante("Lucas",21,"Masculino","Programador")

dalto.hacerActividad()