# Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
# métodos para calcular a área e o perímetro do círculo.

import math

class Circulo:
    def __init__(self,raio):
        self.raio = raio 


    def AreaCirculo(self):
        area = math.pi*math.pow(self.raio, 2)
        print(f"Area do Circulo e {area}")
    
    def Perimetro(self):
        perimetro = (2*math.pi)*self.raio
        print(f"O perimetro do Circuloe {perimetro}")



    
