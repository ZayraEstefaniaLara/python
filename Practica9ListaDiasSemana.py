#lista de los dias de la semana
#Poner valor string a cada dia
#Funcion donde reciba como parametro un valor contenido en enum

from enum import Enum 
from typing import Final

class DiasDeLaSemana(Enum):
    LUNES = "Lunes"
    MARTES = "Martes"
    MIERCOES = "Miercoles"
    JUEVES = "Jueves"
    VIERNES = "Viernes"
    SABADO  = "Sabado"
    DOMIMGO = "Domingo"

class VerificadorDia:
    def __init__(self,dia:DiasDeLaSemana):
        self.dia = dia
v=VerificadorDia("Martoles")
print(v.dia)
print("xd")

class Intento:
    MaxIntento:Final = 5