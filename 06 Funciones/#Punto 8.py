#Punto 8
def  calcular_imc(peso, altura):
    IMC = peso/altura**2 #Formula IMC
    return IMC

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura el metros: "))

print(f"Su IMC es de: {calcular_imc(peso,altura):.2f}") #:.2f indica que solo vamos a mostrar dos decimales, f es porque es float