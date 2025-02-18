from flask import Flask, jsonify, request  # Importa o Flask e ferramentas para trabalhar com JSON e requisições HTTP
import json  # Módulo para trabalhar com JSON

app = Flask(__name__)  # Inicializa a aplicação Flask

@app.route('/<int:id>')  # Define uma rota para a URL com um parâmetro 'id' do tipo inteiro
def pessoa(id):
    soma = 1 + id  # Exemplo simples de operação com o id recebido
    return jsonify({'id': id, 'nome': 'Gabriella'})  # Retorna uma resposta JSON com 'id' e 'nome'

@app.route('/soma', methods=['POST', 'GET'])  # Define uma rota para a URL '/soma' com os métodos POST e GET
def soma():
    if request.method == 'POST':  # Se a requisição for POST
        dados = json.loads(request.data)  # Converte os dados recebidos no corpo da requisição para um dicionário Python
        total = sum(dados["valores"])  # Soma os valores presentes na chave "valores" do dicionário
    elif request.method == 'GET':  # Se a requisição for GET
        total = 10 + 10  # Exemplo simples de soma fixa
    return jsonify({'soma': total})  # Retorna o resultado da soma em formato JSON

# Comentário adicional sobre o funcionamento do POST
# O método POST permite que você envie informações no corpo da requisição, 
# enquanto o GET recupera dados sem alterar o estado no servidor.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    app.run(debug=True)  # Inicia o servidor Flask com o modo de depuração ativado (reinicia automaticamente em caso de mudanças)
