#Punto 7
final = int(input("Ingrese el valor final: "))

while final < 1:
    print("EL FINAL NO PUEDE SER MAS PEQUEÑO QUE 0")
    final = int(input("ingrese el valor final: "))

sumatoria = 0

for i in range(0,final): 
    sumatoria = sumatoria + i

print(f"La suma de los numeros enteros comprendidos entre 0 y {final} es de: {sumatoria}")
