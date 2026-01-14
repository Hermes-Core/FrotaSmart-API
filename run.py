from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🚀 Servidor FrotaSmart rodando em http://localhost:5000")
    # debug=True facilita ver os erros no terminal
    app.run(debug=True)