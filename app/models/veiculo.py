# importando as coisas necessarias
from abc import ABC, abstractmethod
from app.models.enums import StatusVeiculo

# classe abstrata Veiculo
class Veiculo(ABC):
    # construtor
    def __init__(self, placa, marca, modelo, ano):
        # salvando os dados do veiculo
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = 0.0
        self.status = StatusVeiculo.ATIVO
    
    # funcao para pegar a quilometragem
    def get_km(self):
        return self.km
    
    # funcao para atualizar a quilometragem
    def set_km(self, nova_km):
        # verificando se a km nova é menor que a atual
        if nova_km < self.km:
            # se for, da erro
            raise ValueError("A quilometragem não pode ser reduzida! Atual: " + str(self.km) + ", Tentativa: " + str(nova_km))
        else:
            # senao, atualiza
            self.km = nova_km
    
    # funcao para pegar o status em formato texto
    def get_status(self):
        # retorna o valor do status
        return self.status.value
    
    # metodo abstrato que precisa ser implementado nas classes filhas
    @abstractmethod
    def exibir_detalhes(self):
        # este metodo precisa ser implementado
        pass
    
    # metodo para imprimir o veiculo
    def __str__(self):
        # retornando a string formatada
        resultado = "[" + self.placa + "] " + self.marca + " " + self.modelo + " (" + str(self.ano) + ") - " + str(self.km) + "km"
        return resultado