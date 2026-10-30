from http.server import HTTPServer #Esta biblioteca importa o servidor HTTP para a comunicação entre o serviço e o cliente 
import pysimplesoap  
from lxml import etree; 


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


def analisar_documento(xml_conteudo): 
    try:
        schema_xsd = etree.XMLSchema(etree.parse("documento.xsd")); 
        conteudo = etree.fromstring(xml_conteudo.encode("utf-8")); 
        schema_xsd.assertValid(conteudo) 

        dados = pysimplesoap.simplexml.SimpleXMLElement(xml_conteudo); 
        tipo = int(str(dados.tipo).strip()); 
        doc = str(dados.doc).strip(); 
    
        if tipo == 0:
            if validar_cpf(doc):
                return {"valido": True, "mensagem": "CPF válido e dentro do padrão XSD!"}
            else:
                return {"valido": False, "mensagem": "CPF inválido (dígitos verificadores incorretos ou tamanho incompatível)!"}
        elif tipo == 1:
            if validar_cnpj(doc):
                return {"valido": True, "mensagem": "CNPJ válido e dentro do padrão XSD!"}
            else:
                return {"valido": False, "mensagem": "CNPJ inválido (dígitos verificadores incorretos ou tamanho incompatível)!"}

        return {"valido": False, "mensagem": "Tipo de documento inválido!"}; 
    except etree.DocumentInvalid as err:
        return {"valido": False, "mensagem": f"Está fora do padrão XSD: {err}"}; 
    except Exception as erro: 
        return {"valido": False, "mensagem": f"Erro ao processar o XMl: {erro}"}; 



dispatcher = pysimplesoap.server.SoapDispatcher(
    name = "ValidadorDocumentoServer", #Nome 
    location = "http://localhost:8080",  #Servidor que vai rodar 
    action = "http://localhost:8080", #Cabeçalho padrãoi do SOAP 
    namespace="http://localhost:8080/validadadordocumento.wsdl", #Identificador do XML do serviço 
    prefix="doc", #Apelido das tags XMl 
    trace=True, #Irá imprimir XML SOAP na tela do terminal 
    ns = True #Ativa o uso de namespace XML, Isso é feito por conta que o meu cliente é em JAVA e ele pode reclamar por não ter 
)

#Resgistra a função no meu servidor SOAP 
dispatcher.register_function(
    "AnalisadorDocumento", 
    analisar_documento, 
    returns={"valido": bool, "mensagem": str}, 
    args={"xml_conteudo": str}
) 

if __name__ == "__main__":
    print("=======Servidor SOAP Iniciado na porta 8080=====\n\n")
    httpn = HTTPServer(("", 8080), pysimplesoap.server.SOAPHandler)
    httpn.dispatcher = dispatcher #Conecta o nosso dispatcher com o nosso servidor
    httpn.serve_forever() #Servidor fica ligado até o cliente sair com ctrl+c




