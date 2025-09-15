#Punto 5
def  segundos_a_horas(segundos):
    return segundos/3600

seg = int(input("Ingrese la cantidad de segundos: "))

print(f"{seg} segundos equivalen a {segundos_a_horas(seg)} horas")