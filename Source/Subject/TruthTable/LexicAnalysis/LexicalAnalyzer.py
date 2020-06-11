import Source.PLY.ply.lex as lex
from Source.ErrorHandling.ErrorHandler import *

tokens = [
'ATOMIC',
'LEFTPARENTHESIS',
'RIGHTPARENTHESIS',
'OR',
'AND',
'IMPLY',
'DOUBLEIMPLY',
'EXCLUSIVEOR',
'NEGATE'
]



t_ignore = ' \t'
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_OR = r'\∨'
t_AND = r'\∧'
t_IMPLY = r'\→'
t_DOUBLEIMPLY = r'\↔'
t_EXCLUSIVEOR = r'\#'
t_NEGATE = r'\¬'


def t_ATOMIC(t):
    r'[A-Z]'
    return t

def t_error(t):
    logError("Se ha introducido el caracter ilegal '%s' " % t.value[0])
    t.lexer.skip(1)

def startLexicalAnalysis(data):
    lexer = lex.lex()
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
    return lexer


