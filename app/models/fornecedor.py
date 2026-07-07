class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cpnj, sla_atendimento):
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cpnj
        self._sla_atendimento = self.validar_sla(sla_atendimento)

    def validar_sla(self, sla):
        if sla < 0:
            raise ValueError("O SLA de atendimento não pode ser negativo.")
            
    def atualizar_dados(self, novo_razao, novo_nome, novo_cnpj, novo_sla):
        self.validar_sla(novo_sla)
        self._razao_social = novo_razao
        self._nome_fantasia = novo_nome
        self._cnpj = novo_cnpj
        self._sla_atendimento = novo_sla

            