#Conjunto
conjunto = {1,2,3,4,5}
print(conjunto)

#Agregar un elemento repetido
conjunto.add(6)
print(conjunto)

#remueve un elemento y da un error si no lo encuentra
conjunto.remove(1)
print(conjunto)

#remueve un elememto y no hay error si no lo encuentra
conjunto.discard(2)
print(conjunto)

#verificar si un numero esta en la  lista (devueleve un bulean)
print(1 in conjunto)

#agregar un elemento que ya exista
conjunto.add(5)
print(conjunto)