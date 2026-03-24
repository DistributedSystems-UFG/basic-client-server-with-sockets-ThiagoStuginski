# Calculadora Remota via Sockets (Protocolo Binário)

Este projeto consiste em um sistema cliente-servidor desenvolvido em Python para a realização de operações matemáticas remotas utilizando sockets TCP e comunicação binária.

## Funcionalidades
O servidor processa quatro operações principais enviadas pelo cliente:
* **Soma (`+`)**
* **Subtração (`-`)**
* **Multiplicação (`*`)**
* **Divisão (`/`)**

## Diferencial Técnico: Comunicação Binária
Diferente de implementações baseadas em strings, este sistema utiliza o módulo `struct` do Python para empacotar os dados em formato binário (Network Byte Order).
* **Requisição (17 bytes):** 1 byte para a operação (char) e 16 bytes para dois números de precisão dupla (double).
* **Resposta (8 bytes):** Retorno do resultado diretamente como um double.

## Exemplos de entradas
124 + 95

5 * 85.6

12 / 57

98.0048 - 336.756
