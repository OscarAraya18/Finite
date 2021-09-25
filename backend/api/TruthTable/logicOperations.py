def NOT(a):
    result = []
    for i in range(0,len(a)):
        result.append(not a[i])
    return result

def AND(a,b):
    result = []
    for i in range(0,len(a)):
        result.append(a[i] and b[i])
    return result

def OR(a,b):
    result = []
    for i in range(0, len(a)):
        result.append(a[i] or b[i])
    return result

def XOR(a,b):
    result = []
    for i in range(0, len(a)):
        result.append(a[i] ^ b[i])
    return result

def NAND(a,b):
    result = []
    for i in range(0, len(a)):
        result.append(not(a[i] and b[i]))
    return result

def NOR(a,b):
    result = []
    for i in range(0, len(a)):
        result.append(not(a[i] or b[i]))
    return result

def XNOR(a,b):
    result = []
    for i in range(0, len(a)):
        result.append(not(a[i] ^ b[i]))
    return result
