import math

from flask import Blueprint, jsonify, request

from models.produto import Produto

produto_bp = Blueprint("produtos", __name__)


@produto_bp.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie os dados do produto em JSON."}), 400

    nome = dados.get("nome")
    preco = dados.get("preco")
    quantidade = dados.get("quantidade")
    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "O campo 'nome' é obrigatório."}), 400
    if (
        isinstance(preco, bool)
        or not isinstance(preco, (int, float))
        or not math.isfinite(preco)
        or preco < 0
    ):
        return jsonify({"erro": "O campo 'preco' deve ser um número não negativo."}), 400
    if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade < 0:
        return jsonify({"erro": "O campo 'quantidade' deve ser um inteiro não negativo."}), 400

    produto = Produto(
        nome=nome.strip(),
        preco=preco,
        quantidade=quantidade,
        descricao=dados.get("descricao"),
        categoria=dados.get("categoria"),
    )
    produto_id = produto.salvar()
    return jsonify({"id": produto_id, "mensagem": "Produto cadastrado."}), 201


@produto_bp.route("/listar", methods=["GET"])
def listar():
    produtos = [dict(produto) for produto in Produto.listar()]
    return jsonify(produtos)


@produto_bp.route("/apagar", defaults={"produto_id": None}, methods=["DELETE"])
@produto_bp.route("/apagar/<int:produto_id>", methods=["DELETE"])
def apagar(produto_id):
    if produto_id is None:
        dados = request.get_json(silent=True) or {}
        produto_id = request.args.get("id", dados.get("id"))

    try:
        produto_id = int(produto_id)
    except (TypeError, ValueError):
        return jsonify({"erro": "Informe um ID de produto válido."}), 400

    if not Produto.excluir(produto_id):
        return jsonify({"erro": "Produto não encontrado."}), 404
    return jsonify({"mensagem": "Produto excluído."})