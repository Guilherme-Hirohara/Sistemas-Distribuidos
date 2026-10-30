
const { log } = require("console");
const net = require("net");
const readline = require("readline");

const HOST = "127.0.0.1";
const PORT = 8081;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const socket = new net.Socket();


socket.connect(PORT, HOST, () => {
  console.log("---Cliente---\n");
  console.log(`Conectado ao servidor ${HOST}:${PORT}\n`);
  perguntarDocumento();
});

socket.on("error", (err) => {
  console.error(`\nErro de conexão: ${err.message}`);
  process.exit(1);
});


socket.on("data", (data) => {
  const resposta = data.toString().trim();
  console.log(`\nServidor: ${resposta}`);
  perguntarDocumento();
});

socket.on("close", () => {
  console.log("\nConexão encerrada.");
  rl.close();
  process.exit(0);
});


function perguntarDocumento() {
  rl.question("\nTipo (cpf/cnpj): ", (tipo) => {
    tipo = tipo.trim().toLowerCase();

    if(tipo == 'cpf'){
      tipo = 1; 
    }
    if(tipo == 'cnpj'){
      tipo = 0; 
    }

    rl.question(`Digite o documento: `, (documento) => {
      documento = documento.trim();

      console.log(documento); 

      tamanho = documento.length; 
      const mensagem = `protocolGui:${tipo}:${tamanho}:${documento}`;
      socket.write(mensagem, 'utf8');
    });
  });
}