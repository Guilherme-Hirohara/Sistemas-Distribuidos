var soap = require('soap'); //Biblioteca Soap 
const url = "http://localhost:8000/?wsdl" //Servidor 
const readline =  require('readline/promises'); 

const teclado = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
}); 

function analisando_documento(doc){
    if(doc.length == 11){
        tipo = 0; 
    }
    else if(doc.length == 14){
        tipo = 1; 
    }
    else{
        tipo = -1; 
    }
    return tipo;
}

async function criando_cliente(){
    const doc = await teclado.question('Digite seu CPF ou CNPJ: ');
    teclado.close();
    docLimpo = doc.replace(/\D/g, ""); 
    tipoDoc = analisando_documento(docLimpo);  
    try{
        const client = await soap.createClientAsync(url); 

        const dados = {
            tipo: tipoDoc, 
            doc: docLimpo
        }; 

        const [resposta] = await client.analisar_documentoAsync(dados); 

        console.log("\nResposta do Servidor Analisar documento\n"); 
        console.log(resposta.analisar_documentoResult); 
    }catch(err){
        console.error("Erro ao na comunicação com o servidor"); 
    }
}

criando_cliente(); 
