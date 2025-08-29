#Punto 8
cantidad = int(input("Ingrese la cantidad de numeros que quiere cargar: "))

positivos = 0
negativos = 0
pares = 0
impares = 0

while cantidad < 1:
    print("INGRESE UNA CANTIDAD VALIDA")
    cantidad = int(input("Ingrese la cantidad de numeros que quiere cargar: "))

for i in range(cantidad):
    num = int(input(f"Ingrese el numero ({i+1}):"))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    
    if num%2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")