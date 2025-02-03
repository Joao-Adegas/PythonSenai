# Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas 
# online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de 
# compras, aplicar descontos e calcular o valor total da compra. 
from Produto import Produto

class OnlineStore():
    def __init__(self):
        self.products = []
        self.shoppingCart = []

    def generateShoppingCart(self):
        self.shoppingCart = []
        print(f"carrinho de compras gerado com sucesso")
        print(self.shoppingCart)

    def registerProducts(self,nameProduct,priceProduct,quantityProduct):
        self.product = Produto(nameProduct,priceProduct,quantityProduct)
        self.products.append(self.product)
        print("\n============= Registring Product ============\n"
              f"Name: \033[34m{nameProduct}\033[m \nPrice: : \033[32m {priceProduct}\033[m\nQuantity:{quantityProduct}\nAdded in system"
              "\n====================================")

    def addShoppingCart(self,nameProductSearch,quantityProductSearch):

        search = self.searchProduct(nameProductSearch)
    
        if(search):
            print("\n============ Adding Product ===========")
            self.shoppingCart.append({"nome":nameProductSearch,"quantidade":quantityProductSearch,"preco":self.product.priceProduct})
            print(f"Added product in shopping cart {quantityProductSearch} {nameProductSearch}")
            print("==============================================")
                
        else:
            print(f"Product {nameProductSearch} notfound")
    
    def listProducts(self):

         print("Produtos:\n")
         for i in self.products:
              print(
                    "==============================="
                    f"\n{i}\n"
                    "===============================")
        
    def applyDiscout(self,nameProduct,valueDiscout):

        search = self.searchProduct(nameProduct)

        if(search):
            newPrice = self.product.priceProduct - (valueDiscout/100)
            print(f"Applies discount successfully: {nameProduct} de {newPrice}")         
            
        else:
            print(f"Discount dont apply because product dont exist")

       
        
    def searchProduct(self, nameProduct):
        found = False  # Variável para rastrear se o produto foi encontrado
        for produto in self.products:
            if produto.nameProduct == nameProduct:
                found = True
                return produto
                break  # Se o produto for encontrado, interrompe o loop

        if not found:
            print(f"Product not found: {nameProduct}")
             
    def calculateShoppingCart(self):
        print("\n\n======== Seu Carrinho ========\n")
        total = 0
        for item in self.shoppingCart:
            nameProduct = item["nome"]
            priceProduct = item["preco"]
            print(f"\033[34m{nameProduct}\033[m - R$\033[32m{priceProduct}\033[m")
            total += item["preco"]*item["quantidade"]
        print(f"total purchase price: \033[32m{total}\033[m")


       
        

                 
                 
             
         


onlinestore = OnlineStore()
#registrando produtos no sistema
onlinestore.registerProducts("pepsi",2.99,20)
onlinestore.registerProducts("coca-cola",2.99,20)

#Adicionando produtos ao carrinho
onlinestore.addShoppingCart("pepsi",2)
onlinestore.applyDiscout("coca-cola",10)
onlinestore.addShoppingCart("coca-cola",2)

#calculando valor do carrinho
onlinestore.calculateShoppingCart()


