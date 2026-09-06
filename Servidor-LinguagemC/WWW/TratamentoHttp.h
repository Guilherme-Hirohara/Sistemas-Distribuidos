long int lendo_binario(FILE *arq, char msg[]){
    char c; 
    long int tamanho; 

    fseek(arq, 0, SEEK_END); 
    tamanho = ftell(arq); 
    fseek(arq, 0, SEEK_SET); 

    fread(msg, 1, tamanho, arq); 
    return tamanho; 
}

long int lendo_html(FILE *arq, char msg[]){
    char c;
    int i=0;
    long int tamanho; 
    fseek(arq, 0, SEEK_END); 
    tamanho = ftell(arq); 
    fseek(arq, 0, SEEK_SET); 
    while((c = fgetc(arq))!=EOF){
        msg[i] = c;
        i++;
    }
    msg[i] = '\0';
    return tamanho; 
}

void procurarCaminho(char req[], char caminho[]){
    int i=0, posInicial, posFinal;
    while(req[i] !='\n'){
        if(req[i] == ' '){
            posInicial = i+2;
            i++;
            while(req[i] != ' ')
                i++;
            posFinal = i;
            break;
        }
        i++;
    }

    for(i = posInicial; i < posFinal; i++)
    {
        caminho[i- posInicial] = req[i];
        printf("%c", req[i]);
    }
    caminho[i-posInicial] = '\0';
}
void content_type(char caminho[], char contentType[]){ 
    if((strstr(caminho, "favicon")) != NULL){
        strcpy(contentType, "image/x-icon"); 
    }
    if((strstr(caminho, "estilo"))!=NULL){
        strcpy(contentType, "text/css"); 
    }
    if((strstr(caminho, "index"))!=NULL){
        strcpy(contentType, "text/html");
    }
    if((strstr(caminho, "bolo"))!=NULL){
        strcpy(contentType, "image/jpeg"); 
    }
    printf("\n\nContentType: %s\n\n", contentType); 
}

long int procurarPagina(char caminho[], char msg[], char contentType[]){
    FILE *arq;
    char c;
    int i=0;
    long int tam; 
    char pagina[200]; 

    content_type(caminho, contentType); 

    if(strcmp(caminho, "index") == 0){
        strcpy(pagina, LOCATION);
        strcat(pagina, "index.html");  
        arq = fopen(pagina, "r");
        tam = lendo_html(arq, msg);
    }else if(strcmp(caminho, "favicon.ico") == 0){
        strcpy(pagina, LOCATION);
        strcat(pagina, "favicon.ico");
        arq = fopen(pagina, "rb");
        tam = lendo_binario(arq, msg); 
    }else if(strcmp(caminho, "bolo.jpg") == 0){
        strcpy(pagina, LOCATION);
        strcat(pagina, "bolo.jpg");
        arq = fopen(pagina, "rb");
        tam = lendo_binario(arq, msg); 
    } else if(strcmp(caminho, "estilo.css") == 0){
        strcpy(pagina, LOCATION);
        strcat(pagina, "estilo.css");
        arq = fopen(pagina, "rb"); 
        tam = lendo_binario(arq,msg);
    }
    else{
        strcpy(pagina, LOCATION);
        strcat(pagina, "pagina404.html");
        arq = fopen(pagina, "r");
        tam = lendo_html(arq, msg);
        strcpy(contentType, "text/html"); 
    }

    fclose(arq);
    return tam; 
}





