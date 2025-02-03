# Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
# a altura. Implemente métodos para calcular a área e o perímetro do retângulo. 

class Retangulo:

    #definindo o construtor da classe Retangulo
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    #calcular area
    def CalcularAltura(self):
        res = self.altura*self.largura
        print(res)
    
    #calcular perimetro
    def CalcularPerimetro(self):
        perimetro = 2*(self.altura + self.largura)
        print(perimetro)


#definindo o objeto da classe Retangulo 
retangulo = Retangulo(3,9)

retangulo.CalcularAltura()
retangulo.CalcularPerimetro()
