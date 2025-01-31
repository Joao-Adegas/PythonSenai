# Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o 
# modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
# velocidade atual.

class Carro():
    def __init__(self,marca,modelo,velocidade_atual=0): #velocidade atual esta com valor padrão incial
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    #acelerar
    def acelerar(self,acelerou):
        self.velocidade_atual += acelerou
        return self.velocidade_atual

    #frear
    def frear(self,freio):
        self.velocidade_atual -= freio
        return self.velocidade_atual
    

    #exibir_velocidade
    def exibir_velicidade(self):
        print(f"A velocidade atual e {self.velocidade_atual }")


carro1 = Carro("wolksvagen","algunModelo")

carro1.acelerar(100)
carro1.frear(10)
carro1.exibir_velicidade()
