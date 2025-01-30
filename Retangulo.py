class Retangulo:

    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    #calcular area
    def CalcularAltura(self):
        return self.altura*self.largura
    
    #calcular perimetro
    def CalcularPerimetro(self):
        perimetro = 2*(self.altura + self.largura)
        return perimetro

