#Punto 8
stock = {"pan": 33, "tomate": 25}

continuar = True

while continuar:
    opcion = int(input("1-Consultar stock \n 2-Agregar stock \n 3-Salir \n"))
    while opcion != 1 and opcion != 2 and opcion != 3:
        print("VALOR INVALIDO")
        opcion = int(input("1-Consultar stock \n 2-Agregar stock \n 3-Salir \n"))
    
    if opcion == 1:
        producto = input("Ingrese el producto del que desea consultar stock: \n")
        if producto in stock:
            print(f"Stock: {stock[producto]}")
        else:
            print("El producto ingresado no existe")
    elif opcion == 2:
        producto = input("Ingrese el producto del que desea agregar stock: \n")
        cantidad = int(input("Cuanto desea agregar: \n"))
        while cantidad < 0:
            print("VALOR INVALIDO")
            cantidad = int(input("Cuanto desea agregar: \n"))
        
        stock[producto] = stock.get(producto,0) + cantidad
    elif opcion == 3:
        continuar = False