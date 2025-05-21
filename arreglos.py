from numpy import array
import numpy as np


class Arreglos:
    def _init_(self, arreglo):
        self.arreglo = np.array(arreglo)
        
        #Insertar elemento
        def insertar(self, arreglo):
            self.arreglo.insert(arreglo)
            
        def eliminar(self, indice):
            self.lista = np.delete(self.lista, indice)
        
        def modificar(self, indice, nuevo_elemento):
                self.lista[indice] = nuevo_elemento
                   
class listas:
    def _init_(self, lista):
        self.lista = lista
        
        lista = [1,2,3,4,5,6,7,8,9,10]
        lista_2 = lista
        #Insertar elemento
        def insertar(self, elemento):
            self.lista.append(elemento)
        #Eliminar elemento
        def eliminar(self, indice):
            self.lista.pop(indice) 
        #Modificar elemento
        def modificar(self, indice, nuevo_elemento):
            self.lista[indice] = nuevo_elemento