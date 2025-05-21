class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def MostrarDatos (self):
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"Edad del estudiante: {self.edad}")
              
        

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def MostrarGrado(self):
        print(f"Grado estudiante: {self.grado}")
    
estudiante = Estudiante('Zayra', 19, '2do')

estudiante.MostrarDatos()
estudiante.MostrarGrado()


