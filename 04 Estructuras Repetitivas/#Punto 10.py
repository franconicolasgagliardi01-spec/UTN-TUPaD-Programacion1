#Punto 10
num = int(input("Ingresa un numero: "))
mun = 0

while num >= 1:
    cifra = num % 10
    num = int(num/10)
    mun = mun*10 + cifra

print(f"El numero ingresado con los digitos invertidos es: {mun}")