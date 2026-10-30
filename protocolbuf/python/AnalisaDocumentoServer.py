import teste_pb2 as analisador_documento_pb2 
import teste_pb2_grpc as analisador_documento_pb2_grpc
import grpc
import concurrent.futures as futures

def analisarCnpj(doc): 
    doc = doc.replace('.','').replace('/', '').replace("-", "")
    doc1 = [] 
    for item in doc: 
        doc1.append(int(item))
    if(len(set(doc))==0):
        return 3
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = 0

    for i in range(12):
        soma = soma + (doc1[i] * pesos1[i])
    resto = soma%11 

    if(resto<=1):
        digito1 = 0
    else: 
        digito1 = 11 - resto

    soma = 0 
    for i in range(13):
        soma = soma + (doc1[i] * pesos2[i])
    resto = soma%11 

    if(resto<=1):
        digito2 = 0 
    else: 
        digito2 = 11 - resto 

    if(doc1[12] == digito1 and doc1[13] == digito2):
        return 1 
    return 2     

def analisarCpf(doc): 
    doc = doc.replace('.', "").replace('-', "")
    doc1 = []
    for item in doc:    
        doc1.append(int(item))
    if(len(set(doc)) == 0): 
        3
    pesos1 = [10, 9, 8, 7, 6 , 5, 4, 3, 2]
    pesos2 = [11, 10, 9, 8, 7, 6 , 5, 4, 3, 2]
    soma = 0
    for i in range(9):
        soma = soma + (doc1[i] * pesos1[i])

    resto = soma % 11
    if(resto <=1): 
        digito1 = 0 
    else:
        digito1 = abs(resto - 11)

    soma = 0
    for i in range(10): 
        soma = soma + (doc1[i] * pesos2[i])
    resto = soma % 11 
    if (resto<=1):
        digito2 = 0 
    else: 
        digito2 = abs(resto - 11) 


    
    if digito1 == doc1[9] and digito2 == doc1[10]: 
        return 1
    return 2


def mensagemDeResposta(tipo):
    if tipo == 1: 
        return "Seu documento esta valido" 
    if tipo == 2: 
        return "Documento com digitos incorretos" 
    if tipo == 3: 
        return "Documento com mesmo valor em todos os campos"

class AnalisadorDocumentoService(analisador_documento_pb2_grpc.ServicoValidadoServicer):
    def Validar(self, request, context):
        if(request.tipo == 1):
            validarDoc = analisarCpf(request.doc)
        else: 
            validarDoc = analisarCnpj(request.doc)
        mensagemResposta = mensagemDeResposta(validarDoc)
        return analisador_documento_pb2.ReplyDoc(mensagem=mensagemResposta, nome="ProtocolGui", tipo_erro=validarDoc)



def server(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analisador_documento_pb2_grpc.add_ServicoValidadoServicer_to_server(AnalisadorDocumentoService(), server)
    server.add_insecure_port("localhost:8080")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__": 
    server()