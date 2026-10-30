import socket
import threading

HOST = "127.0.0.1"     
PORT = 8081       
MESSAGESIZE = 255      

clientes = []

lock = threading.Lock()

def encontrarDivisao(mensagem): 
    local = []
    for i in range(len(mensagem)): 
        if(mensagem[i]==':'): 
            local.append(i)

    return local

def calcularDigitoVerificador(numeros, pesos):
    soma = sum(int(digito) * peso for digito, peso in zip(numeros, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def verificarDigito(doc, tipoDoc):
    if tipoDoc:  
        if len(doc) != 11:
            return False
        pesos1 = list(range(10, 1, -1)) 
        pesos2 = list(range(11, 1, -1)) 
        digito1 = calcularDigitoVerificador(doc[:9], pesos1)
        digito2 = calcularDigitoVerificador(doc[:10], pesos2)
    else: 
        if len(doc) != 14:
            return False
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digito1 = calcularDigitoVerificador(doc[:12], pesos1)
        digito2 = calcularDigitoVerificador(doc[:13], pesos2)

    return doc[-2:] == f"{digito1}{digito2}"

def analisarTipoDoDocumento(local, mensagem):
    doc = mensagem[local[0]+1:local[1]]
    return doc


def verificarTamanho(local, mensagem, tipoDoc):
    tam = mensagem[local[1]+1:local[2]]
    tam = int(tam)
    if tipoDoc == 1: 
        if tam == 14 or tam == 11: 
            return tam
        else: 
            return 502 
    if tipoDoc == 0:  
        if tam == 14 or tam == 18: 
            return tam 
        else: 
            return 502

def calcularDigitoVerificador(numeros, pesos):
    soma = sum(int(digito) * peso for digito, peso in zip(numeros, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto
 
 
 
def validarCPF(doc):
    if len(doc) != 11 or not doc.isdigit():
        return False
 
    pesos1 = list(range(10, 1, -1))
    pesos2 = list(range(11, 1, -1))
    digito1 = calcularDigitoVerificador(doc[:9], pesos1)
    digito2 = calcularDigitoVerificador(doc[:10], pesos2)
 
    return doc[-2:] == f"{digito1}{digito2}"

def verificarDocumentacao(local, mensagem, tipoDoc): 
    doc = mensagem[local[2]+1:]
    tam = verificarTamanho(local, mensagem, tipoDoc)
    if tam == 502:
        return 3
    
    docLimpo = doc.replace(".", "").replace("-", "").replace("/", "")


    if not verificarDigito(docLimpo, tipoDoc):
        return 4
    else:
        return 1 

def enviarReposta(tipoRes, tipoDoc): 
    protocolo = "protocolGui"
    tipo = str(tipoRes)

    if tipoDoc == -1: 
       doc = "-1"
    else: 
       doc = 'cpf' if tipoDoc else 'cnpj'

    match tipoRes: 
        case 1: 
            mensagem = "Documento valido"
        case 2: 
            mensagem = "Tipo de documento inválido"
        case 3: 
            mensagem = "Tamanho incorreto do documento"
        case 4:
            mensagem = "Digito verificador invalido"
        case 5: 
            mensagem = "Campo não definido"

    tam = str(len(mensagem))
    resposta = protocolo+":"+tipo+":"+doc+":"+tam+":"+mensagem
    return resposta

def getdata(conn, addr):
    while True:
        try:
            data = conn.recv(MESSAGESIZE)  
        except ConnectionResetError:
            break

        if not data:
            break
        mensagem = data.decode("utf-8")
        local = encontrarDivisao(mensagem)
        if(len(local) == 3):
            tipoDoc = analisarTipoDoDocumento(local, mensagem)
            if(tipoDoc != '1' and tipoDoc != '0'):
                res = enviarReposta(2, -1) 
            else: 
                tipoRes = verificarDocumentacao(local, mensagem, tipoDoc)
                print(tipoRes)
                res = enviarReposta(tipoRes, tipoDoc)
        else:
            res = enviarReposta(5, -1) 
        

        try:
            conn.sendall((res + "\n").encode())
        except OSError:
            pass  

    with lock:
        if conn in clientes:
            clientes.remove(conn)
    conn.close()
    print(f"\nConexão encerrada - {addr}")


def main():
    print("-----Servidor-----\n\n")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((HOST, PORT))  
    s.listen(3)             

    try:
        while True:
  
            conn, addr = s.accept()

            with lock:
                clientes.append(conn)

            print("\nConexao aceita.")
            print(f"Dados do cliente - IP: {addr[0]} - Porta: {addr[1]}")

            t = threading.Thread(target=getdata, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
    finally:
        s.close()  


if __name__ == "__main__":
    main()