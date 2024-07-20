class Temperatura:
    def __init__(self,n1,n2,n3,n4,n5,n6,n7):
        self.lunes= n1
        self.martes= n2
        self.miercoles= n3
        self.jueves= n4
        self.viernes= n5
        self.sabado= n6
        self.domingo= n7
        self.total= ((n1 + n2 + n3 + n4 + n5 + n6 + n7)/7)
cal_temperaturas = Temperatura (22,23,24,25,26,27, 28)
print(cal_temperaturas.total)