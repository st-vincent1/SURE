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
    def __init__(self, arg, family, obsv=False, refObsv=False):
        self.family = family
        self.arg = arg
        self.andor = 'AND' if self.family in ['ref','uni','eq','ax','num'] else 'OR'
        self.num = 0 if self.family == 'num' else None
        self.symbol = arg.symbol if self.family == 'uni' else None
        self.eq = ()
        self.eqArgs = 0 #Make this take arguments of lituni
        self.truth = None
        self.obsv = obsv
        self.refObsv = refObsv
        self.trueParents = 0
        self.falseParents = 0
    def __repr__(self):
        return "<" + self.family + "> " + repr(self.arg)
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.arg == other.arg and self.family == other.family
    def __hash__(self):
        return hash((self.arg,self.family))



def initGraph(nodes):
    G = dict()
    for node in nodes:
        #Observational nodes are children of axiom 0
        G[node] = []
    return G
def addChildren(graph, node, children):
    if node not in graph.keys():
        graph[node] = []
    for c in children:
        if c not in graph[node]:
            graph[node].append(c)

def dfsDegree(graph, node, degreeTable, vis):
    if node.family == 'ref':
        print(node)
        print(node.refObsv)
    for i in graph[node]:
        degreeTable[i] += 1
        if not vis[i]:
            vis[i] = True
            dfsDegree(graph, i, degreeTable, vis)
    return degreeTable

def dfsTop(graph, node, order, degreeTable, vis):
    order.append(node)
    for i in graph[node]:
        degreeTable[i] -= 1
        if degreeTable[i] == 0 and not vis[i]:
            vis[i] = True
            dfsTop(graph, i, order, degreeTable, vis)

def analyseNode(graph, node, par):
    if node.obsv == True:
        return (True, False)
    if node.family == 'num':
        node.num = par[node][1]
        return (False, False)
    if par[node][1] == 0 and par[node][0] == 0:
        return (True, True)
    if node.andor == 'AND':
        if par[node][0] > 0:
            return (False, True)
        else:
            return (True, False)
    elif node.andor == 'OR':
        if par[node][1] > 0:
            return (True, False)
        else:
            return (True, True)
    else:
        print("Error: undefined node")
        return (False, False)

def traversal(graph, node, preCombo, par):
    (truth, falsity) = analyseNode(graph, node, par)
    newComboT = [combo + [(node, True)] for combo in preCombo]
    newComboF = [combo + [(node, False)] for combo in preCombo]
    preCombo = newComboT * truth + newComboF * falsity
    for j in range(len(preCombo)):
        for i in graph[node]:
            i.falseParents += falsity*1
            i.trueParents += truth*1
    return preCombo
"""
def traversal(graph):
    Sort nodes topologically
    For all nodes in beginTable:
        For all models:
            Analyse node -- returns True, False or True and False
            if should, Traverse(node=True)
            if should, Traverse(node=False)
                remember a traversal path when branching

    When you enter the last node (will be last in topological order),
    see what paths you have. Select only those where all observables are true,
    and then create hypotheses [by picking out those literals that have no true parents]

Remember to include number of unifications for the num nodes.
Now we have hypotheses and models. Can calculate the probability.
Research conditional probability tables!

"""
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
