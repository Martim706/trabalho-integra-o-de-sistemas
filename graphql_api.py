from flask import Flask, request, jsonify
import graphene
import json
import os

DATA_FILE = 'tarefas.json'

# Utilitários para JSON
def carregar_tarefas():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def guardar_tarefas(tarefas):
    with open(DATA_FILE, 'w') as f:
        json.dump(tarefas, f, indent=2)

# GraphQL types
class Tarefa(graphene.ObjectType):
    id = graphene.Int()
    titulo = graphene.String()
    descricao = graphene.String()
    concluida = graphene.Boolean()

# Query
class Query(graphene.ObjectType):
    todas_tarefas = graphene.List(Tarefa)
    tarefa_por_id = graphene.Field(Tarefa, id=graphene.Int(required=True))

    def resolve_todas_tarefas(root, info):
        return carregar_tarefas()

    def resolve_tarefa_por_id(root, info, id):
        tarefas = carregar_tarefas()
        for t in tarefas:
            if t["id"] == id:
                return t
        return None

# Mutation
class CriarTarefa(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        titulo = graphene.String()
        descricao = graphene.String()
        concluida = graphene.Boolean()

    tarefa = graphene.Field(lambda: Tarefa)

    def mutate(root, info, id, titulo, descricao, concluida):
        tarefas = carregar_tarefas()
        nova = {
            "id": id,
            "titulo": titulo,
            "descricao": descricao,
            "concluida": concluida
        }
        tarefas.append(nova)
        guardar_tarefas(tarefas)
        return CriarTarefa(tarefa=nova)

class Mutation(graphene.ObjectType):
    criar_tarefa = CriarTarefa.Field()

# Schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# App Flask
app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_api():
    data = request.get_json()
    result = schema.execute(data["query"])
    return jsonify(result.data)

if __name__ == "__main__":
    app.run(debug=True)
