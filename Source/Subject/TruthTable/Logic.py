def negateOperator(P):
    return not P

def orOperator(P,Q):
    if P or Q:
        return True
    return False

def andOperator(P,Q):
    if P and Q:
        return True
    return False

def orExclusiveOperator(P,Q):
    if (P and Q) or (not P and not Q):
        return False
    return True

def implyOperator(P,Q):
    if P and not Q:
        return False
    return True

def doubleImplyOperator(P,Q):
    if (P and Q) or (not P and not Q):
        return True
    return False

