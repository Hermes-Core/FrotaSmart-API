import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from app.models.veiculo import Veiculo

class VeiculoRepository(ABC):
    @abstractmethod
    def salvar(self, veiculo: Veiculo): pass
    @abstractmethod
    def listar(self) -> List[Dict]: pass
    @abstractmethod
    def buscar_por_placa(self, placa: str) -> Optional[Dict]: pass

class JsonVeiculoRepository(VeiculoRepository):
    def __init__(self, arquivo_db='data/frota.json'):
        self.arquivo_db = arquivo_db
        os.makedirs(os.path.dirname(self.arquivo_db), exist_ok=True)
        # Cria arquivo vazio se não existir
        if not os.path.exists(self.arquivo_db):
            with open(self.arquivo_db, 'w') as f:
                json.dump([], f)

    def _ler_arquivo(self) -> List[Dict]:
        try:
            with open(self.arquivo_db, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _salvar_arquivo(self, dados: List[Dict]):
        with open(self.arquivo_db, 'w') as f:
            json.dump(dados, f, indent=4)

    def salvar(self, veiculo: Veiculo):
        dados = self._ler_arquivo()
        # Remove se já existir (atualização simples)
        dados = [v for v in dados if v['placa'] != veiculo.placa]
        # Adiciona o novo (serializado pelo método to_dict das classes)
        dados.append(veiculo.to_dict())
        self._salvar_arquivo(dados)

    def listar(self) -> List[Dict]:
        return self._ler_arquivo()

    def buscar_por_placa(self, placa: str) -> Optional[Dict]:
        dados = self._ler_arquivo()
        for v in dados:
            if v['placa'] == placa:
                return v
        return None