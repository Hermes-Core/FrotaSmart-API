# FrotaSmart-API
API RESTful para gerenciamento inteligente de frotas, motoristas e manutenções preventivas.

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem de programação
- **Flask**: Framework web para criação da API REST
- **pytest**: Framework de testes
- **JSON**: Formato de persistência de dados

---

## 📦 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes do Python)

### Passo 1: Clone o repositório

```bash
git clone <url-do-repositorio>
cd FrotaSmart-API
```

### Passo 2: Crie um ambiente virtual (recomendado)

```bash
# No macOS/Linux
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

### Passo 3: Instale as dependências

```bash
pip install -r requirements.txt
```

As dependências incluem:
- `flask`: Framework web
- `pytest`: Framework de testes

---

## 🚀 Como Executar o Projeto

### Método 1: Usando o script run.py (Recomendado)

```bash
python run.py
```

### Testando se o servidor está funcionando

Abra seu navegador ou use curl:

```bash
curl http://localhost:5000/api/veiculos
```

---

## 🧪 Como Executar os Testes

### Executar todos os testes

```bash
pytest
```

---

## 📁 Estrutura do Projeto

```
FrotaSmart-API/
│
├── app/                          # Pacote principal da aplicação
│   ├── __init__.py              # Factory da aplicação Flask
│   ├── config.py                # Configurações (Singleton)
│   │
│   ├── models/                  # Camada de Domínio (Classes de Negócio)
│   │   ├── veiculo.py          # Classe abstrata Veiculo
│   │   ├── carro.py            # Classe concreta Carro
│   │   ├── moto.py             # Classe concreta Moto
│   │   ├── caminhao.py         # Classe concreta Caminhao
│   │   ├── enums.py            # Enumeradores (StatusVeiculo, etc.)
│   │   └── mixins.py           # ManutencivelMixin, AbastecivelMixin
│   │
│   ├── repositories/            # Camada de Persistência (Repository Pattern)
│   │   └── veiculo_repo.py     # Interface e implementação JSON
│   │
│   └── routes/                  # Camada de Apresentação (Endpoints)
│       ├── __init__.py
│       └── veiculo_routes.py   # Rotas da API (/api/veiculos)
│
├── data/                        # Diretório de dados persistidos
│   └── frota.json              # Arquivo JSON com os veículos
│
├── tests/                       # Testes Automatizados
│   ├── __init__.py
│   ├── conftest.py             # Configurações e fixtures do pytest
│   ├── test_models.py          # Testes das classes de domínio
│   └── test_api.py             # Testes dos endpoints da API
│
├── run.py                       # Script para iniciar o servidor
├── requirements.txt             # Dependências do projeto
├── settings.json                # Configurações de políticas e custos
├── teste_sistema.py             # Script de demonstração do sistema
└── README.md                    # Este arquivo
```

---

## 🌐 Endpoints da API

### Base URL
```
http://localhost:5000/api/veiculos
```

### 1. Listar todos os veículos

**Método:** `GET /api/veiculos`

**Descrição:** Retorna todos os veículos cadastrados no sistema.

**Exemplo de requisição:**
```bash
curl -X GET http://localhost:5000/api/veiculos
```

**Resposta de sucesso (200 OK):**
```json
[
  {
    "tipo": "carro",
    "placa": "ABC-1234",
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022,
    "km": 15000.5,
    "status": "ATIVO",
    "portas": 4
  },
  {
    "tipo": "moto",
    "placa": "XYZ-5678",
    "marca": "Honda",
    "modelo": "CB 500",
    "ano": 2023,
    "km": 5000.0,
    "status": "ATIVO",
    "cilindradas": 500
  }
]
```

### 2. Criar um novo veículo

**Método:** `POST /api/veiculos`

**Descrição:** Cria um novo veículo no sistema.

#### Criar Carro

**Exemplo de requisição:**
```bash
curl -X POST http://localhost:5000/api/veiculos \
  -H "Content-Type: application/json" \
  -d '{
    "tipo": "carro",
    "placa": "ABC-1234",
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022,
    "portas": 4
  }'
```

**Body (JSON):**
```json
{
  "tipo": "carro",
  "placa": "ABC-1234",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2022,
  "portas": 4
}
```

#### Criar Moto

**Exemplo de requisição:**
```bash
curl -X POST http://localhost:5000/api/veiculos \
  -H "Content-Type: application/json" \
  -d '{
    "tipo": "moto",
    "placa": "XYZ-5678",
    "marca": "Honda",
    "modelo": "CB 500",
    "ano": 2023,
    "cilindradas": 500
  }'
