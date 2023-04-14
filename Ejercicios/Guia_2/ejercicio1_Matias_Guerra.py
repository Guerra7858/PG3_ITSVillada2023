class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(f"El nombre es {self.nombre}")

persona1 = Persona("Matias")
persona2 = Persona("Nahuel")

persona1.mostrar_nombre()
persona2.mostrar_nombre()
