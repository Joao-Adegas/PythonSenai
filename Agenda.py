#   Implemente uma classe chamada “Agenda” que represente uma agenda telefônica. 
# Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
# contatos a partir de um nome ou número de telefone. 

class Contact:
    def __init__(self,numberContact,nameContact):
        self.numberContact = numberContact
        self.nameContact = nameContact
        

class Agenda:

    def __init__(self):
        self.contatos = []

    def addContact(self,contato):
        self.contatos.append(contato)
        print(f"{contato.nameContact} - {contato.numberContact} Adicionado com sucesso\n")

    def removeContact(self,contato):
        self.contatos.remove(contato)
        print(f"{contato.nameContact} removido da lista de contatos\n")
     
    def buscarContato(self,numberContact):
        for percorrer in self.contatos:
            if numberContact == percorrer.numberContact:
                print(f"{numberContact} encontrado\n")
            else:
                print("Contato nao encontrado\n")



agenda = Agenda()
contato1 = Contact(19982783882,"joao")
agenda.addContact(contato1)
agenda.buscarContato(19982783882)