```

**Body (JSON):**
```json
{
  "tipo": "moto",
  "placa": "XYZ-5678",
  "marca": "Honda",
  "modelo": "CB 500",
  "ano": 2023,
  "cilindradas": 500
}
```

#### Criar Caminhão

**Exemplo de requisição:**
```bash
curl -X POST http://localhost:5000/api/veiculos \
  -H "Content-Type: application/json" \
  -d '{
    "tipo": "caminhao",
    "placa": "CAM-9999",
    "marca": "Volvo",
    "modelo": "FH 460",
    "ano": 2021,
    "capacidade_toneladas": 25.0
  }'
```

**Body (JSON):**
```json
{
  "tipo": "caminhao",
  "placa": "CAM-9999",
  "marca": "Volvo",
  "modelo": "FH 460",
  "ano": 2021,
  "capacidade_toneladas": 25.0
}
```

**Resposta de sucesso (201 Created):**
```json
{
  "mensagem": "Veículo criado com sucesso!",
  "veiculo": {
    "tipo": "carro",
    "placa": "ABC-1234",
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022,
    "portas": 4,
    "km": 0.0,
    "status": "ATIVO"
  }
}
```

## Diagrama
<img src="diagrama.png" alt="Diagrama">

## Lista das principais classes do sistema

### Domínio (Core Domain)
`Veiculo`: (Classe Abstrata): Classe base que define os atributos encapsulados (`_placa`, `_modelo`, `_ano`, `_km`) e métodos abstratos. Implementa `@property` para validações de integridade.

`Carro`, `Moto`, `Caminhao` (Classes Concretas): Herdam de `Veiculo` e implementam especificidades de cada tipo.

`Motorista`: Classe responsável pelos dados do condutor e validação de CNH.

### Mixins (Herança Múltipla - Obrigatório)
`ManutenivelMixin`: Adiciona comportamentos de manutenção (registrar manutenção, alterar status para "EM MANUTENÇÃO").

`AbastecivelMixin`: Adiciona comportamentos de abastecimento (registrar abastecimento, calcular consumo médio).

### Persistência (Padrão Repository)
`VeiculoRepository` (Interface/Abstrata): Contrato que define operações de CRUD (`save`, `get_by_placa`, `list_all`, `update`).

`JsonVeiculoRepository`: Implementação concreta que persiste os dados em arquivos `.json`.

### Persistência (Padrão Repository)
`Settings` (Singleton): Responsável por carregar e validar o arquivo `settings.json` (políticas de manutenção e custos).

`FrotaService`: Camada de serviço que orquestra as regras de negócio (ex: verificar se Motorista tem CNH compatível com Veículo antes de alocar).

### Exceções Customizadas
`VeiculoError`, `ManutencaoInvalidaError`, `AlocacaoError`.

## Descrição de responsabilidades de cada membro

### Membro 1: Felipe Alves Bezerra Neto
`Responsabilidade`: Modelagem do Domínio Base.

`Tarefas`: Implementação da classe abstrata Veiculo e das subclasses Carro, Moto e Caminhao.

### Membro 2: Antonio Lucas da Costa Pereira
`Responsabilidade`: Mixins e Tratamento de Erros.

`Tarefas`: Implementação de ManutenivelMixin e AbastecivelMixin (para cumprir o requisito de herança múltipla) e criação das Exceções Customizadas.

### Membro 3: Rubens Paulo Rodrigues Parente
`Responsabilidade`: Gestão de Pessoas e Validações de Negócio.

`Tarefas`: Implementação da classe Motorista e lógica de validação de CNH (ex: Motorista categoria B não pode dirigir Caminhão).

### Membro 4: Everton Lucas Fernandes
`Responsabilidade`: Persistência de Dados (Repository Pattern).

`Tarefas`: Criar a interface VeiculoRepository e a implementação JsonVeiculoRepository (CRUD). Garantir que o domínio não dependa diretamente do arquivo JSON.

### Membro 5: Antonio Airlon da Silva Filho 
`Responsabilidade`: Interface (API Flask) e Configurações.

`Tarefas`: Configuração do Flask, criação dos Endpoints (Rotas) e implementação da classe Settings para leitura do settings.json.

