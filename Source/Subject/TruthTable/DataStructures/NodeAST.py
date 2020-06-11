class NodeAST:
    def __init__(self,atomic=None,operator=None,parenthesis=None,mainNodeName=None):
        self.atomic = atomic
        self.operator = operator
        self.mainNodeName = mainNodeName
        self.parenthesis = parenthesis