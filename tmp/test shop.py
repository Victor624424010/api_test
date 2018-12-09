from suds.client import Client
service = Client('http://115.28.108.130:4000/?wsdl').service
result = service.addUser('范火火','123456')
print(result)