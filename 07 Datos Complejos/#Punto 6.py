#Punto 6
alumnos = {}

for i in range(3): 
    nombre = input(f"Ingrese el nombre del alumno ({i+1}) \n")

    nota1 = int(input(f"Ingrese la nota 1 del alumno ({i+1}) \n"))
    while nota1 < 0 or nota1 > 100:
        print("INGRESE UN VALOR VALIDO")
        nota1 = int(input(f"Ingrese la nota 1 del alumno ({i+1}) \n"))
    
    nota2 = int(input(f"Ingrese la nota 2 del alumno ({i+1}) \n"))
    while nota2 < 0 or nota2 > 100:
        print("INGRESE UN VALOR VALIDO")
        nota2 = int(input(f"Ingrese la nota 2 del alumno ({i+1}) \n"))

    nota3 = int(input(f"Ingrese la nota 3 del alumno ({i+1}) \n"))
    while nota3 < 0 or nota3 > 100:
        print("INGRESE UN VALOR VALIDO")
        nota3 = int(input(f"Ingrese la nota 3 del alumno ({i+1}) \n"))

    notas = (nota1, nota2, nota3)
    alumnos[nombre] = notas

seguir = True

while seguir:
    opcion = input("Desea ver el promedsio de un alumno? s/n")

    while opcion != "s" and opcion != "n":
        print("INGRESE UN VALOR VALIDO")
        opcion = input("Desea ver el promedsio de un alumno? s/n")

    if opcion == "s":
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print(f"El promedio de {nombre} es de {sum(alumnos[nombre])/3}")
        else:
            print("El nombre ingresado es invalido ")
    elif opcion == "n":
        seguir = False