import grpc 
import teste_pb2_grpc as analisador_documento_pb2_grpc
import teste_pb2 as analisador_documento_pb2 
import logging

def run():
    with grpc.insecure_channel("localhost:8080") as channel: 
        stub = analisador_documento_pb2_grpc.ServicoValidadoStub(channel)
        valido = stub.Validar(analisador_documento_pb2.RequestDoc(nome='ProtocolGui', doc = '540.096.128-27', tipo = 1))
        print(valido)

if __name__ == "__main__":
    logging.basicConfig()
    run() 