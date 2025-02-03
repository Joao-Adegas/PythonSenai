# Implemente uma classe chamada “Produto” que possua atributos para armazenar o 
# nome, o preço e a quantityProduct em estoque. Adicione métodos para calcular o valor 
# total em estoque e verificar se o produto está disponível.

class Produto:

    def __init__(self,nameProduct,priceProduct,quantityProduct):
        self.nameProduct = nameProduct
        self.priceProduct = priceProduct
        self.quantityProduct = quantityProduct

    # calculateValue - calcular valor total em estoque 
    def calculateValue(self):
        self.quantityProduct += self.quantityProduct
        print(self.quantityProduct)
    
    #checkAvailable - verificar disponibilidade
    def checkAvailable(self):
        if(self.quantityProduct < 1):
            print("Produto em falta")
        else:
            print(f"Produto disponivel {self.quantityProduct} em estoque")
        
    def __str__(self):
        return f"Nome: {self.nameProduct}\nPreco: {self.priceProduct}\nQuantidade: {self.quantityProduct}"


