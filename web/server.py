from flask import Flask
from src.routes import router
from flask_gravatar import Gravatar

# Cria uma instância do Flask
app = Flask(__name__)

# Registra as rotas do arquivo routes.py
app.secret_key = "secret_key"
app.register_blueprint(router)

gravatar = Gravatar(
    app,
    size=100,
    rating="g",
    default="retro",
    force_default=False,
    use_ssl=False,
    base_url=None,
)


# Verifica se o arquivo está sendo executado diretamente antes de executar o servidor
if __name__ == "__main__":
    app.run(debug=True)
