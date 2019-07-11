import logic as lo
"""
Idea: One structure for all
Node - with argument and and/or indicator
Vertex - takes Node and children. G is a structure in which vertices are keys and values are children
a Vertex can either hold or not hold - this is for further calculations

"""
class Vertex:
    def __init__(self, value, child=None):
        self.value = value # Node, any class
        self.child = child
        self.holds = None
    def __repr__(self):
        return repr(self.value) + " ---> " + repr(self.child)

class Node:
    def __init__(self, arg, family):
        self.family = family
        self.arg = arg
        self.andor = 'AND' if self.family in ['ref','uni','eq','ax','num'] else 'OR'
        self.num = 0 if self.family == 'num' else None
        self.eqArgs = 0 #Make this take arguments of lituni
    def __repr__(self):
        return "[" + self.andor + "] " + repr(self.arg)
    def holds(self, obsv):
        return True if self.arg in obsv and self.family == 'ref' else False

def addChildren(graph, node, children):
    if node not in graph.keys():
        graph[node] = []
    graph[node] += children

# class Literal:
#     def __init__(self, arg):
#         self.arg = arg # Form(define the literal node)
#     def __repr__(self):
#         return repr(self.arg) + " ---> " + repr(self.child)
#
# class Axiom:
#     def __init__(self, no):
#         self.no = no
#     def __repr__(self):
#         return "(" + str(self.no) + ") ---> " + repr(self.child)
#
# class Ref:
#     def __init__(self, arg):
#         self.arg = arg
#     # define a holds function
#     def holds(self, obsv):
#         return True if self.arg in obsv else False
#
# class Uni:
#     def __init__(self, child):
#         self.symbol = child[0].symbol
#
# class LitUni:
#     def __init__(self, child):
#         self.arg = (child.child[0].arg, child.child[1].arg)
#         self.child = child
#         self.id = self.arg
#         self.holds = None

# def backchain(nodes, axiom)
