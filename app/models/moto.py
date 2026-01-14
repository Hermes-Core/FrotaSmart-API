from typing import Dict, Any
from app.models.veiculo import Veiculo
from app.models.mixins import ManutenivelMixin, AbastecivelMixin

class Moto(Veiculo, ManutenivelMixin, AbastecivelMixin):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int, cilindradas: int):
        Veiculo.__init__(self, placa, marca, modelo, ano)
        ManutenivelMixin.__init__(self)
        AbastecivelMixin.__init__(self)
        self._cilindradas = cilindradas

    def exibir_detalhes(self) -> str:
        return f"Moto {self._modelo} ({self._cilindradas}cc) - {self.status}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tipo": "moto",
            "placa": self.placa,
            "marca": self._marca,
            "modelo": self._modelo,
            "ano": self._ano,
            "km": self.km,
            "status": self.status,
            "cilindradas": self._cilindradas,
            "consumo_medio": self.consumo_medio
        }