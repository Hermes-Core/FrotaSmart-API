# importando a classe Carro
from app.models.carro import Carro
import json

# verificando se é o arquivo principal
if __name__ == "__main__":
    # imprimindo linha em branco
    print("\n")
    
    # testando criar um carro
    print("Criando um carro...")
    try:
        # criando o objeto carro
        meu_carro = Carro(placa="ABC2A25", marca="Toyota", modelo="Corolla", ano=2024)
        # se deu certo, imprime
        print("Sucesso: " + str(meu_carro))
    except Exception as e:
        # se deu erro, imprime o erro
        print("Erro ao criar veículo: " + str(e))

    # testando a parte de manutencao
    print("\n--- Teste de Manutenção ---")
    # registrando uma manutencao no carro
    meu_carro.registrar_manutencao("Preventiva", 500.00, "Revisão de 10k")
    
    # mostrando o estado final
    print("\n--- Estado Final (Dicionário) ---")
    # convertendo o carro para dicionario
    dicionario_carro = meu_carro.to_dict()
    # convertendo para json bonito
    json_bonito = json.dumps(dicionario_carro, indent=4, ensure_ascii=False)
    # imprimindo
    print(json_bonito)