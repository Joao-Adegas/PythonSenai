# Implemente uma classe chamada “Produto” que possua atributos para armazenar o 
# nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
# total em estoque e verificar se o produto está disponível.

class Produto:

    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    #calcular valor total em estoque 
    def CalcularValorEstoque(self):
        self.quantidade += self.quantidade
        print(self.quantidade)
    
    def VerificarDisponibilidade(self):
        if(self.quantidade < 1):
            print("Produto em falta")
        else:
            print(f"Produto disponivel {self.quantidade} em estoque")


produto1 = Produto("banana",2.99,11)


produto1.CalcularValorEstoque()
produto1.VerificarDisponibilidade()

    