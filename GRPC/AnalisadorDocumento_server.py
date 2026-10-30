from concurrent import futures 
import AnalisadorDocumento_pb2 
import AnalisadorDocumento_pb2_grpc
import grpc
class AnalisadorDocumentoServer(AnalisadorDocumento_pb2_grpc.AnalisadorDocumentoServicer):
    def analisandoDocumento(self, request, context):
        return super().analisandoDocumento(request, context)
    

def serve(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    AnalisadorDocumento_pb2_grpc.add_AnalisadorDocumentoServicer_to_server(AnalisadorDocumentoServer(), server) 
    server.add_insecure_port("localhost:8080")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__': 
    serve()