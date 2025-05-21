class Estudiante:
    def __init__(self,nombre,edad,grado):
     self.nombre = nombre
     self.edad = edad
     self.grado = grado
     
     def estudiar(self):
         print(f"el estudiante{estudiante1.nombre} esta estudiando")
     
nombre = input("Cual es tu nombre? ")
edad = input("Cual es su edad? ")
grado = input ("Cual es su grado? ")

estudiante1 = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE
      Nombre: {estudiante1.nombre}
      Edad: {estudiante1.edad}
      Grado: {estudiante1.grado}
      
       """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
      estudiante1.estudiar()


