import grpc
from concurrent import futures
import tarefa_pb2
import tarefa_pb2_grpc

# Dados de exemplo (como se fosse a base de dados)
TAREFAS = {
    1: {
        "id": 1,
        "titulo": "Tarefa gRPC",
        "descricao": "Exemplo de tarefa via gRPC",
        "concluida": False
    }
}

class TarefaServiceServicer(tarefa_pb2_grpc.TarefaServiceServicer):
    def ObterTarefa(self, request, context):
        tarefa = TAREFAS.get(request.id)
        if tarefa:
            return tarefa_pb2.TarefaReply(
                id=tarefa["id"],
                titulo=tarefa["titulo"],
                descricao=tarefa["descricao"],
                concluida=tarefa["concluida"]
            )
        else:
            context.set_details("Tarefa não encontrada")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return tarefa_pb2.TarefaReply()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tarefa_pb2_grpc.add_TarefaServiceServicer_to_server(TarefaServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC a correr em http://localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
