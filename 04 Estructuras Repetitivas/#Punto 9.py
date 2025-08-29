#Punto 9
cantidad = int(input("Ingrese la cantidad de numeros que quiere cargar: "))

while cantidad < 1:
    print("INGRESE UNA CANTIDAD VALIDA")
    cantidad = int(input("Ingrese la cantidad de numeros que quiere cargar: "))
sumatoria = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el numero ({i+1})"))
    sumatoria = sumatoria + num

media = sumatoria/cantidad

print(f"La media de los numeros ingresados es: {media}")