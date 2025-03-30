from flask import Flask, jsonify, request
from jsonschema import validate, ValidationError
import json
import os

app = Flask(__name__)

DATA_FILE = 'tarefas.json'
SCHEMA_FILE = 'schema.json'

# Carregar schema
with open(SCHEMA_FILE, 'r') as f:
    schema = json.load(f)

# Funções utilitárias
def carregar_tarefas():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def guardar_tarefas(tarefas):
    with open(DATA_FILE, 'w') as f:
        json.dump(tarefas, f, indent=2)

# Endpoints

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(carregar_tarefas())

@app.route('/tarefas/<int:tarefa_id>', methods=['GET'])
def obter_tarefa(tarefa_id):
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)
    if tarefa:
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    try:
        validate(instance=dados, schema=schema)
    except ValidationError as e:
        return jsonify({"erro": "Dados inválidos", "detalhes": e.message}), 400

    tarefas = carregar_tarefas()
    if any(t["id"] == dados["id"] for t in tarefas):
        return jsonify({"erro": "ID já existente"}), 400
    tarefas.append(dados)
    guardar_tarefas(tarefas)
    return jsonify(dados), 201

@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    dados = request.get_json()
    try:
        validate(instance=dados, schema=schema)
    except ValidationError as e:
        return jsonify({"erro": "Dados inválidos", "detalhes": e.message}), 400

    tarefas = carregar_tarefas()
    for i, t in enumerate(tarefas):
        if t["id"] == tarefa_id:
            tarefas[i] = dados
            guardar_tarefas(tarefas)
            return jsonify(dados)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def eliminar_tarefa(tarefa_id):
    tarefas = carregar_tarefas()
    tarefas_filtradas = [t for t in tarefas if t["id"] != tarefa_id]
    if len(tarefas) == len(tarefas_filtradas):
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    guardar_tarefas(tarefas_filtradas)
    return jsonify({"mensagem": "Tarefa eliminada"})

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

