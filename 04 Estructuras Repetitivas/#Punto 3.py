#Punto 3
inicio = int(input("Ingrese el valor de inicio: "))
final = int(input("Ingrese el valor final: "))

while final < inicio:
    print("EL FINAL NO PUEDE SER MAS PEQUEÑO QUE EL INICIO")
    final = int(input("ingrese el valor final: "))

sumatoria = 0

for i in range(inicio+1,final): #Le sumo un 1 a inicio para que no me tome ese valor
    sumatoria = sumatoria + i

print(f"La suma de los numeros enteros comprendidos entre {inicio} y {final} es de: {sumatoria}")

