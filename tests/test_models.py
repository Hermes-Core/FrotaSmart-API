import pytest
from app.models.enums import StatusVeiculo
from app.models.moto import Moto

def test_criar_carro_com_sucesso(carro_teste):
    """Verifica se o carro é criado corretamente (Herança)."""
    assert carro_teste.placa == "TEST-0001"
    assert carro_teste.km == 0.0
    assert carro_teste.status == "Ativo"

def test_nao_pode_reduzir_km(carro_teste):
    """Testa o Encapsulamento: KM não pode diminuir."""
    carro_teste.km = 100.0  # Aumentar pode
    
    with pytest.raises(ValueError):
        carro_teste.km = 50.0  # Diminuir deve dar erro

def test_registrar_manutencao_altera_status(carro_teste):
    """Testa Mixin de Manutenção e mudança de estado."""
    assert carro_teste.status == StatusVeiculo.ATIVO.value
    
    carro_teste.registrar_manutencao("Troca de Óleo", 200.0, "Preventiva")
    
    assert carro_teste.status == StatusVeiculo.MANUTENCAO.value

def test_calculo_consumo_medio():
    """Testa Mixin de Abastecimento e matemática."""
    moto = Moto("MOTO-99", "Honda", "CG", 2022, 160)
    
    # Simula andar 100km e abastecer
    moto.km = 100.0
    moto.abastecer(litros=10, valor=50.0, km_atual=100.0) # Primeiro abastecimento
    
    # Simula andar +100km (Total 200) e abastecer 5L
    # Consumo: 100km andados / 5L = 20 km/l
    moto.abastecer(litros=5, valor=25.0, km_atual=200.0)
    
    assert moto.consumo_medio == 20.0