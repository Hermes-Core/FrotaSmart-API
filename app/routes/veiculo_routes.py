from flask import Blueprint, request, jsonify
from app.models.carro import Carro
from app.models.moto import Moto
from app.models.caminhao import Caminhao
from app.repositories.veiculo_repo import JsonVeiculoRepository

veiculo_bp = Blueprint('veiculos', __name__)
repo = JsonVeiculoRepository()

@veiculo_bp.route('', methods=['GET'])
def listar_veiculos():
    todos = repo.listar()
    return jsonify(todos), 200

@veiculo_bp.route('/<placa>', methods=['GET'])
def buscar_veiculo(placa):
    veiculo = repo.buscar_por_placa(placa)
    if veiculo:
        return jsonify(veiculo), 200
    return jsonify({"erro": "Veículo não encontrado"}), 404

@veiculo_bp.route('', methods=['POST'])
def criar_veiculo():
    dados = request.get_json()
    if not dados or 'tipo' not in dados:
        return jsonify({"erro": "Campo 'tipo' obrigatório"}), 400

    try:
        tipo = dados['tipo'].lower()
        novo_veiculo = None

        # Factory Pattern (Polimorfismo na criação)
        if tipo == 'carro':
            novo_veiculo = Carro(
                dados['placa'], dados['marca'], dados['modelo'], 
                int(dados['ano']), int(dados.get('portas', 4))
            )
        elif tipo == 'moto':
            novo_veiculo = Moto(
                dados['placa'], dados['marca'], dados['modelo'], 
                int(dados['ano']), int(dados.get('cilindradas', 150))
            )
        elif tipo == 'caminhao':
            novo_veiculo = Caminhao(
                dados['placa'], dados['marca'], dados['modelo'], 
                int(dados['ano']), float(dados.get('capacidade_toneladas', 10.0))
            )
        else:
            return jsonify({"erro": "Tipo inválido"}), 400

        repo.salvar(novo_veiculo)
        return jsonify({"mensagem": "Veículo criado!", "dados": novo_veiculo.to_dict()}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500