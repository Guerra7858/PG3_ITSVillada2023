meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

while True:
    try:
        num_mes = int(input("Ingrese el número del mes (1-12): "))
        mes = meses[num_mes-1]
        print("El mes correspondiente es:", mes)
    except IndexError:
        print("Error: el número ingresado está fuera de rango.")

    respuesta = input("¿Desea seguir sumando valores? (s/n): ")
    if respuesta.lower() != 's':
        break
