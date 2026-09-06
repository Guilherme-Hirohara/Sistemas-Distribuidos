# Sistemas Distribuídos (PEPSDIS)

Este repositório contém os códigos em Linguagem C e materiais práticos desenvolvidos durante a disciplina de **Sistemas Distribuídos** (Código: `PEPSDIS`), do curso de **Bacharelado em Ciência da Computação** do **Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) — Câmpus Presidente Epitácio**.

---

## 📌 Visão Geral da Disciplina

* **Instituição:** Instituto Federal de São Paulo (IFSP) - Câmpus Presidente Epitácio
* **Curso:** Bacharelado em Ciência da Computação
* **Componente Curricular:** Sistemas Distribuídos
* **Código:** PEPSDIS
* **Carga Horária Total:** 63,3 horas (76 aulas)
* **Linguagem Principal:** C

---

## 🎯 Objetivos

* Compreender e aplicar os principais conceitos, tecnologias, estratégias e problemas no projeto de sistemas distribuídos[cite: 1].
* Conhecer problemas inerentes aos sistemas distribuídos (exclusão mútua, concorrência, tempo global, replicação) e estratégias de solução[cite: 1].
* Utilizar técnicas e tecnologias para implementar comunicação entre processos via Sockets, MPI, RPC, entre outros[cite: 1].

---

## 🗺️ Conteúdo Programático

| Unidade[cite: 1] | Tópicos Cobertos[cite: 1] | Foco das Aulas Práticas (C) |
| :--- | :--- | :--- |
| **01. Introdução** | Caracterização, tipos e desafios de sistemas distribuídos[cite: 1] | Conceitos de arquitetura e concorrência |
| **02. Estudos de Casos** | Domain Name System (DNS) e World Wide Web (WWW)[cite: 1] | Clientes HTTP simples e resolução de nomes |
| **03. Arquiteturas** | Estilos arquiteturais, organização de middleware e sistemas[cite: 1] | Estruturação de middlewares em C |
| **04. Comunicação** | Sockets POSIX, empacotamento de dados, difusão seletiva e MPI[cite: 1] | Sockets TCP/UDP, Chat multithread, OpenMPI |
| **05. Implementação** | Tempo/relógios globais, coordenação, concorrência e replicação[cite: 1] | Mutex (`pthread`), algoritmos de eleição e acordo |
| **06. Invocação Remota** | Conceitos e implementação de chamadas remotas[cite: 1] | Implementação de RPC (Remote Procedure Call) |
| **07. Comunicação Indireta** | Conceitos de pub/sub e filas de mensagens[cite: 1] | Filas de mensagens POSIX / System V |
| **08. Objetos Distribuídos**| Conceitos e componentes distribuídos[cite: 1] | Componentes e interfaces remotas |
| **09. Serviços Web** | Conceitos e arquiteturas de Web Services[cite: 1] | Consumo de serviços via C |
| **10. Arquivos Distribuídos**| Sistemas de arquivos distribuídos[cite: 1] | Leitura/escrita e sincronização de arquivos |
| **11. Processamento Paralelo**| Práticas de processamento paralelo distribuído[cite: 1] | Algoritmos de divisão de tarefas |
| **12. Computação Ubíqua**| Computação móvel, IoT e estudos de caso[cite: 1] | Comunicação entre nós heterogêneos |
| **13. Computação em Nuvem**| Conceitos de nuvem e práticas[cite: 1] | Deploy e teste de nós distribuídos |
