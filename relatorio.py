# pip install reportlab
# import reportlab
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
# Definir o documento PDF
pdf = SimpleDocTemplate("relatorio.pdf")
# Definir a lista de elementos
elementos = []
# Definir a lista de estilos
estilos = getSampleStyleSheet()
# Dados de venda
dados = [
    ["produto", "quantidade", "valor_total", "data_venda"],
    ["Notebook", 10, 2500.00, "2026-01-05"],
    ["Mouse", 25, 50.00, "2026-02-02"],
    ["Teclado", 15, 75.00, "2026-03-01"],
    ["Monitor", 8, 1200.00, "2026-01-15"],
    ["Headset", 20, 150.00, "2026-01-22"],
    ["Webcam", 12, 300.00, "2026-01-28"],
    ["Cadeira Gamer", 5, 950.00, "2026-02-05"],
    ["Mousepad", 40, 35.00, "2026-02-12"],
    ["SSD 1TB", 18, 420.00, "2026-02-19"],
    ["Memória RAM 16GB", 14, 280.00, "2026-02-25"],
    ["Placa de Vídeo", 4, 3200.00, "2026-03-04"],
    ["Fonte 650W", 9, 450.00, "2026-03-14"],
    ["Gabinete", 7, 380.00, "2026-03-23"],
]

df = pd.DataFrame(dados[1:], columns=dados[0])

# Titulo
titulo = Paragraph(
    "Relatório de Vendas 1° Tri 2026",
    estilos['Title']
)
elementos.append(titulo)
# Subtítulo
subtitulo = Paragraph(
    "Resumo Gerencial",
    estilos['Heading2']
)
elementos.append(subtitulo)
# Indicadores
total_vendas = df["valor_total"].sum()
quantidade = len(df)
ticket_medio = total_vendas / quantidade
resumo = f"""
As vendas do Q1 podem ser resumidas em: <br/>
Total vendido: R$ {total_vendas} <br/>
Quantidade de vendas: {quantidade} vendas <br/>
Ticket médio: R$ {ticket_medio}
"""
elementos.append(Paragraph(resumo, estilos["Normal"]))
elementos.append(Spacer(1, 20))
# criar tabela
tabela = Table(dados)
from reportlab.lib import colors
tabela.setStyle(TableStyle([
    ("BACKGROUND",(0,0), (-1,0), colors.darkblue),
    ("TEXTCOLOR",(0,0), (-1,0), colors.white),
    ("GRID",(0,0),(-1,-1),0.5,colors.gray)
]))
elementos.append(tabela)

df["data_venda"] = pd.to_datetime(df["data_venda"])

# Gerando as três variáveis com o total de vendas de cada mês
total_janeiro = df[df["data_venda"].dt.month == 1]["valor_total"].sum()
total_fevereiro = df[df["data_venda"].dt.month == 2]["valor_total"].sum()
total_marco = df[df["data_venda"].dt.month == 3]["valor_total"].sum()

elementos.append(Spacer(1, 20))
resumo_mensal = f"""
Resumo Mensal: <br/>
Janeiro: R$ {total_janeiro} <br/>
Fevereiro: R$ {total_fevereiro} <br/>
Março: R$ {total_marco} <br/>
"""
elementos.append(Paragraph(resumo_mensal, estilos["Normal"]))

# construir/gerar o relatório
pdf.build(elementos)