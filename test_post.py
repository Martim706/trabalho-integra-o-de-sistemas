import requests

url = "http://localhost:5000/tarefas"

tarefa = {
    "id": 1,
    "titulo": "Tarefa via Python",
    "descricao": "Criada com requests em vez do Postman",
    "concluida": False
}

resposta = requests.post(url, json=tarefa)

print("Status:", resposta.status_code)
print("Resposta:", resposta.json())
