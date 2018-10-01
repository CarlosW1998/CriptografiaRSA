from Cryptography import generatePublicKey, cryptography
from Descriptograph import descriptograph

print("Ditite:")
print("0 - Sair")
print("1 - Gerar Chave Publica")
print("2 - Criptografar")
print("3 - Descriptografar")
i = int(input())
while i != 0:
    if i == 1:
        print("Digite dois primos P e Q e um expoente E relativamente primo")
        p, q, e = map(int, input().split())
        generatePublicKey(p, q, e)
    if i == 2:
        print("Digite a Chave public (N, E) para criptografar a mensagem")
        n, e = map(int, input().split())
        print("Digite a mensagem a ser codificada:")
        mensage = input()
        cryptography(n, e, mensage)
    if i == 3:
        print("Digite as chaves P, Q e E")
        p, q, e = map(int, input().split())
        descriptograph(p, q, e)
    print("Ditite:")
    print("0 - Sair")
    print("1 - Gerar Chave Publica")
    print("2 - Criptografar")
    print("3 - Descriptografar")
    i = int(input())
