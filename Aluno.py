# Implemente uma classe chamada “Aluno” que possua atributos para armazenar o 
# nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
# notas e verificar a situação do aluno (aprovado ou reprovado).

class Aluno():

    #Construtor da classe Aluno
    def __init__(self,Nome,Matricula):
        self.Nome = Nome
        self.matricula = Matricula
        self.Notas = []

    #CalcularMedia
    def CalcularMedia(self):
        for i in range(0,5):
            notas = float(input(f"Digite a {i+1} nota "))
            self.Notas.append(notas)

        total = sum(self.Notas)
        self.media = total/len(self.Notas)
        print(self.media)

    #Situação
    def Situacao(self):
        if(self.media >=6):
            print("Aprovado")
        else:
            print("Reprovado")


aluno1 = Aluno("joao",208814)

aluno1.CalcularMedia()
aluno1.Situacao()