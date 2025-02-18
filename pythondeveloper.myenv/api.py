from flask import Flask, request, jsonify
import json

# Criação da aplicação Flask
app = Flask(__name__)

# Lista de tarefas simulando um banco de dados
tarefas = [
    {'id': 1, 'responsavel': 'Julia', 'tarefa': 'Administração', 'status': 'Concluído'},
    {'id': 2, 'responsavel': 'André', 'tarefa': 'Vigilancia', 'status': 'Concluído'},
    {'id': 3, 'responsavel': 'Joaquim', 'tarefa': 'Criar API', 'status': 'Andamento'}
]

# Rota principal para manipular as tarefas com os métodos GET, PUT, POST e DELETE
@app.route('/tarefas/<int:id>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def cadastro(id):
    # Verificando se o ID está dentro do limite válido
    if id < 0 or id >= len(tarefas):
        return jsonify({'erro': 'ID não encontrado'}), 404

    # Consulta uma tarefa específica
    if request.method == 'GET':
        return consultar_tarefa(id)

    # Altera o status de uma tarefa
    if request.method == 'PUT':
        return alterar_status(id)

    # Adiciona uma nova tarefa
    if request.method == 'POST':
        return listar_tarefas()

    # Deleta uma tarefa
    if request.method == 'DELETE':
        return deletar_tarefa(id)

# Função para listar ou adicionar uma nova tarefa
def listar_tarefas():
    if request.method == 'POST':
        # Carregando os dados recebidos no corpo da requisição
        dados = json.loads(request.data)
        tarefas.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro inserido'})

# Função para alterar o status de uma tarefa
# Apenas o campo "status" pode ser alterado
def alterar_status(id):
    if request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = dados['status']
        return jsonify({'status': 'sucesso', 'mensagem': f'Status alterado para: {tarefas[id]}'}), 200

# Função para consultar uma tarefa específica pelo ID
def consultar_tarefa(id):
    if request.method == 'GET':
        cadastro = tarefas[id]
        print(cadastro)  # Exibe no console para fins de depuração
        return jsonify(cadastro)

# Função para deletar uma tarefa pelo ID
def deletar_tarefa(id):
    if request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'}), 200

# Inicia a aplicação Flask no modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
