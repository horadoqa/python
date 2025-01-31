import os
import random
from time import sleep

try:
    while True:
        sleep(1)
        os.system(f"echo 'O processo {random.randint(1, 1000)} está sendo executado!' >> app.log")
except KeyboardInterrupt:
    print("\nProcesso interrompido com sucesso.")