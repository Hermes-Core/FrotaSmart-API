# importando as bibliotecas necessarias
from datetime import datetime
from app.models.enums import StatusVeiculo

# classe mixin para manutencao
class ManutenivelMixin:
    # esse mixin serve para gerenciar manutencao dos veiculos
    
    def __init__(self):
        # criando a lista de manutencoes vazia
        self.historico_manutencoes = []
        # status inicial do veiculo é ativo
        self.status = StatusVeiculo.ATIVO
    
    # funcao para registrar manutencao
    def registrar_manutencao(self, tipo, custo, descricao):
        # pegando a data de hoje
        data_atual = datetime.now()
        # convertendo para string
        data_string = data_atual.isoformat()
        
        # criando o dicionario com os dados da manutencao
        registro = {}
        registro["data"] = data_string
        registro["tipo"] = tipo
        registro["custo"] = custo
        registro["descricao"] = descricao
        
        # adicionando na lista
        self.historico_manutencoes.append(registro)
        
        # mudando o status para manutencao
        self.status = StatusVeiculo.MANUTENCAO
        
        # imprimindo mensagem
        print("Manutenção registrada: " + descricao + ". Status alterado para " + self.status.value + ".")
    
    # funcao para finalizar manutencao
    def finalizar_manutencao(self):
        # verificando se o veiculo esta em manutencao
        if self.status != StatusVeiculo.MANUTENCAO:
            # se nao estiver, mostra mensagem
            print("O veículo não está em manutenção.")
            return
        else:
            # se estiver, muda o status para ativo
            self.status = StatusVeiculo.ATIVO
            # mostra mensagem de sucesso
            print("Manutenção finalizada. Veículo liberado (Status: " + self.status.value + ").")
    
    # funcao para verificar se esta em manutencao
    def em_manutencao(self):
        # retorna True se estiver em manutencao
        if self.status == StatusVeiculo.MANUTENCAO:
            return True
        else:
            return False