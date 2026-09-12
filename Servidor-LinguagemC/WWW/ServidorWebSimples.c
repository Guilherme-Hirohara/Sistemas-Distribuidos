/// Define servidor web simples
/// Incluir no Settings -> Compiler -> Linker Settings: -l wsock32

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#define LOCATION "tmp/www/"
#define PORT 8080
#define MESSAGESIZE 262144
#define MAXSOCKETS 20
#include "TratamentoHttp.h"


typedef struct HttpInfo
{
  char message[MESSAGESIZE], conteudo[MESSAGESIZE], contentType[30], header[512], caminho[50];
  int len;
  long int tam;
} httpInfo;

int new_socket[MAXSOCKETS];
int qtde=0; 
httpInfo http[MAXSOCKETS]; 

void* enviarHttp(void* dados)
{
  int verificar; 
  char requisicao[8]; 
  int pos = (int)(long)dados; 
    http[pos].len = recv(new_socket[pos], http[pos].message, MESSAGESIZE, 0);
    if (http[pos].len > 0)
    {
      procurar_requisicao(http[pos].message, requisicao); 
      verificar = verificar_requisicao(requisicao);
      printf("\n\nVerificar -> %d\n\n", verificar);  
      if(verificar){
        
        sprintf(http[pos].header,  "HTTP/1.1 501 Not Implemented\r\n"
              "Server: GuilhermeServidor\r\n"
              "Content-Length: %ld\r\n"
              "Content-Type: text/html\r\n"
              "Connection: close\r\n"
              "\r\n"
              "<h1>Error 501<h1><h2>Not Implemented method %s", 44+strlen(requisicao), requisicao); 
        send(new_socket[pos], http[pos].header, strlen(http[pos].header), 0); 
      }
      else{
        procurarCaminho(http[pos].message, http[pos].caminho);
        http[pos].tam = procurarPagina(http[pos].caminho, http[pos].conteudo, http[pos].contentType);
        // Resposta ao cliente
        http[pos].message[http[pos].len] = '\0';
        
        sprintf(http[pos].header,
          "HTTP/1.1 200 OK\r\n"
          "Server: GuilhermeServidor\r\n"
          "Content-Length: %ld\r\n"
          "Content-Type: %s\r\n"
          "Connection: close\r\n"
          "\r\n",
          http[pos].tam, http[pos].contentType);
          fflush(stdout);
          
          puts(http[pos].header);
          puts(http[pos].conteudo);
          send(new_socket[pos], http[pos].header, strlen(http[pos].header), 0);
          send(new_socket[pos], http[pos].conteudo, http[pos].tam, 0);

        }
    }
    close(new_socket[pos]); 

    return NULL; 
}

int main(int argc, char *argv[])
{
  pthread_t idThread; 
  int s, pos;
  struct sockaddr_in server, client;
  int c; 
  

  // Inicializa o descritor do socket
  s = socket(AF_INET, SOCK_STREAM, 0);

  // Prepara��o da estrutura (struct) sockaddr_in
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = INADDR_ANY; /// 0.0.0.0
  server.sin_port = htons(PORT);

  // Constr�i o socket -> solicita uso da porta ao SO
  bind(s, (struct sockaddr *)&server, sizeof(server));

  // Come�a a escutar na porta
  listen(s, 3);

  // Caso chegue uma conex�o, a fun��o accept ir� verificar se ir� aceit�-la ou n�o
  c = sizeof(struct sockaddr_in);

  while (qtde<MAXSOCKETS)
  {
    pos = qtde % MAXSOCKETS; 
    new_socket[pos] = accept(s, (struct sockaddr *)&client, &c);
    printf("\nConexao aceita\n");
    printf("\nDados do cliente - IP: %s -  Porta: %d\n", inet_ntoa(client.sin_addr), htons(client.sin_port));
    pthread_create(&idThread, NULL, enviarHttp, (void*)(long)pos); 
    printf("\nId da thread\n"); 
    printf("id: %ld\n", idThread);

    qtde++;
  }
  getchar();

  close(s);

  return 0;
}
