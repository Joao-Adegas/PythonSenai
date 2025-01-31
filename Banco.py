# Implemente uma classe chamada “Banco” que represente uma instituição financeira. 
# Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e 
# realizar operações como saques, depósitos e transferências.

import ContaBancaria
class Banco(ContaBancaria):

    def __init__(self,nome):
        self.nome_do_banco = nome
        self.contas = []

    def abrir_conta(self,nome):
        numero_da_conta = int(input("Digite o numero da conta"))
        cliente = ContaBancaria(ContaBancaria.ContaBancaria ,0,numero_da_conta)
        self.contas.append(cliente)
        print(f"conta bancaria aberta com sucesso {cliente}")

    
  

banco1 = Banco("Bradesco")


        
        
    


