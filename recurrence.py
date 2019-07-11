import logic as lo
import aodag as dag
import itertools

#
#
"""
satisfied if all consequents in rule are among nodes
"""
def satisfied(rule, nodes):
    nodesArgs = [node.arg for node in nodes]
    sat = True
    for n in rule.conse:
        if n not in nodesArgs:
            sat = False
    return sat

def backchain(rollingNodes, rule):
    usedNodes = []
    bP = []
    if satisfied(rule, rollingNodes):
        usedNodes += [node for node in rollingNodes if node.arg in rule.conse]
        bP += rule.ante
    return (bP, usedNodes)

def indexUpdate(index, rollingNodes):
    for o in rollingNodes:
        if lo.predPattern(o.arg) not in index.keys():
            index[lo.predPattern(o.arg)] = o
        else:
            index[lo.predPattern(o.arg)].append(o)
    return index

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

f = open("test1.txt", "r")
obsv = f.readline().strip()
obsvNodes = obsv.split(', ')
obsvNodes = [x.split(' ') for x in obsvNodes]
# convert obsv to Nodes
rollingNodes = []
for i in obsvNodes:
    rollingNodes.append(dag.Node(lo.Form(i[0], i[1:])))
KB = []
index = dict()
index = indexUpdate(index, rollingNodes)

for line in f:
    implication = line.strip().split('. ')
    antecedents = implication[0].split(', ')
    consequents = implication[1].split(', ')
    antecedentsArgs, consequentsArgs = parse(antecedents), parse(consequents)
    KB.append(lo.Rule(len(KB)+1, antecedentsArgs, consequentsArgs))

# Erase useless rules from KB
# KB filter  consequents in rolling nodes
# KB = [rule if any i in rule.conse in x.arg for x in rollingNodes for rule in KB]

"""
Assume KB filtered
"""
Refd = dict()
for o in rollingNodes:
    Refd[o] = True

# # Convert KB to a KB of Axioms
d = 1
while(d>0):
    # Backchaining
    for axiom in KB:
        # Axiom is of the form HornClause(args, args)
        # rollingNodes is the list of nodes already explored
        (bP, usedNodes) = backchain(rollingNodes, axiom) #Parse root?
        if bP:
            for used in usedNodes:
#                 #This may not work, check how to index
                newAxiom = dag.Axiom(axiom.no, used)
                # newAxiom.child.append(used)
            for backchained in bP:
                newBackchained = dag.Node(backchained, newAxiom)


        """
        Don't exactly understand the purpose of this; cant rememberlol
        """
        # for a in axiom.conse:
        #     if a not in Refd.keys():
        #         x = dag.Ref(a, newAxiom)
        #         Refd[a] = True
#     """
#     Unification
#     Need to store information about predicates previously added to the KB
#     Need a way of quickly identifying predicate patterns same to the one here
#     So:
#     bP is backchained predicates
#     we know that when we do unification all we need to do is compare those from bP
#     against those that were already come up with earlier.
#     So perhaps a dictionary for predPatterns that is updated at the end of each loop
#     would be useful for this. (bubble sort)
#     then for all predicates in bP we unify them with all their precedents in the dict.
#
#     """
    for x in bP:
        print(x)
        print(index)
        # For each backchained literal, try to unify it with whatever you can
        xPttn = lo.predPattern(x)
        if xPttn in index.keys():
            for y in index[xPttn]:
                # Pair is x, y, they're Nodes
                unified = dag.Uni((x, y))
                equal = dag.LitUni((x, y))
                index[xPttn].append(y)
#
    d -= 1
