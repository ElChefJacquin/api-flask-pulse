from flask import Flask, request
import time
import threading

app = Flask(__name__)

# Variável para registrar a última vez que recebemos um post
ultimo_post = time.time()

# Função para verificar se parou de receber posts
def verificar_timeout():
    global ultimo_post
    while True:
        # Se passou mais de 10 segundos desde o último post
        if time.time() - ultimo_post > 10:
            print("Parou de receber posts!")
        time.sleep(1)  # Verifica a cada 1 segundo

# Endpoint para receber os posts do cliente
@app.route('/post_endpoint', methods=['POST'])
def receber_post():
    global ultimo_post
    # Atualiza o timestamp do último post recebido
    ultimo_post = time.time()
    # Exibe a mensagem recebida no console
    print("Recebi um post:", request.form['message'])
    return "OK", 200

if __name__ == '__main__':
    # Inicia a thread para verificar o timeout
    threading.Thread(target=verificar_timeout).start()
    # Inicia o servidor Flask
    app.run()
