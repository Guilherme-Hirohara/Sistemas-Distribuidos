package edu.pep.ifsp.Analisador;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class Cliente {

    public static void main(String[] args) {
        ManagedChannel canal = ManagedChannelBuilder
                .forAddress("localhost", 8080)
                .usePlaintext()
                .build();

        ServicoValidadoGrpc.ServicoValidadoBlockingStub stub =
                ServicoValidadoGrpc.newBlockingStub(canal);

        RequestDoc requisicao = RequestDoc.newBuilder()
                .setNome("ProtocolGui")
                .setDoc("11.444.777/0001-61")
                .setTipo(2)
                .build();

        ReplyDoc resposta = stub.validar(requisicao);
        if(resposta.getTipoErro() == 1){
            System.out.println("Sucesso!!\n" + resposta.getMensagem());
        }
        else{
            System.out.println("Erro " + resposta.getTipoErro() + " \n" + resposta.getMensagem());
        }
        canal.shutdown();
    }
}