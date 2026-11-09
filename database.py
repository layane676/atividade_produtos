import sqlite3
from pathlib import Path


CAMINHO_BANCO = Path(__file__).resolve().parent / "produtos.db"


def conectar_banco(caminho=CAMINHO_BANCO):
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco(caminho=CAMINHO_BANCO):
    conexao = conectar_banco(caminho)
    try:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                descricao TEXT,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL,
                categoria VARCHAR(50)
            )
            """
        )
        conexao.commit()
    finally:
        conexao.close()