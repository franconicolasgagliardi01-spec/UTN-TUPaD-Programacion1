def gestionNotas(alumnos, notasAlumnos, deVuelta):

    if deVuelta[0]: #Se ejecuta si la funcion ya fue ejecutada anteriormente
        print("-----------------------------------------------------------")
        print("Desea cambiar las notas anteriormente ingresadas? si(s)/no(n)")
        print("-----------------------------------------------------------")
        opcion = input()
        while opcion != "s" and opcion != "n":
            print("INGRESE UNA OPCION VALIDA (s) o (n)")
            print("-----------------------------------------------------------")
            print("Desea cambiar las notas anteriormente ingresadas? si(s)/no(n)")
            print("-----------------------------------------------------------")
            opcion = input()
        if opcion == "s":
            deVuelta[0] = False
    
    if deVuelta[0] == False: #Se ejecuta cuando la funcion no fue nunca ejecutada o se decidio cambiar las notas
        legajos = list(alumnos) #Guardo los legajos(claves) del diccionario como arreglo

        for i in range(len(alumnos)): #Vario segun la cantidad de alumnos
            materias = [["Ciencias"],["Historia"],["Geografia"],["Matematicas"],["Fisica"]] #Reinicio la lista para reutilizarla
            print("-----------------------------------------------------------")
            print(f"Ingrese las notas de {alumnos[legajos[i]]}:") #alumnos[legajos[i] lo utilizo para acceder al nombre del alumno
            print("-----------------------------------------------------------")
            for j in range(len(materias)): #Vario en funcion de las materias
                print(f"{materias[j][0]}: ")

                nota1 = int(input("Ingrese la primer nota: \n"))
                while nota1 < 0: #Validacion de notas
                    print("INGRESE UN VALOR VALIDO")
                    nota1 = int(input("Ingrese la primer nota: \n"))

                nota2 = int(input("Ingrese la segunda nota: \n"))
                while nota2 < 0:
                    print("INGRESE UN VALOR VALIDO")
                    nota2 = int(input("Ingrese la segunda nota: \n"))
            
                notaFinal = int((nota1 + nota2)/2)

                materias[j].append(nota1) #Cargo las notas
                materias[j].append(nota2)
                materias[j].append(notaFinal)
            
            notasAlumnos[legajos[i]] = materias #Agrego la lista al diccionario
            deVuelta[0] = True #Constato de que ya use una vez al menos la funcion
    return notasAlumnos