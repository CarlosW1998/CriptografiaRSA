def mdc(a, b):
    k = a%b
    if k == 0: return  b
    return mdc(b, k)

def isPrime(i):
    k = int(i**(1/2))
    for a in range(2, k+1):
        if i%a == 0:
            return False
    return True

def inverseMod(a, b):
    a = a%b
    for i in range(1, b):
        if(i*a)%b == 1: return i
    return  1

def convertToInt(i):
    if i == ' ': return 26
    return ord(i) - 65

def convertToChar(i):
    if i==26: return " "
    return  chr(65+i)