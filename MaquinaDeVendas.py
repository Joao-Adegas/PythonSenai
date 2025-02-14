
#   Crie uma classe chamada “MáquinaDeVendas” que simule uma máquina de venda de 
# produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para 
# compra, inserir dinheiro, retornar o troco e exibir o estoque disponível. 

class Produtos:
    def __init__(self,priceproduct,nameProduct,quantityProduct):
        self.priceProduct = priceproduct
        self.nameProduct = nameProduct
        self.quantityProduct = quantityProduct

class SalesMachine:
    #comprar
    #inserir dinheiro
    #exibir estoque

    def __init__(self):
        self.products = []
        self.moneyQuantity = 0


    def insert_money(self,valor):
        self.moneyQuantity += valor
        print(f"Foi inserido R$\033[92m{self.moneyQuantity}\033[m na maquina")


    def registerProduct(self,nameProduct,priceProduct,quantityProduct):
        self.produto = Produtos(nameProduct,priceProduct,quantityProduct)
        print(f"Produto Registrado com sucesso\n{self.produto.nameProduct} - {self.produto.priceProduct}")

    def buy(self):
        self.insert_money(self.produto.priceProduct)
        self.produto.quantityProduct - 1
        



salesMachine = SalesMachine()
salesMachine.insert_money(10)
salesMachine.registerProduct("joao",10,2)
salesMachine.buy()