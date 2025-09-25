#Punto 9
agenda = { ("lunes", "10:00"): "Reunion", 
        ("martes", "15:00"): "Clase de ingles"
        }

dia = input("Ingrese el dia(en minusculas): ")
hora = input("Ingrese la hora(Ej: 15:00): ")

print(f"El dia {dia} a las {hora}hs tienes: {agenda[dia,hora]}")