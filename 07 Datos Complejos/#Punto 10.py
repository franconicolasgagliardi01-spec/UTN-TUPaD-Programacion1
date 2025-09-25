#Punto 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}
lista = list(original)

for i in range(2):

    invertido[original[lista[i]]] = lista[i]

print(invertido)