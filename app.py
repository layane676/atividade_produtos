from flask import Flask, redirect, render_template, url_for

from database import inicializar_banco
from controllers.produto_controller import produto_bp

app = Flask(__name__)

inicializar_banco()
app.register_blueprint(produto_bp)


@app.route("/", methods=["GET"])
def inicio():
    return render_template("listar.html")


@app.route("/novo", methods=["GET"])
def novo_produto():
    return render_template("cadastrar.html")


if __name__ == "__main__":
    app.run(debug=True)