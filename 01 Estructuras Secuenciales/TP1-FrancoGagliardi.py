#Punto 1
print("Hola Mundo!")
#Punto 2
nombre = input("Como te llamas?")
print(f"Hola {nombre}!")
#Punto 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
domicilio = input("ingrese su domicilio: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {domicilio}")
#Punto 4
import math
radio = float(input("Ingrese el radio del circulo: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio**2
print(f"El perimetro es: {perimetro} Y el area es: {area}")
#Punto 5
segundos = input("Ingrese una cantidad de segundos: ")
horas = int(segundos)/3600
print(f"{segundos} segundos equivale a {horas} horas")
#Punto 6
numero = int(input("Ingrese un numero: "))
print(f"{numero} * 1 = {numero}")
print(f"{numero} * 2 = {numero*2}")
print(f"{numero} * 3 = {numero*3}")
print(f"{numero} * 4 = {numero*4}")
print(f"{numero} * 5 = {numero*5}")
print(f"{numero} * 6 = {numero*6}")
print(f"{numero} * 7 = {numero*7}")
print(f"{numero} * 8 = {numero*8}")
print(f"{numero} * 9 = {numero*9}")
print(f"{numero} * 10 = {numero*10}")
#Punto 7
numero1,numero2 = float(input("Ingrese dos numeros distintos de 0: ")),float(input())
print(f"La suma de estos numero es: {numero1+numero2}, la resta es: {numero1-numero2}, la multiplicion: {numero2*numero1} y la division es: {numero1/numero2}")
#Punto 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en cm: "))
altura = altura/100
imc = peso/altura**2
print(f"Tu IMC es de: {imc}")
#Punto 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{celsius} grados Celsius equivalen a: {celsius*(9/5)+32} grados Fahrenheit")
#Punto 10
num1,num2,num3 = float(input("Ingrese tres numeros: ")), float(input()), float(input())
promedio = (num1+num2+num3)/3
print(f"El promedio de los tres numeros es de: {promedio}")