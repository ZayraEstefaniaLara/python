class Pisto: 
    def __init__(self,hielera,hielera2):
         self.__hielera = hielera
         self.hielera2 = hielera2

    def pistear(self):
        self.__hielera ="vaciar"
        return self.__hielera
    
    def pistear2(self):
     self.hielera2="Mtha. esta vacia"
     return self.hielera2

fiesta=Pisto("Cartón en hielera","Unas cuantas frías")
print(fiesta.pistear_2())
print(fiesta.pistear_1())