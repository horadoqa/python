import logging
import subprocess
from time import sleep
import os

# Caminho absoluto para o arquivo de log
log_path = "/home/rfahham/projetos/python/jupyter-notebook/log/app.log"  # Substitua pelo caminho correto do seu sistema

# Função para criar o arquivo de log se não existir
def verificar_criar_log():
    if not os.path.exists(log_path):
        with open(log_path, 'w') as f:
            pass  # Cria o arquivo em branco, se não existir
        print(f"Arquivo {log_path} criado com sucesso!")  # Mensagem de depuração
    else:
        print(f"Arquivo {log_path} já existe.")  # Mensagem de depuração

# Configuração do logger para salvar em app.log (modo de append para adicionar logs sem sobrescrever)
verificar_criar_log()

# Configuração do logger com mais detalhes
logging.basicConfig(
    filename=log_path, 
    level=logging.DEBUG,  # Mudança para DEBUG para capturar mais informações
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Verificação de se o logger está funcionando corretamente (mensagem inicial)
logging.debug("Logger configurado com sucesso.")

# Função para realizar o ping e verificar a conectividade
def verificar_ping(endereco):
    try:
        # Usamos o subprocess para executar o comando de ping
        resultado = subprocess.run(
            ["ping", "-c", "1", endereco], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        if resultado.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        logging.error(f"Erro ao tentar fazer ping: {e}")
        return False

try:
    logging.debug("Iniciando o processo de verificação de ping.")
    
    while True:
        sleep(1)
        
        # Verifica se o ChatGPT (OpenAI) está acessível
        endereco_chatgpt = "chat.openai.com"
        sucesso_ping = verificar_ping(endereco_chatgpt)
        
        # Registra o resultado do ping no arquivo de log
        if sucesso_ping:
            logging.info(f"Ping para {endereco_chatgpt} foi bem-sucedido!")
        else:
            logging.warning(f"Falha no ping para {endereco_chatgpt}.")

        # Força o logger a escrever imediatamente no arquivo
        for handler in logging.root.handlers:
            handler.flush()

except KeyboardInterrupt:
    logging.info("Processo interrompido com sucesso.")
    print("\nProcesso interrompido com sucesso.")
