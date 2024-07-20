class Alumno:
 # Inicializamos los atributos
    def __init__(self):
        self.nombre = input  ("Ingrese el nombre del alumno: ")
        self.nota = input ("Ingrese nota del alumno: ")
        print("")
    def imprimir(self):
        print("Alumno: ", self.nombre)
        print("Nota: ", self.nota)
        print("")


    def resultado(self):
        if int(self.nota) < 5:
            print("El alumno ha reprobado")
        else:
            print("El alumno ha aprobado")

alumno1 = Alumno()

alumno1.imprimir()
alumno1.resultado()