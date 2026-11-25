import schedule
from relatorio import gerar_relatorio
import time

def tarefa():
    print("Executando agendamento")
    gerar_relatorio()
    
#schedule.every().day.at("08:00").do(tarefa)
schedule.every(5).seconds.do(tarefa)

while True :
    schedule.run_pending()
    time.sleep(1)