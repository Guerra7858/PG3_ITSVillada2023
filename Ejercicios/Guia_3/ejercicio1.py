while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La suma de los números es:", num1 + num2)
    except ValueError:
        print("Error: ingresó un valor no numérico.")
    respuesta = input("¿Desea seguir sumando valores? (s/n): ")
    if respuesta.lower() != 's':
        break