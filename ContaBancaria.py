# Implemente uma classe chamada “ContaBancária” que possua atributos para 
# armazenar o número da conta, nome do titular e balance. Adicione métodos para realizar 
# depósitos e saques.

class ContaBancaria:
    
    # onde os atributos da classe ficam
    def __init__(self,nameOfHolder,numberAccout,balance):
        self.nameOfHolder = nameOfHolder
        self.balance = balance
        self.numberAccout = numberAccout

    #Deposito
    def Deposito(self,valor,ContaDestinatariaNumero):
        self.balance -= valor
        print(f"O valor {valor} foi depositado na conta de {self.nameOfHolder} para {ContaDestinatariaNumero}")
        
    #Saque
    def Saque(self,valor):
        self.balance += valor
        print(f"O valor {valor} foi sacado da conta de {self.nameOfHolder} e depositado.")

    #metodo para mostrar dados da conta Bancaria
    def __str__(self):
        return f"Nome do titular: {self.nameOfHolder}\n" \
            f"balance: {self.balance}\n" \
            f"Numero da conta: {self.numberAccout}"







