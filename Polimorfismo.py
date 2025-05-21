class Gato():
    def sonido(self):
        return "miau"
    
class Perro():
    def sonido(self):
        return "guau"
    
def hacerSonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(perro.sonido())
print(gato.sonido())


hacerSonido(perro)