class persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad  # privado
        self.sexo = sexo

    def presentarse (self):
        return f"{self.nombre} {self.apellido} {self.__edad} {self.sexo}"

#ejemplo Herencia
class estudiante(persona):
    def __init__(self, nombre, apellido, colegio, edad, sexo):
        super().__init__(nombre, apellido,edad, sexo)
        self.colegio = colegio

class estudiante2(persona):
    def __init__(self, nombre, apellido, edad, sexo, curso):
        super().__init__(nombre, apellido, edad, sexo)
        self.curso = curso

#Ejemplo polimorfismo

def imprimir_presentarse(persona):
    print(persona.presentarse())

# creación de objetos
estudiante1 = estudiante("David", "Smith", "Ecuador", 18, "masculino")
print(estudiante1.presentarse())
estudiante3 = estudiante2("Carlos", "Jarrin", 19,"masculino", "tercero")
print(estudiante3.presentarse())

#llamada polimorfismo
imprimir_presentarse(estudiante1)



