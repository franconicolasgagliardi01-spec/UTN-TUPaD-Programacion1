#Punto 4
def AgregarContacto(contactos):

    nombre = input("Ingrese el nombre del contacto: \n")

    while nombre in contactos:
        print("ESE NOMBRE YA ESTA EN USO")
        nombre = input("Ingrese el nombre del contacto: \n")
    
    numero = int(input("Ingrese el numero del contacto \n"))

    contactos[nombre] = numero

def VerificarContacto(contactos):
    nombre = input("Ingrese el nombre del contacto: \n")

    if nombre in contactos:
        print(f"El numero asociado a ese nombre es: {contactos[nombre]}")
    else:
        print("El nombre ingresado no existe en los contactos")

contactos = {}
seguir = True

while seguir == True:
    print("Seleccione una opcion:")
    opcion = int(input("1-Agregar Contactos\n2-Verificar Contacto\n3-Salir\n"))

    while opcion not in (1,2,3):
        print("SELECCIONE UNA OPCION VALIDA")
        opcion = int(input("1-Agregar Contactos\n2-Verificar Contacto\n3-Salir\n"))
    
    if opcion == 1:
        AgregarContacto(contactos)
    elif opcion == 2:
        VerificarContacto(contactos)
    elif opcion == 3:
        seguir = False
