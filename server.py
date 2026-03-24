from socket import *
from constCS import *
import struct

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Servidor aguardando operações...")

while True:
    (conn, addr) = s.accept() 
    
    data = conn.recv(17)#Recebe exatamente 17 bytes: 1 (char) + 8 (double) + 8 (double)
    if not data or len(data) < 17: break

    # Desempacota os dados: 'c' para char, 'd' para dois doubles
    # O '!' no início indica "network byte order" (big-endian)
    op_byte, n1, n2 = struct.unpack('!cdd', data)
    op = op_byte.decode() # Converte b'+' para '+'

    print(n1,op,n2)
    
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    elif op == '/':
        res = n1 / n2 if n2 != 0 else 0.0
    else:
        res = 0.0

    # Retorna o resultado como um double binário (8 bytes)
    conn.send(struct.pack('!d', res))
    conn.close()


