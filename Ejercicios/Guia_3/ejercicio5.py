try:
    with open('archivo.txt', 'w') as archivo:
        archivo.write('Hola\n')
        archivo.write('Mundo\n')
        archivo.write(123)  # intentamos escribir un entero
except TypeError:
    print("Error: no se puede escribir un entero en el archivo.")