import api.TruthTable.ply.ply.lex as lex

tokens = ['LEFTPARENTHESIS','RIGHTPARENTHESIS','OPERAND','NOT','AND','OR','XOR','NAND','NOR','XNOR']

t_ignore = ' \t'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_OPERAND = r'[A-Z]'
t_NOT = r'n'
t_AND = r'a'
t_OR = r'o'
t_XOR = r'xo'
t_NAND = r'na'
t_NOR = r'no'
t_XNOR = r'xno'

def t_error(t):
    print("There is an error with character %s" %t.value[0])

lexer = lex.lex()

def createLogicValue(index,operandsAmount):
    logicValue = []
    currentLogicValue = False
    for i in range(0,2**(index)):
        for j in range(0,2**(operandsAmount-index)):
            logicValue.append(currentLogicValue)
        currentLogicValue = not currentLogicValue
    return logicValue

def assignLogicValues(tokenList):
    operandsDictionary = {}
    for i in range(0,len(tokenList)):
        operandsDictionary[tokenList[i]] = createLogicValue((i+1),len(tokenList))
    return operandsDictionary

def startLexicalAnalysis(input):
    lexicalAnalyzer = lex.lex()
    lexicalAnalyzer.input(input)

    tokenList = []
    operands = []
    while True:
        newToken = lexicalAnalyzer.token()
        if not newToken:
            break

        tokenList.append((newToken.value,newToken.type))

        if(newToken.type == 'OPERAND'):
            operands.append(newToken.value)

    operandsDictionary = assignLogicValues(operands)

    return operandsDictionary