# importando as classes necessarias
from app.models.veiculo import Veiculo
from app.models.mixins import ManutenivelMixin

# classe do carro
class Carro(Veiculo, ManutenivelMixin):
    # construtor da classe
    def __init__(self, placa, marca, modelo, ano, portas=4):
        # chamando o construtor da classe pai Veiculo
        Veiculo.__init__(self, placa, marca, modelo, ano)
        # chamando o construtor do Mixin
        ManutenivelMixin.__init__(self)
        
        # salvando o numero de portas
        self.portas = portas

    # metodo para exibir os detalhes do carro
    def exibir_detalhes(self):
        # retornando a string com os detalhes
        detalhes = "Carro " + self.modelo + " com " + str(self.portas) + " portas. Status: " + self.get_status()
        return detalhes

    # metodo para converter para dicionario
    def to_dict(self):
        # criando o dicionario
        dicionario = {}
        dicionario["placa"] = self.placa
        dicionario["modelo"] = self.modelo
        dicionario["tipo"] = "Carro"
        dicionario["km"] = self.km
        dicionario["status"] = self.get_status()
        dicionario["manutencoes"] = self.historico_manutencoes
        return dicionario