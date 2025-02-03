# Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do 
# triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua 
# área.

import math 

class Triangulo:

    #Construtor da classe Triangulo
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
      

    #Verificar
    def Verificar(self):
        if(  (self.ladoA < ( self.ladoB + self.ladoC ))) and (self.ladoB < (self.ladoA + self.ladoC)) and (self.ladoC < (self.ladoA + self.ladoB)):
            print("O triangulo e valido")
        else:
            print("O triangulo não e valido")

    def calcular_area(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        area = math.sqrt( perimetro * ((perimetro-self.ladoA) * (perimetro-self.ladoB) * (perimetro-self.ladoC))  ) 
        print(area)

        


triangulo = Triangulo(5,10,9)

triangulo.Verificar()
triangulo.calcular_area()