from Source.Subject.TruthTable.DataStructures.NodeAST import *

class AbstractSyntaxTree:
    def __init__(self,node,children=[],level=1):
        self.children=children
        self.level=level
        self.node=node

    def addNode(self,node):
        self.children.append(AbstractSyntaxTree(node))

    def graphicRepresentation(self,tokenList):
        for token in tokenList:
            if token.mainNodeName:
                print(token.mainNodeName)
            if token.atomic:
                print(token.atomic)
            if token.operator:
                print(token.operator)
            if token.parenthesis:
                print(token.parenthesis)


    def parseTree(self,tokenList):
        priorityLevel = 1
        for token in tokenList:
            if token.parenthesis:
                if token.parenthesis == "(":
                    priorityLevel+=1
                if token.parenthesis == ")":
                    priorityLevel-=1
            else:
                if token.atomic: print("El token analizado tiene una prioridad de " +
                                       str(priorityLevel) + " " + str(token.atomic))
                if token.operator: print("El token analizado tiene una prioridad de " +
                                       str(priorityLevel) + " " +str(token.operator))







