# Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a 
# idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
# uma nova consulta ao histórico e exibir as consultas realizadas. 

class Paciente():

    #construtor da classe Paciente
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.historico = 0
        self.consultas = 0
    
    #Adicionar consulta
    def adicionar_consultas(self,quantidade):
        self.consultas += quantidade
        return self.consultas

    #exibir_consultas
    def exibir_consultas(self):
        print(f" o paciente {self.nome} possui {self.consultas} consultas")

paciente1 = Paciente("gabi",19)

paciente1.adicionar_consultas(10)
paciente1.exibir_consultas()


        
        