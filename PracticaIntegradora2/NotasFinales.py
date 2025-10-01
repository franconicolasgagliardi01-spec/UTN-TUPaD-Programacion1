def mostrarNotasFinales(notasAlumnos, alumnos):
    notasFinales = []
    legajo = list(notasAlumnos) #Creo arreglo con los legajos de los alumnos

    for i in range(len(legajo)): #Vario en cada alumno
        nota = [] #Areglo auxiliar
        materias = notasAlumnos[legajo[i]] #creo arreglo materias para trabajar
        suma = 0 #Variable que usare para sumar las notas de cada materia

        for j in range(len(materias)): #Sumo las materias
            suma = suma + materias[j][3]
    
        nota.append(alumnos[legajo[i]]) #Agrego el nombre del alumno
        nota.append(suma/len(materias)) #Agrego la nota final

        notasFinales.append(nota) #Agrego el arreglo con la nota y el nombre
    print("-----------------------------------------------------------")
    print("Las notas finales de los alumnos son: ")
    print("-----------------------------------------------------------")
    for i in range(len(notasFinales)): #Muestro las notas finales
        print(F"Alumno : {notasFinales[i][0]} \n Nota Final: {notasFinales[i][1]}")
    
    mayorNota = 0 #Variable para guardar la mayor nota final
    mejorAlumno = "" #Variable para guardar al alumno con mayor nota

    for i in range(len(notasFinales)): #Busco mejor alumno
        if mayorNota < notasFinales[i][1]:
            mayorNota = notasFinales[i][1]
            mejorAlumno = notasFinales[i][0]
    print("-----------------------------------------------------------")
    print(f"El alumno con mayor nota final es {mejorAlumno} con una nota de {mayorNota}")
    print("-----------------------------------------------------------")