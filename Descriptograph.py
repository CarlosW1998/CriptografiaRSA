from Utility import inverseMod

def descriptograph(p, q, e):
    f = open("NewMensage.txt", 'r', encoding='utf-8')
    mensage = f.read()
    f.close()
    d = inverseMod(e, (p - 1) * (q - 1))
    descriptMensage = ""
    print(mensage)
    for i in mensage:
        descriptMensage += chr((ord(i)**d)%(p*q))
    f = open("DescriptMensage.txt", 'w', encoding='utf-8')
    f.write(descriptMensage)
    f.close()