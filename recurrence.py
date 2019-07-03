import logic as lo
import itertools

#
#
#
# def backchain:
#
#
#
# def unify:
#
#
#
# def listHypotheses:
#


def parse(varList):
    args = [varList[i].split(' ') for i in range(len(varList))]
    args = [lo.Form(args[i][0], args[i][1:]) for i in range(len(args))]
    return args
rules = []
"""
Define Tree structure
the structure has the following features:
- each literal node is either an observable or a parent of exactly one Axiom
OR[x][0] -> value of node
OR[x][1] -> axiom; 0 if observable
AND[x][0] -> value of node (no of axiom, 0 if unifying, -1 if ref)
AND[x][1] -> list of children if axiom; list of unified predicates if unifying;
ref predicate if ref;

BS

I need the following types of nodes:
- literal node (name, child axiom number)
- axiom node (number, children)
- unification node (predicate pattern, child 1, child 2)
- literal unification node (argument 1, argument 2, child unification)
- referential node (predicate, child axiom)
- numbU node (number of unifications, child axiom)

Example graph [taken from PDF] would look like this:

Node(q(x,y), null, True)
Node(r(x), null, True)
Axiom(1, [q(x,y)], tV)
Axiom(2, [q(x,y), r(x)], tV)
Ref(r(x), [2])
Ref(q(x,y), [1,2])
Node(p(y), 1, tV)
Node(p(x), 2, tV)
Node(s(z), 2, tV)
NumbU(null, 1)
NumbU(null, 2)
Uni(p, [p(x), p(y)], tV)
LitUni((x,y), p, tV)

Note: Ref, NumbU in themselves are already TFNodes. Thus only need to account for the rest.

class Node(self, arg, child=null):
    self.arg = arg # Form(define the literal node)
    self.child = child
    self.holds = True if self.child == null else null
    self.id = self.arg

class Axiom(self, no, child):
    self.no = no
    self.child = child
    self.holds = null
    self.id = self.no
class Ref(self, arg, child):
    self.arg = arg
    self.child = child
    self.id = self.arg
    define a holds function
    holds(self, obsv) = True if self.arg in obsv else False

class NumbU(self, child):
    self.value = null
    self.child = child
    self.id = self.child
    setValue(self, value):
        self.value = value


class Uni(self, child):
    self.symbol = child[0].symbol
    self.holds = null
    self.id = self.symbol

class LitUni(self, child):
    self.arg = (child.child[0].arg, child.child[1].arg)
    self.child = child
    self.id = self.arg
A node is an archetypical structure to which I can then assign T/F value.
In other words, perhaps the actual graph will be defined in the following way:
Node(truthValue, node, children)
children to be extracted from node upon definition.

- each axiom can be the child and parent of many literal nodes
- each unification node connects to exactly two literal nodes of the same pred pattern

"""
f = open("test1.txt", "r")
obsv = f.readline().strip()
# Add observational nodes to the tree
KB = []
for line in f:
    implication = line.strip().split('. ')
    print(implication)
    antecedents = implication[0].split(', ')
    consequents = implication[1].split(', ')
    antecedentsArgs, consequentsArgs = parse(antecedents), parse(consequents)
    KB.append(lo.HornClause(0, consequentsArgs, antecedentsArgs))
    print(antecedentsArgs, consequentsArgs)
# Erase useless rules from KB
# Create a Refd[v] list of all predicates
print(KB)
d = 5
while(d>0):
    # Backchaining
    for axiom in KB:
        # Axiom is of the form HornClause(args, args)
        (bP, uP) = backchain(Tree, axiom)
        if bP:
            for used in uP:
                Tree[axiom].append(used)
            for backchained in bP:
                # Do it differently; you know that only one axiom is applied
                # to each predicate - exploit that
                Tree[backchained].append(axiom)
        for a in axiom.antecedents:
            if !Refd[a]:
                x = lo.Ref(a, True if a in obsv else False)
                Tree[x].append(axiom)

    # Unification
    # Need to store information about predicates previously added to the KB
    # Need a way of quickly identifying predicate patterns same to the one here
    for ...:
        # Pair is x, y
        unified = lo.Uni(x.symbol)
        Tree[unified].append(x)
        Tree[unified].append(y)
        equal = lo.Equal(x, y)
        Tree[equal].append(unified)
        Tree[x]

    d -= 1
