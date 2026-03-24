from socket import *
from constCS import *
import struct

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("--- Calculadora Remota ---")
print("Operacoes aceitas: + , - , * , /")
print("Exemplo de digitacao: 10 + 20")
print("-" * 30)

try:
    while True:
        entrada = input("Digite a operaçao e os numeros: ")  #Le a entrada do usuário
        partes = entrada.split()

        if len(partes) != 3:
            print("Erro: Formato invalido. Use: <num1> <op> <num2>")
        else: #Prepara os dados
            op = partes[1].encode('ascii')
            n1 = float(partes[0])
            n2 = float(partes[2])

            pacote = struct.pack('!cdd', op, n1, n2)
            s.send(pacote)
          
            data = s.recv(8) # Recebe a resposta (8 bytes do double)
            if data:
                resultado = struct.unpack('!d', data)[0]
                print(f"\nResposta do Servidor: {resultado}")
            else:
                print("\nServidor fechou a conexão sem resposta.")

except ValueError:
    print("Erro: Certifique-se de digitar numeros validos.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    s.close()
    print("\nConexao encerrada.")
