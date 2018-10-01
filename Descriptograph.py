from Utility import inverseMod, convertToChar

def descriptograph(p, q, e):
    f = open("NewMensage.txt", 'r')
    mensage = list(map(int, f.read().split()))
    f.close()
    d = inverseMod(e, (p - 1) * (q - 1))
    descriptMensage = ""
    for i in mensage:
        descriptMensage += convertToChar((i**d)%(p*q))
    f = open("DescriptMensage.txt", 'w')
    f.write(descriptMensage)
    f.close()