def muestraNotas(notasAlumnos, alumnos):
    print("-----------------------------------------------------------")
    print("Ingrese el legajo del alumno del que desea ver sus notas:")
    print("-----------------------------------------------------------")
    legajo = int(input())
    while legajo not in notasAlumnos: #Verifico el legajo
        print("EL LEGAJO INGRESADO NO EXISTE")
        print("-----------------------------------------------------------")
        print("Ingrese el legajo del alumno del que desea ver sus notas:")
        print("-----------------------------------------------------------")
        legajo = int(input())
    
    notas = notasAlumnos[legajo] #creo arreglo auxiliar para trabajar con las notas mas facil
    print("-----------------------------------------------------------")
    print(f"Las notas de {alumnos[legajo]} son: ")
    print("-----------------------------------------------------------")
    for i in range(len(notas)): #Vario en funcion de las materias
        print(f"{notas[i][0]}: ")
        print("-----------------------------------------------------------")
        for j in range(1,4): #Vario en funcion de las notas de la materia
            if j == 3:
                print(f"La nota final es: {notas[i][j]}") #Muestro notas
            else:
                print(f"La nota ({j}) es: {notas[i][j]}")
        print("-----------------------------------------------------------")
        
    maxNota = 0 # Variable que usare para guardar la nota mas alta
    mejorMateria = "" #Variable que usare para guardar la materia con la nota mas alta

    for i in range(len(notas)): #Veo cual es la mayor nota
        if notas[i][3] > maxNota:
            maxNota = notas[i][3]
            mejorMateria = notas[i][0]
    
    print(f"La materia con mejor nota del alumno es {mejorMateria}, con una nota de {maxNota}")