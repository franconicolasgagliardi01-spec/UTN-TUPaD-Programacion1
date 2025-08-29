#Punto 5
import random

num_azar = random.randint(0,9)
intentos = 0
num = -1
print("¡Trata de adivinar el numero entre 0 y 9!")

while num != num_azar:
    num = int(input("Ingrese un numero: "))
    intentos += 1
    if num == num_azar:
        print(f"¡Lo has logrado! Te ha tomado {intentos} intento/s")
    else:
        print("Incorrecto. Intentalo de nuevo")