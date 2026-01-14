from abc import ABC, abstractmethod
from app.models.enums import StatusVeiculo

class Veiculo(ABC):
    def __init__(self, placa: str, marca: str, modelo: str, ano: int):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._km: float = 0.0
        self._status = StatusVeiculo.ATIVO

    @property
    def placa(self) -> str:
        return self._placa

    @property
    def km(self) -> float:
        return self._km

    @km.setter
    def km(self, nova_km: float):
        if nova_km < self._km:
            raise ValueError("A quilometragem não pode ser reduzida.")
        self._km = nova_km

    @property
    def status(self) -> str:
        return self._status.value

    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass

    # Métodos Mágicos
    def __str__(self) -> str:
        return f"[{self._placa}] {self._marca} {self._modelo}"

    def __eq__(self, outro):
        if isinstance(outro, Veiculo):
            return self._placa == outro.placa
        return False

    def __lt__(self, outro):
        return self._km < outro.km
