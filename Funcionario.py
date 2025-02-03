# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o 
# salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
# considerando descontos de impostos e benefícios. 

class Funcionario:

    # construtor da classe Funcionario
    def __init__(self,nome,salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    #DescontarImpostos
    def DescontarImpostos(self):
        impostos = float(input("Digite o valor dos impostos:\n"))
        self.salario = self.salario - impostos
        print(f"Foram descontados {impostos} de impostos do seu salario, seu novo saldo esta {self.salario}")

    #DescontarBeneficios
    def DescontarBeneficios(self):
        beneficios = float(input("Digite o valor dos beneficios:\n"))
        self.salario = self.salario - beneficios
        print(f"Foram descontados {beneficios} de beneficios do seu salario, seu novo saldo esta {self.salario}")


cleber = Funcionario("cleber",1200,"estagiario")

cleber.DescontarImpostos()
cleber.DescontarBeneficios()