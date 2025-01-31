# Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do 
# triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua 
# área. 

class Triangulo:

    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def Verificar(self):
        if( ((self.ladoB - self.ladoC) < self.ladoA and self.ladoA < ( self.ladoB + self.ladoC )) 
         and ((self.ladoA - self.ladoC) < self.ladoB and self.ladoB < (self.ladoA + self.ladoC)) 
         and ((self.ladoA - self.ladoB) < self.ladoC and self.ladoC < (self.ladoA + self.ladoB)) ):
            print("O triangulo e valido")
        else:
            print("O trisngulo não e valido")

triangulo = Triangulo(6,10,9)

triangulo.Verificar()