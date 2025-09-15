#Punto 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

num = int(input("Ingrese un numero para obtener su tabla de multiplicar: "))

tabla_multiplicar(num)