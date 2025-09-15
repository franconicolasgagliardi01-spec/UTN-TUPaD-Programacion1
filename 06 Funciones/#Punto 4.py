#Punto 4
import math

def calcular_area_circulo(radio):
    return math.pi*radio**2

def calcular_perimetro_circulo(radio):
    return 2*math.pi*radio

radio = float(input("Ingrese el radio del circulo: "))

print("El area del circulo es: ",calcular_area_circulo(radio))
print("El perimetro del circulo es: ",calcular_perimetro_circulo(radio))