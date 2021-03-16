# Este script executa um servidor muito simplificado que aceita requests cross-origin de qualquer outro servidor.
# Não faça isso num projeto real
# E os três batepapos estão na memória, da forma mais simplificada só para facilitar a implementação
# já que o foco ainda é o front-end.

# Se você for executar, precisará executar os comandos abaixo, como usuário comum, considerando que está no ambiente Windows:
# mkdir back 
# ls -la -> mostra os arquivos ocultos na pasta ./back
# Rodei dois comandos do tutorial via cmd - How to use a Python 3 virtual environment in Windows 10 - Techcoil Blog
# python -m venv %systemdrive%%homepath%\my-venv
# %systemdrive%%homepath%\my-venv\Scripts\activate.bat - serve para ativar o ambiente virtual do Python 3 no windows: 
# pip install flask flask-cors
# (crie o arquivo com o conteúdo deste script e, digamos, o nome flask_app.py)
# python flask_app.py
# Na pasta back, você terá só ele mesmo. Os próximos arquivos são num projeto Vue que, conforme vimos
# na aula anterior, você pode criar com o Vue CLI.

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})

bccdw = []
animes = []
viagens = []

@app.route("/chat", methods=['POST'])
def chat():
    if request.method == 'POST':
        data = request.get_json()
        if data['chat'] == 'bccdw':
            bccdw.append(data)
            return jsonify(bccdw), 200
        elif data['chat'] == 'animes':
            animes.append(data)
            return jsonify(animes), 200
        elif data['chat'] == 'viagens':
            viagens.append(data)  
            return jsonify(viagens), 200
    abort(404)


if __name__ == '__main__':
    app.debug = True
    app.run()