import json

def test_listar_veiculos_status_200(client):
    """Verifica se a API responde 200 na listagem."""
    response = client.get('/api/veiculos')
    assert response.status_code == 200

def test_criar_veiculo_api(client):
    """Verifica se cria um veículo via JSON."""
    payload = {
        "tipo": "carro",
        "placa": "API-TEST",
        "marca": "Ford",
        "modelo": "Ka",
        "ano": 2021,
        "portas": 4
    }
    
    response = client.post('/api/veiculos', 
                           data=json.dumps(payload),
                           content_type='application/json')
    
    assert response.status_code == 201
    assert response.json['mensagem'] == "Veículo criado!"

def test_validar_tipo_obrigatorio(client):
    """Verifica se a API recusa JSON sem o campo 'tipo'."""
    payload = {"placa": "ERR-0000"}
    
    response = client.post('/api/veiculos', 
                           data=json.dumps(payload),
                           content_type='application/json')
    
    assert response.status_code == 400