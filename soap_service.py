from spyne import Application, rpc, ServiceBase, Integer, Unicode, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import xml.etree.ElementTree as ET

XML_FILE = 'tarefas.xml'

def carregar_tarefas():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    tarefas = []
    for tarefa in root.findall('tarefa'):
        tarefas.append({
            'id': int(tarefa.find('id').text),
            'titulo': tarefa.find('titulo').text,
            'descricao': tarefa.find('descricao').text,
            'concluida': tarefa.find('concluida').text == 'true'
        })
    return tarefas

class TarefaService(ServiceBase):

    @rpc(Integer, _returns=Unicode)
    def obter_tarefa(ctx, tarefa_id):
        tarefas = carregar_tarefas()
        for t in tarefas:
            if t["id"] == tarefa_id:
                return f'{t["id"]} - {t["titulo"]} - {t["descricao"]} - Concluída: {t["concluida"]}'
        return "Tarefa não encontrada"

app = Application([TarefaService], 'soap.tarefas',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("Servidor SOAP disponível em http://localhost:8000/")
    servidor = make_server('0.0.0.0', 8000, wsgi_app)
    servidor.serve_forever()

