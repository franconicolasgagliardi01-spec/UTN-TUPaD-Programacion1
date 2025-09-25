#Punto 5
Palabras = []
Recuento = {}

frase = input("Ingrese una frase u oracion, sin puntos ni comas: \n")
palabra = ""

for i in frase: #Creo lista que guarda todas las palabras de la frase
    if i != " ":
        palabra = palabra + i
    else:
        Palabras.append(palabra)
        palabra = ""
Palabras.append(palabra)

Palabras_unicas = set(Palabras) #Creo set sin palabras repetidas

largo = len(Palabras) #Guardo el largo de la lista Palabras

for i in range(largo): #Guardo en un diccionario la palabra junto con su cantidad
    contador = 0
    texto = Palabras[i]
    
    if texto not in Recuento:
        for j in range(largo):
            if texto == Palabras[j]:
                contador = contador + 1
            else:
                pass
        
        Recuento[texto] = contador

print(Palabras_unicas)
print(Recuento)