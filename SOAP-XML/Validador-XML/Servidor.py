from spyne import Application, rpc, ServiceBase, Unicode, String, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit() or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"

def validar_cnpj(cnpj):
    if len(cnpj) != 14 or not cnpj.isdigit() or cnpj == cnpj[0] * 14:
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    return cnpj[-2:] == f"{digito1}{digito2}"

class ValidadorDocumento(ServiceBase): 
    @rpc(Integer, Unicode, _returns=Unicode)
    def analisar_documento(ctx, tipo, doc): 
            if tipo == 0:
                if validar_cpf(doc):
                    return "CPF válido e dentro do padrão XSD!"
                else:
                    return "CPF inválido (dígitos verificadores incorretos ou tamanho incompatível)!"
            elif tipo == 1:
                if validar_cnpj(doc):
                    return "CNPJ válido e dentro do padrão XSD!"
                else:
                    return "CNPJ inválido (dígitos verificadores incorretos ou tamanho incompatível)!"
            else:
                return "Documento Inválido (Quantidade de dígitos errado)";  

application = Application(
    [ValidadorDocumento], 
    tns='analisador.service', 
    in_protocol=Soap11(validator='lxml'), 
    out_protocol=Soap11()
)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    print("======= Servidor SOAP iniciado na porta 8000 =======")
    print("WSDL disponível em: http://localhost:8000/?wsdl\n")
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()




