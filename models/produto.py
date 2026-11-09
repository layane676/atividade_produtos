from database import conectar_banco


class Produto:
    def __init__(self, nome, preco, quantidade, descricao=None, categoria=None):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def salvar(self):
        conexao = conectar_banco()
        try:
            cursor = conexao.execute(
                """
                INSERT INTO produtos (nome, descricao, preco, quantidade, categoria)
                VALUES (?, ?, ?, ?, ?)
                """,
                (self.nome, self.descricao, self.preco, self.quantidade, self.categoria),
            )
            conexao.commit()
            return cursor.lastrowid
        finally:
            conexao.close()

    @staticmethod
    def listar():
        conexao = conectar_banco()
        try:
            return conexao.execute("SELECT * FROM produtos ORDER BY id").fetchall()
        finally:
            conexao.close()

    @staticmethod
    def excluir(produto_id):
        conexao = conectar_banco()
        try:
            cursor = conexao.execute(
                "DELETE FROM produtos WHERE id = ?",
                (produto_id,),
            )
            conexao.commit()
            return cursor.rowcount > 0
        finally:
            conexao.close()
