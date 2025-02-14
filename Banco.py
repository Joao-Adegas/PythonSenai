# Implemente uma classe chamada “Banco” que represente uma instituição financeira. 
# Essa classe deve conter métodos para cadastrar clients, abrir accouts bancárias e 
# realizar operações como saques, depósitos e transferências.
import random
from ContaBancaria import ContaBancaria

class Banco:

    #Construtor 
    def __init__(self):
        self.accouts = []
        self.clients = []

    def client_register(self,clietName):
        client = [{"name":clietName}]
        self.clients.append(client)
        
    #Metodo para abrir conta
    def open_accout(self,nameHolder,balance,numberAccout):
        print("\n\033[32m================== Account create ===================\033[m")
        self.accout = ContaBancaria(nameHolder,numberAccout,balance)
        self.accouts.append(self.accout) 
        print(f"Name: \033[32m{nameHolder}\033[m\nBalance: \033[32m{balance}\033[m\nNumber accout: \033[32m{numberAccout}\033[m")
        print("\033[32m====================================================\033[m")

    #metodo para cer as accouts criadas    
    def see_accouts(self):
       for conta in self.accouts:
            print(f"conta: {conta}\n\n")

    
    def transfe(self, valor, sender_numberAccout, recipient_numberAccout):
        sender_account = None
        recipient_account = None

        # Encontrar as contas com base nos números fornecidos
        for conta in self.accouts:
            if conta.numberAccout == sender_numberAccout:
                sender_account = conta
            if conta.numberAccout == recipient_numberAccout:
                recipient_account = conta

        # Verificando se as contas foram encontradas
        if sender_account is None:
            print("Conta do remetente não encontrada!")
            return
        if recipient_account is None:
            print("Conta do destinatário não encontrada!")
            return

        # Realizando a transferência
        
        recipient_account.Deposito(valor,sender_account)
        print(f"Transferência de R${valor} realizada com sucesso!")

        


banco1 = Banco()
banco1.open_accout("adegas",100,1)
banco1.open_accout("jubscreuda",100,2)
banco1.client_register("adegas")
banco1.client_register("jubscreuda")
banco1.transfe(12,1,2)




        
        
    


