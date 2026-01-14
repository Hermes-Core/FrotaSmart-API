import pytest
from app import create_app

@pytest.fixture
def client():
    """Cria um cliente de teste do Flask."""
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

@pytest.fixture
def carro_teste():
    """Cria um objeto Carro pronto para os testes."""
    from app.models.carro import Carro
    return Carro(placa="TEST-0001", marca="Fiat", modelo="Mobi", ano=2023, portas=4)