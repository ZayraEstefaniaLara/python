class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property                     #decorador para acceder al valor de un atrivuto privado
    def nombre(self):
        return self.__nombre
    
    
    @nombre.setter               #Decorador para cambiar un valor de un atrivuto privado
    def nombre(self, newNombre):
        self.__nombre = newNombre
        
        
    @nombre.deleter            # del     es un operador que nos elimina valores 
    def nombre(self):
        del self.__nombre
    
dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

# dalto.nombre = "Pepe"
# nombre = dalto.nombre
# print(nombre)

del dalto.nombre