#Punto 7
def operaciones_basicas(a, b):
    return (a+b,a-b,a*b,a/b) #devuelvo una tupla, que es un arreglo que no puede modificar su tamaño

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

tupla_op = operaciones_basicas(num1,num2) #Asigno el valor a tupla_op para guardar el resultado

print(f"El resultado de {num1} + {num2} = {tupla_op[0]}")
print(f"El resultado de {num1} - {num2} = {tupla_op[1]}")
print(f"El resultado de {num1} * {num2} = {tupla_op[2]}")
print(f"El resultado de {num1} / {num2} = {tupla_op[3]}")