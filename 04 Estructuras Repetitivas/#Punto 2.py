#Punto 2
num = int(input("Ingrese un numero entero: "))
contador = 0
condicion = num
while condicion >= 1:
    condicion = int(condicion/10)
    contador += 1
print(f"El numero {num} tiene {contador} digito/s")