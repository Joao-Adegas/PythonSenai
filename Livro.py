# Implemente uma classe chamada “Livro” com atributos para armazenar o título, o 
# autor e o número de páginas do livro. Adicione métodos para emprestar o livro, 
# devolvê-lo e verificar se está disponível.

class Livro:

    def __init__(self,titulo,autor,numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.disponibilidade = True #declarando o livro como DISPONIVEL


    #emprestar_livro
    def emprestar_livro(self):
        if self.disponibilidade == True:
            self.disponibilidade = False
            print("Livro emprestado")
        

    #devolver_livro
    def devolver_livro(self):
        if(self.disponibilidade == False):
            self.disponibilidade == True
            print("livro devolvido ")
        else:
            print(" o livro nem saiu daqui ")

    #verificar_disponibilidade
    def verificar_disponibilidade(self):
        if(self.disponibilidade == False):
            print("o livro nao esta disponivel")
        elif(self.disponibilidade == True):
            print("O livro esta disponivel")

livro1 = Livro("Extraordinario","eu",200)

livro1.emprestar_livro()
livro1.verificar_disponibilidade()
livro1.devolver_livro()
