# Implemente uma classe chamada “ContaBancária” que possua atributos para 
# armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
# depósitos e saques.

class ContaBancaria:
    
    # onde os atributos da classe ficam
    def __init__(self,NomeDoTitular,saldo,NumeroDaConta):
        self.NomeDoTitular = NomeDoTitular
        self.saldo = saldo
        self.NumeroDaconta = NumeroDaConta

    #Deposito
    def Deposito(self,valor,ContaDestinatariaNumero):
        self.saldo -= valor
        print(f"O valor {valor} foi depositado na conta de {self.NomeDoTitular} para {ContaDestinatariaNumero}")
        
    #Saque
    def Saque(self,valor):
        self.saldo += valor
        print(f"O valor {valor} foi sacado. seu saldo agora e {self.saldo}")








