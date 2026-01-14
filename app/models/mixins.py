from datetime import datetime
from typing import List, Dict
from app.models.enums import StatusVeiculo

class ManutenivelMixin:
    """Gerencia status e histórico de manutenções."""
    def __init__(self):
        if not hasattr(self, '_historico_manutencoes'):
            self._historico_manutencoes: List[Dict] = []
        if not hasattr(self, '_status'):
            self._status = StatusVeiculo.ATIVO

    def registrar_manutencao(self, tipo: str, custo: float, descricao: str) -> None:
        registro = {
            "data": datetime.now().isoformat(),
            "tipo": tipo,
            "custo": custo,
            "descricao": descricao
        }
        self._historico_manutencoes.append(registro)
        self._status = StatusVeiculo.MANUTENCAO

    def finalizar_manutencao(self) -> None:
        if self._status == StatusVeiculo.MANUTENCAO:
            self._status = StatusVeiculo.ATIVO

    @property
    def em_manutencao(self) -> bool:
        return self._status == StatusVeiculo.MANUTENCAO


class AbastecivelMixin:
    """Gerencia abastecimento e cálculo de consumo."""
    def __init__(self):
        if not hasattr(self, '_historico_abastecimento'):
            self._historico_abastecimento: List[Dict] = []
        if not hasattr(self, '_consumo_medio'):
            self._consumo_medio = 0.0

    def abastecer(self, litros: float, valor: float, km_atual: float):
        # Tenta pegar a KM atual do veículo
        km_anterior = getattr(self, 'km', 0)
        
        # Lógica de consumo (se andou algo)
        distancia = km_atual - km_anterior
        if distancia > 0 and litros > 0:
            consumo_trecho = distancia / litros
            if self._consumo_medio == 0:
                self._consumo_medio = consumo_trecho
            else:
                # Média ponderada simples
                self._consumo_medio = (self._consumo_medio + consumo_trecho) / 2

        # Atualiza KM no veículo se possível
        if hasattr(self, 'km'):
            try:
                self.km = km_atual
            except ValueError:
                pass # Ignora erro se KM for menor (validação do Veiculo)

        registro = {
            "data": datetime.now().isoformat(),
            "litros": litros,
            "valor": valor,
            "km_momento": km_atual
        }
        self._historico_abastecimento.append(registro)

    @property
    def consumo_medio(self) -> float:
        return round(self._consumo_medio, 2)