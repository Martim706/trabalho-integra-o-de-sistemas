import requests

URL = "http://localhost:5000/tarefas"

# 🟢 POST - Criar uma nova tarefa
nova_tarefa = {
    "id": 2,
    "titulo": "Tarefa 2",
    "descricao": "Criada via script Python",
    "concluida": False
}
res = requests.post(URL, json=nova_tarefa)
print("POST:", res.status_code, res.json())

# 🔵 GET - Obter todas as tarefas
res = requests.get(URL)
print("GET todas:", res.status_code, res.json())

# 🔵 GET - Obter tarefa específica
res = requests.get(f"{URL}/2")
print("GET tarefa 2:", res.status_code, res.json())

# 🟡 PUT - Atualizar tarefa
tarefa_atualizada = {
    "id": 2,
    "titulo": "Tarefa 2 editada",
    "descricao": "Editada via PUT",
    "concluida": True
}
res = requests.put(f"{URL}/2", json=tarefa_atualizada)
print("PUT:", res.status_code, res.json())

# 🔴 DELETE - Eliminar tarefa
res = requests.delete(f"{URL}/2")
print("DELETE:", res.status_code, res.json())
