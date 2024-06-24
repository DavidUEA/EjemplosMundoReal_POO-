#calcular el area del tringulo
#definimos la funcion calcular_area_triangulo y sus variables
def calcular_area_triangulo(base,altura):
#formula para calcular el area del triangulo
    area=((base*altura)/2)
    return area

#asignamos un valor a la variable
base=3
altura=5


area_triangulo=calcular_area_triangulo(base, altura)
print(area_triangulo)