class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cpnj, sla_atendimento):
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cpnj
        self._sla_atendimento = self.validar_sla(sla_atendimento)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def razao_social(self):
        return self._razao_social

    @razao_social.setter
    def razao_social(self, nova_razao):
        self._razao_social = nova_razao

    @property
    def nome_fantasia(self):
        return self._nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, novo_nomefant):
        self._nome_fantasia = novo_nomefant

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj

    @property
    def sla_atendimento(self):
        return self._sla_atendimento

    @sla_atendimento.setter
    def sla_atendimento(self, novo_sla):
        self._sla_atendimento = novo_sla 

    def validar_sla(self, sla):
        if sla < 0:
            raise ValueError("O SLA de atendimento não pode ser negativo.")
            
    def atualizar_dados(self, novo_razao, novo_nome, novo_cnpj, novo_sla):
        self.validar_sla(novo_sla)
        self._razao_social = novo_razao
        self._nome_fantasia = novo_nome
        self._cnpj = novo_cnpj
        self._sla_atendimento = novo_sla

            