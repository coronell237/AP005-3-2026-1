while True:
    Numero = input("1Ingrese un numero entero: ")
    print("El numero que ingreso es:", Numero)

    mod = int(Numero) % 2

    if mod == 0:
        print("el numero es par")
    else:
        print("el numero es impAr")

    while True:
        print("\n-/-/-/-/---Menu---/-/-/-/")
        Opcion = input("Desea continuar? \n1. Para sí \n2. Para no\nSeleccione: ")

        if Opcion == "1":
            break
        elif Opcion == "2":
            exit()
        else:
            print("Opción no válida. Ingrese 1 o 2.")
