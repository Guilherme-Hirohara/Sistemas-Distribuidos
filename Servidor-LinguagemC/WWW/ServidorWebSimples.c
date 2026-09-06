/// Define servidor web simples
/// Incluir no Settings -> Compiler -> Linker Settings: -l wsock32

#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#define LOCATION "tmp/www/"
#include "TratamentoHttp.h"
#define PORT 8080
#define MESSAGESIZE 262144 

int main(int argc , char *argv[]) {

  int s, new_socket;
  struct sockaddr_in server , client;
  int c, len;
  long int tam; 
  char message[MESSAGESIZE], caminho[50], conteudo[MESSAGESIZE], contentType[30], header[512];

  //Inicializa o descritor do socket
  s = socket(AF_INET , SOCK_STREAM , 0 );

  //Prepara��o da estrutura (struct) sockaddr_in
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = INADDR_ANY; ///0.0.0.0
  server.sin_port = htons(PORT);

  //Constr�i o socket -> solicita uso da porta ao SO
  bind(s ,(struct sockaddr *)&server , sizeof(server));

  //Come�a a escutar na porta
  listen(s,3);

  //Caso chegue uma conex�o, a fun��o accept ir� verificar se ir� aceit�-la ou n�o
  c = sizeof(struct sockaddr_in);
  
  
  while(1) {
    new_socket = accept(s, (struct sockaddr *)&client, &c);
    printf("\nConexao aceita\n");
    printf("\nDados do cliente - IP: %s -  Porta: %d\n",inet_ntoa(client.sin_addr),htons(client.sin_port));
    //Recep��o da mensagem
    len=recv(new_socket,message,MESSAGESIZE,0);
    if(len>0) {
    procurarCaminho(message, caminho);
    tam = procurarPagina(caminho, conteudo, contentType);
      //Resposta ao cliente
      message[len]='\0';

      sprintf(header,
        "HTTP/1.1 200 OK\r\n"
        "Server: GuilhermeServidor\r\n"
        "Content-Length: %ld\r\n"
        "Content-Type: %s\r\n"
        "Connection: close\r\n"
        "\r\n",
        tam, contentType);
        fflush(stdout);
      send(new_socket, header, strlen(header), 0);
      send(new_socket, conteudo, tam, 0); 
    }
  }
  getchar();


  close(s);




  return 0;
}
