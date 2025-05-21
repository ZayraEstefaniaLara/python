def decorador(funcion):
    def funcionModificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcionModificada()

def saludo():
    print("hola soy zayra")
    
saludoModificado = decorador(saludo)

saludoModificado()