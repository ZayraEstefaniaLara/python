class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
             #esto es un getter y aqui muestra coo acceder aun atributo privado
    def get_nombre(self):      
      return self.__nombre
  
    def set_nombre(self, newNombre):  #setter  para cambiar el atrivuto
      self.__nombre = newNombre

dalto = Persona('Lucas', 21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre ("Zayra Bonita") #se cambio el nombre del atributo con el setter

nombre = dalto.get_nombre()
print(nombre)