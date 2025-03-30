import grpc
import tarefa_pb2
import tarefa_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = tarefa_pb2_grpc.TarefaServiceStub(channel)

    resposta = stub.ObterTarefa(tarefa_pb2.TarefaRequest(id=1))

    print("Resposta do servidor gRPC:")
    print("ID:", resposta.id)
    print("Título:", resposta.titulo)
    print("Descrição:", resposta.descricao)
    print("Concluída:", resposta.concluida)

if __name__ == '__main__':
    run()
