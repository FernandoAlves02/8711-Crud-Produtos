from app.core.data_utils import Data_Utils

class Usuario:
    def __init__(self, id, nome, email, data_nascimento):
        self._id = id
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        self._data_nascimento = nova_data

    def atualizar_dados(self, novo_nome, novo_email, nova_data_nascimento):
        self._nome = novo_nome
        self._email = novo_email
        self._data_nascimento = nova_data_nascimento #Deixar aqui, vai que o cara colocou a data errada
        