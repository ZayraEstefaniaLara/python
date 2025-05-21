import json
import requests

class GestorJson:
    def __init__(self,arch):
        self.arch = arch
        
    def LeerJson(self):
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
        
        except FileNotFoundError:
            print("Archivo no exixte")
            return{}
            
        except Json.JSONDecoderError:
            print("el archivon no es Json")
            return{}
        
        
    def escribirJson(self,datos):
        try:
            with open(self.arch, 'w') as f:
                return json.dump(datos, f, indent= 4)
        
        except FileNotFoundError:
            print("Archivo no exixte")
            return{}
            
        except json.JSONDecoderError:
            print("el archivon no es Json")
            return{}
        
    def modificarJson(self, llave, valor):
        datos = self.LeerJson
        datos[llave] = valor
        self.escribirJson(datos)
        
    def obtenerPokemon(self, pokemon):
        try:
              url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
              response = requests.get(url)
              response.raise_for_status()
              data = response.json()
              self.escribirJson(data)
              
              print("la informacion ya fue almacenaada")
              
        except requests.exceptions.HTTPError:
            print("El enlase no existe")
        
        except requests.exceptions.RequestException:
            print("No se pudo realizar la peticion")
            
GJson = GestorJson ("pokemmon.Json")
GJson.obtenerPokemon("Pikachu")

x = Pokemoninfo[name]
print(x)