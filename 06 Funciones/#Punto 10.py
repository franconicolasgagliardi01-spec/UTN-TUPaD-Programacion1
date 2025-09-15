#Punto 10
def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio

lista = []
for i in range(0,3):
    print(f"Ingrese el numero ({i+1}): ")
    num = int(input())
    lista.append(num)

a = lista[0]
b = lista[1]
c = lista[2]

print(f"El promedio de estos numeros es: {calcular_promedio(a,b,c)}")