from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    # Recebe o parâmetro nome da query string e retorna uma saudação personalizada
    nome = request.args.get('nome', 'visitante')
    return jsonify({"mensagem": f"Olá, {nome}!"})

@app.route('/soma', methods=['POST'])
def soma():
    # Recebe JSON com numero1 e numero2, soma e retorna resultado
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400
    try:
        numero1 = float(dados.get('numero1'))
        numero2 = float(dados.get('numero2'))
    except (TypeError, ValueError):
        return jsonify({"erro": "Os valores 'numero1' e 'numero2' devem ser números."}), 400

    resultado = numero1 + numero2
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
