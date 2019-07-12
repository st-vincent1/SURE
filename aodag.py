import logic as lo
"""
Idea: One structure for all
Node - with argument and and/or indicator
Vertex - takes Node and children. G is a structure in which vertices are keys and values are children
a Vertex can either hold or not hold - this is for further calculations

graph needs to have children easily accessed
- graph[x] = children
- graph[x].children = children

Each node has the following specifics:
- has a predicate or axiom or pattern or equality of variables
- type
- has and/or (pre-determined by type)
- value true/false (pre-determined in some cases, will be added later tho)
create a graph structure which operates on Node (one class), backchain and unify on nodes,
do basically everything on nodes, not just when you need to add to graph. Make sure that nodes are always passed
when you call functions, not their arguments (predicates etc)
yull be ok

finish this today tho

"""
class Node:
    def __init__(self, arg, family):
        self.family = family
        self.arg = arg
        self.andor = 'AND' if self.family in ['ref','uni','eq','ax','num'] else 'OR'
        self.num = 0 if self.family == 'num' else None
        self.symbol = arg[0].symbol if self.family == 'uni' else None
        self.eq = ()
        self.eqArgs = 0 #Make this take arguments of lituni
        self.truth = None
    def __repr__(self):
        return "[" + self.family + "] " + repr(self.arg)
    def holds(self, obsv):
        return True if self.arg in obsv and self.family == 'ref' else False

def initGraph(nodes):
    G = dict()
    for node in nodes:
        G[node] = []
    return G
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
