class ContaBancaria:
    
    # onde os atributos da classe ficam
    def __init__(self,NomeDoTitular,saldo,NumeroDaConta):
        self.NomeDoTitular = NomeDoTitular
        self.saldo = saldo
        self.NumeroDaconta = NumeroDaConta

    def Deposito(self,valor,ContaDestinatariaNumero):
        self.saldo -= valor
        print(f"O valor {valor} foi depositado na conta de {self.NomeDoTitular} para {ContaDestinatariaNumero}")
        
    def Saque(self,valor):
        self.saldo += valor
        print(f"O valor {valor} foi sacado. seu saldo agora e {self.saldo}")


        

conta1 = ContaBancaria("joao",1,9121281298)

conta2 = ContaBancaria("gabi",10000,129128728)

conta1.Deposito(120,129128728)

conta2.Saque(2)




