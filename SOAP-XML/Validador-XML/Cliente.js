const soap = require('soap'); //Biblioteca Soap 
const url = "http://localhost:8080/" //Servidor 
const readline =  require('readline/promises'); 

const teclado = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
}); 

async function criando_xml(){
    let xml; 
    const tipo = await teclado.question("Digite o tipo de documento: (0 - CPF e 1 - CNPJ)"); 
    let doc = await teclado.question("Digite o documento:"); 
    doc = doc.replaceAll(".", "").replaceAll("-", "").replaceAll("/", ""); 
    teclado.close(); 

    xml = `<documento><tipo>${tipo}</tipo><doc>${doc}</doc></documento>`

    return {
        xml_conteudo: xml
    }; 
}

async function enviar_soap(doc_xml){
    const dados_soap = await criando_xml(); 
    const cliente = await soap.createClientAsync(url); 

    const [resposta] = await cliente.AnalisadorDocumentoAsync(dados_soap); 

    console.log("Resposta: ", resposta); 
}

enviar_soap(); 
