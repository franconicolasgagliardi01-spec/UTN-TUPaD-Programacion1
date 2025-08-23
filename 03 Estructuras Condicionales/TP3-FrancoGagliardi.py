#Punto 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Punto 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Punto 3
numpar = int(input("Ingrese un numero: "))
if numpar%2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Punto 4
edad = int(input("Ingrese su edad: "))
if edad < 12 and edad > 0:
    print("Es un niño")
elif edad >= 12 and edad < 18:
    print("Es un adolecente")
elif edad >= 18 and edad < 30:
    print("Es un adulto joven")
elif edad >= 30:
    print("Es un adulto")
else:
    print("Seleccione una edad valida")

#Punto 5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longcontraseña = len(contraseña)
if longcontraseña >= 8 and longcontraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Punto 6
from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #se calculan numeros aleatorios
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución irregular")

#Punto 7
frase = input("Ingrese una frase o palabra: ")
longfrase = len(frase)
letra = frase[longfrase-1] #De esta forma se saca una letra en especifico de un string
letra = letra.lower() #lower pone un string en minuscual, uper() en mayuscula
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    frase = frase + "!" #asi se pueden concatenar strings
print(frase)

#Punto 8
nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. ")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
opcion = int(input("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. "))
if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title() #title() convierte la primer letra del string en mayuscula
else:
    print("Ingrese una opcion valida")
print(nombre)

#Punto 9
magnitud = int(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3 and magnitud >= 0:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños). ")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles). ")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos). ")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")

#Punto 10
hemisferio = input("En cuál hemisferio se encuentra (N/S)? ")
mes = input("En que mes del año se encuentra? ")
dia = int(input("En que dia del mes se encuentra? "))
mes = mes.lower()
hemisferio = hemisferio.upper()
if (mes == "diciembre" and dia >= 21 and dia <= 31) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Invierno")
    elif hemisferio == "S":
        print("Verano")
elif (mes == "marzo" and dia >= 21 and dia <=31) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Primavera")
    elif hemisferio == "S":
        print("Otoño")
elif (mes == "junio" and dia >= 21 and dia <= 30) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Verano")
    elif hemisferio == "S":
        print("Invierno")
elif (mes == "septiembre" and dia >= 21 and dia < 30) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Otoño")
    elif hemisferio == "S":
        print("Primavera")
else:
    print("Ingrese bien los datos")