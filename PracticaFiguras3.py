#Practica 3
#Programa de figuras unificando el calculo del area
#(Atributos y comportamientos)


from math import pi , tan , sqrt 

NL=int(input("Cuántos lados tiene la figura?"))
L= int(input("Cuánto mide cada lado?"))

class Figura:
    def perimetro(NL,L):
        p = NL * L
        return print("Perimetro= ",p)
    def a3(L):
        a=L*(sqrt((L**2)-((L/2)**2)))/2
        return print("Área del triángulo= ",a)   
    def a4(L):
        a=L*L 
        return print("Área del cuadrado= ",a) 
    def poly(NL,L):
        a=((NL*L*L)/(4*(tan(pi/NL))))
        return print("Área del polígono= ",a) 

Figura.perimetro(NL,L)

    
Figura.poly(NL,L)