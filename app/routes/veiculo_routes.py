from flask import Blueprint, request, jsonify
from app.models.carro import Carro
from app.models.moto import Moto
from app.models.caminhao import Caminhao
from app.repositories.veiculo_repo import JsonVeiculoRepository

veiculo_bp = Blueprint('veiculos', __name__)

# Instanciamos o repositório uma vez (Singleton implícito)
repo = JsonVeiculoRepository()

@veiculo_bp.route('', methods=['GET'])
def listar_veiculos():
    """Retorna todos os veículos cadastrados."""
    todos = repo.listar()
    return jsonify(todos), 200

@veiculo_bp.route('', methods=['POST'])
def criar_veiculo():
    """Cria um novo veículo baseado no JSON enviado."""
    dados = request.get_json()
    
    # Validação simples
    if not dados or 'tipo' not in dados:
        return jsonify({"erro": "O campo 'tipo' (Carro, Moto, Caminhao) é obrigatório."}), 400

    try:
        # Factory: decide qual classe criar baseada no tipo (Polimorfismo)
        tipo = dados['tipo'].lower()
        novo_veiculo = None

        if tipo == 'carro':
            novo_veiculo = Carro(
                placa=dados['placa'],
                marca=dados['marca'],
                modelo=dados['modelo'],
                ano=dados['ano'],
                portas=dados.get('portas', 4)
            )
        elif tipo == 'moto':
            novo_veiculo = Moto(
                placa=dados['placa'],
                marca=dados['marca'],
                modelo=dados['modelo'],
                ano=dados['ano'],
                cilindradas=dados.get('cilindradas', 150)
            )
        elif tipo == 'caminhao':
            novo_veiculo = Caminhao(
                placa=dados['placa'],
                marca=dados['marca'],
                modelo=dados['modelo'],
                ano=dados['ano'],
                capacidade_toneladas=dados.get('capacidade_toneladas', 10.0)
            )
        else:
            return jsonify({"erro": f"Tipo de veículo '{tipo}' inválido."}), 400

        # Salva usando o repositório
        repo.salvar(novo_veiculo)
        
        return jsonify({
            "mensagem": "Veículo criado com sucesso!",
            "veiculo": novo_veiculo.to_dict()
        }), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao criar veículo: {str(e)}"}), 500