from zeep import Client

wsdl = 'http://localhost:8000/?wsdl'

client = Client(wsdl=wsdl)

# Chamada ao método obter_tarefa
resposta = client.service.obter_tarefa(1)

print("Resposta do serviço SOAP:")
print(resposta)
