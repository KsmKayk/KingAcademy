from flask import Flask
from src.routes import router

# Cria uma instância do Flask
app = Flask(__name__)

# Registra as rotas do arquivo routes.py
app.register_blueprint(router)


# Verifica se o arquivo está sendo executado diretamente antes de executar o servidor
if __name__ == "__main__":
    app.run(debug=True)
