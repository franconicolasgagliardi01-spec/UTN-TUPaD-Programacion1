#Punto 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

print(f"{celsius} grados Celsius equivalen a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")