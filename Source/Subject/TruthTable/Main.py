from Source.Subject.TruthTable.LexicAnalysis.LexicalAnalyzer import *
from Source.Subject.TruthTable.SyntacticAnalysis.SyntacticAnalyzer import *
from Source.ErrorHandling.ErrorHandler import *

import Source.PLY.ply.lex as lex
import Source.PLY.ply.yacc as yacc

def Main():

    data1 = '(A#E)#((P#O)#(P#(T#R)))'
    data = '(((A)#N)#J)#(B)#(I)'
    lexer = startLexicalAnalysis(data)

    lexer.input(data)

    if not theresErrors():
        startSyntacticAnalysis(lexer)
    else:
        print(readErrorLog())


wipeErrorLog()
Main()