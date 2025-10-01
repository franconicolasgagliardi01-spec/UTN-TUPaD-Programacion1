from GestionarNotas import gestionNotas
from MostrarNotas import muestraNotas
from NotasFinales import mostrarNotasFinales

alumnos = {
    60902 : "Rodolfo Fernandez",
    61654 : "Luis Gomez",
    61852 : "Andrea Pereira",
    61754 : "Juan Cruz Gonzales"
}

notasAlumnos = {} #Diccionario donde guardare las notas de cada alumno

deVuelta = [False]
apagar = False

while apagar == False:
    print("-----------------------------------------------------------")
    print("Seleccione una opcion: \n a) Gestionar notas \n b) Mostrar notas \n c) Salir")
    print("-----------------------------------------------------------")
    opcion = input()
    while opcion != "a" and opcion != "b" and opcion != "c":
        print("SELECCIONE UNA OPCION VALIDA (a) o (b) o (c)")
        print("-----------------------------------------------------------")
        print("Seleccione una opcion: \n a) Gestionar notas \n b) Mostrar notas \n c) Salir")
        print("-----------------------------------------------------------")
        opcion = input()
    
    if opcion == "a":
        notasAlumnos = gestionNotas(alumnos, notasAlumnos, deVuelta)
    elif opcion == "b":
        if deVuelta[0] == True:
            muestraNotas(notasAlumnos, alumnos)
        else:
            print("No se han ingresado notas todavia")
    elif opcion == "c":
        if deVuelta[0] == True:
            mostrarNotasFinales(notasAlumnos, alumnos)
            apagar = True
        else:
            print("No se ingresaron notas")
            apagar = True