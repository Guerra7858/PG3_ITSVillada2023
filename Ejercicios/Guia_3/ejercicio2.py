
while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        division = num1 / num2
        print("La división de los números es:", division)
    except ZeroDivisionError:
        print("Error: no es posible dividir por cero.")
    respuesta = input("¿Desea seguir sumando valores? (s/n): ")
    if respuesta.lower() != 's':
        break