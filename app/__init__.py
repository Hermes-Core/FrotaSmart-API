from flask import Flask
from app.config import Settings

def create_app():
    app = Flask(__name__)

    # Carrega configurações (Singleton)
    Settings.get_instance().load()

    # Registra as rotas
    from app.routes.veiculo_routes import veiculo_bp
    app.register_blueprint(veiculo_bp, url_prefix='/api/veiculos')

    return app