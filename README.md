
# Trabalho Individual - Integração de Sistemas

## 👤 Autor: Martim Nunes  
**Repositório:** `trabalho-integra-o-de-sistemas`

---

## 📦 Projeto: Microserviços em Python

Este projeto implementa uma aplicação com múltiplos microserviços utilizando diferentes tecnologias:

- ✅ REST com Flask
- ✅ SOAP com Zeep/XML
- ✅ gRPC com Protocol Buffers
- ✅ GraphQL com Graphene
- ✅ Validação com JSON Schema e XML Schema
- ✅ Testes realizados via código Python (`requests`)

---

## 🛠️ Requisitos

- Python 3.10
- Ambiente virtual ativo (venv310)

---

## 🚀 Como executar

### 1. Ativar o ambiente virtual

```bash
.env310\Scriptsctivate
```

### 2. REST API

```bash
python rest_api.py
```

### 3. SOAP

```bash
python soap_service.py
python cliente_soap.py
```

### 4. gRPC

```bash
python servidor_grpc.py
python cliente_grpc.py
```

### 5. GraphQL

```bash
python graphql_api.py
```

---

## 📁 Estrutura de ficheiros

```
servidor/
├── venv310/
├── rest_api.py
├── soap_service.py
├── cliente_soap.py
├── tarefa.proto
├── tarefa_pb2.py
├── tarefa_pb2_grpc.py
├── servidor_grpc.py
├── cliente_grpc.py
├── graphql_api.py
├── tarefas.json
├── schema.json
├── tarefas.xml
├── schema.xsd
├── test_post.py
├── testes_rest.py
```

---

## ✅ Estado do Projeto

| Componente | Estado |
|------------|--------|
| REST       | ✅     |
| SOAP       | ✅     |
| gRPC       | ✅     |
| GraphQL    | ✅     |
| JSON/XML   | ✅     |
| Testes     | ✅     |

---

## 📝 Licença

Este projeto é parte de um trabalho académico e não tem fins comerciais.
