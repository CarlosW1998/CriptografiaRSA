from Utility import *

def generatePublicKey(p, q, e):
    if not isPrime(q) or not isPrime(p):
        print("Numeros informados não são primos")
        return
    j = (p-1)*(q-1)
    if mdc(j, e) != 1:
        print("O expoente E não é relativamente primo")
        return
    f = open("Cheave.txt", 'w')
    f.write("(" + str(p*q) + ", " + str(e) + ")")
    f.close()

def cryptography(n, e, mensage):
    newMensage = ""
    for i in mensage:
        newMensage += str((convertToInt(i)**e)%n) + " "
    f = open("NewMensage.txt", 'w')
    f.write(newMensage)
    f.close()