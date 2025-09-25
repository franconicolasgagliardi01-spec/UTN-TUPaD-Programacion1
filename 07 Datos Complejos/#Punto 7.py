#Punto 7
Parcial1 = {"Franco", "Pedro", "Nicolas", "Alejo"}
Parcial2 = {"Nicolas", "Pedro", "Adrian", "Juan"}
lista = []

print("Aprobaron ambos parciales: ")
for i in Parcial1:
    for j in Parcial2:
        if i == j:
            print(j)
            lista.append(j)

print("Aprobaron un parcial: ")
for i in Parcial1:
    if i not in lista:
        print(i)

for i in Parcial2:
    if i not in lista:
        print(i)

Aprobados = list(Parcial1) + list(Parcial2)
Aprobados = set(Aprobados)

print(f"Aprobados totales: \n {Aprobados}")