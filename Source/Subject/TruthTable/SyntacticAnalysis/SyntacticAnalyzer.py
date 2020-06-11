import Source.PLY.ply.yacc as yacc
from Source.Subject.TruthTable.DataStructures.AbstractSyntaxTree import *
from Source.Subject.TruthTable.LexicAnalysis.LexicalAnalyzer import *

treeHead = "MainStructure"
tokenList = []
tokenList.append(NodeAST(None,None,None,treeHead))


def p_mainStructure(p):
    '''
    mainStructure : molecular
    '''


def p_operator(p):
    '''
    operator : OR
    operator : AND
    operator : IMPLY
    operator : DOUBLEIMPLY
    operator : EXCLUSIVEOR
    '''

    tokenList.append(NodeAST(None,p[1]))


def p_molecular(p):
    '''
    molecular : lparenthesis molecular rparenthesis
    molecular : lparenthesis molecular operator molecular rparenthesis
    molecular : lparenthesis molecular operator atomic rparenthesis
    molecular : lparenthesis atomic operator atomic rparenthesis
    molecular : molecular operator molecular
    molecular : molecular operator atomic
    molecular : atomic operator atomic
    molecular : atomic
    '''


def p_atomic(p):
    '''
    atomic : ATOMIC
    '''

    tokenList.append(NodeAST(p[1]))

def p_lparenthesis(p):
    '''
    lparenthesis : LEFTPARENTHESIS
    '''
    tokenList.append(NodeAST(None, None, p[1]))

def p_rparenthesis(p):
    '''
    rparenthesis : RIGHTPARENTHESIS
    '''
    tokenList.append(NodeAST(None, None, p[1]))


def startSyntacticAnalysis(lexer):

    parser = yacc.yacc()
    result = parser.parse(lexer=lexer)
    abstractSyntaxTree = AbstractSyntaxTree(NodeAST(None,None,None,treeHead))
    abstractSyntaxTree.graphicRepresentation(tokenList)
    abstractSyntaxTree.parseTree(tokenList)