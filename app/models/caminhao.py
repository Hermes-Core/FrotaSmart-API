from typing import Dict, Any
from app.models.veiculo import Veiculo
from app.models.mixins import ManutenivelMixin, AbastecivelMixin

class Caminhao(Veiculo, ManutenivelMixin, AbastecivelMixin):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int, capacidade_toneladas: float):
        Veiculo.__init__(self, placa, marca, modelo, ano)
        ManutenivelMixin.__init__(self)
        AbastecivelMixin.__init__(self)
        self._capacidade = capacidade_toneladas

    def exibir_detalhes(self) -> str:
        return f"🚛 Caminhão {self._modelo} ({self._capacidade}t) - {self.status}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tipo": "caminhao",
            "placa": self.placa,
            "marca": self._marca,
            "modelo": self._modelo,
            "ano": self._ano,
            "km": self.km,
            "status": self.status,
            "capacidade_toneladas": self._capacidade,
            "consumo_medio": self.consumo_medio
        }