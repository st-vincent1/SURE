import logic as lo

class Node:
    def __init__(self, arg, child=None):
        self.arg = arg # Form(define the literal node)
        self.child = child
        self.holds = True if self.child == None else None
        self.id = self.arg
    def __repr__(self):
        return repr(self.arg) + " ---> " + repr(self.child)

class Axiom:
    def __init__(self, no, child=None):
        self.no = no
        self.child = child
        self.holds = None
        self.id = self.no
    def __repr__(self):
        return "(" + str(self.no) + ") ---> " + repr(self.child)

class Ref:
    def __init__(self, arg, child):
        self.arg = arg
        self.child = child
        self.id = self.arg
    # define a holds function
    def holds(self, obsv):
        return True if self.arg in obsv else False

class NumbU:
    def __init__(self, child):
        self.value = None
        self.child = child
        self.id = self.child
    def setValue(self, value):
        self.value = value

class Uni:
    def __init__(self, child):
        self.symbol = child[0].symbol
        self.holds = None
        self.id = self.symbol

class LitUni:
    def __init__(self, child):
        self.arg = (child.child[0].arg, child.child[1].arg)
        self.child = child
        self.id = self.arg
        self.holds = None

# def backchain(nodes, axiom)
