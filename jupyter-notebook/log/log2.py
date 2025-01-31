import random
import logging
from time import sleep

# Configuração do logger para salvar em app.log
logging.basicConfig(filename='app2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    while True:
        sleep(1)
        processo_id = random.randint(1, 1000)
        logging.info(f'O processo {processo_id} está sendo executado!')
except KeyboardInterrupt:
    print("\nProcesso interrompido com sucesso.")