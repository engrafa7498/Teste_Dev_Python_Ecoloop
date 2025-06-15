# Resposta Questão 1

from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota GET /saudacao
@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'visitante')
    return jsonify({"mensagem": f"Olá, {nome}!"})

# Rota POST /soma
@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    numero1 = dados.get('numero1', 0)
    numero2 = dados.get('numero2', 0)
    resultado = numero1 + numero2
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
