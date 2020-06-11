import os
path = os.path.dirname(os.path.realpath(__file__))+'\ErrorLog.txt'


def logError(error):
    file = open(path,'a')
    file.write(error+'\n')
    file.close()

def readErrorLog():
    file = open(path,'r')
    errors = file.readlines()
    return errors

def theresErrors():
    file = open(path,'r')
    errors = file.readlines()
    if errors == []:
        return False
    return True

def wipeErrorLog():
    file = open(path, "r+")
    file.truncate(0)
    file.close()

