from api.TruthTable.lexicalAnalyzer import *
from api.TruthTable.logicOperations import *

precedence = (
    ('left','AND'),
    ('left','OR'),
    ('left','XOR'),
    ('left','NAND'),
    ('left','NOR'),
    ('left','XNOR'),
    ('left', 'NOT')

)

data = ''

operandsDictionary = startLexicalAnalysis(data)
operationIndex = 1

def p_expression_logicOperation(t):
    '''expression : NOT expression
                  | expression AND expression
                  | expression OR expression
                  | expression XOR expression
                  | expression NAND expression
                  | expression NOR expression
                  | expression XNOR expression'''
    global operationIndex
    if t[2] == 'xno':
        operandsDictionary[operationIndex] = XNOR(operandsDictionary[t[1]], operandsDictionary[t[3]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1
    elif t[2] == 'xo':
        operandsDictionary[operationIndex] = XOR(operandsDictionary[t[1]], operandsDictionary[t[3]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1
    elif t[2] == 'na':
        operandsDictionary[operationIndex] = NAND(operandsDictionary[t[1]], operandsDictionary[t[3]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1
    elif t[2] == 'no':
        operandsDictionary[operationIndex] = NOR(operandsDictionary[t[1]], operandsDictionary[t[3]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1
    elif t[1] == 'n':
        operandsDictionary[operationIndex] = NOT(operandsDictionary[t[2]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1
    elif t[2] == 'a':
        operandsDictionary[operationIndex] = AND(operandsDictionary[t[1]], operandsDictionary[t[3]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1
    elif t[2] == 'o':
        operandsDictionary[operationIndex] = OR(operandsDictionary[t[1]], operandsDictionary[t[3]])
        t[0] = operationIndex
        operationIndex = operationIndex + 1

def p_expression_parenthesis(t):
    '''expression : LEFTPARENTHESIS expression RIGHTPARENTHESIS'''
    global operationIndex

    operandsDictionary[operationIndex] = operandsDictionary[t[2]]
    t[0] = operationIndex
    operationIndex = operationIndex + 1

def p_expression(p):
    '''expression : OPERAND'''

    p[0] = p[1]


import api.TruthTable.ply.ply.yacc as yacc
parser = yacc.yacc()



def solveTable(newData):
    global data
    global operandsDictionary
    data = newData
    operandsDictionary = startLexicalAnalysis(data)

    parser.parse(data)
    return str(operandsDictionary[operationIndex-1])



