import logic as lo
import aodag as dag
import itertools
import pprint as pp

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


def parse(varList):
    args = [varList[i].split(' ') for i in range(len(varList))]
    args = [lo.Form(args[i][0], args[i][1:]) for i in range(len(args))]
    return args




################### MAIN
f = open("test1.txt", "r")
obsv = f.readline().strip()
obsvNodes = obsv.split(', ')
obsvNodes = [x.split(' ') for x in obsvNodes]
# convert obsv to Nodes
rollingNodes = []
for i in obsvNodes:
    rollingNodes.append(dag.Node(lo.Form(i[0], i[1:]), 'lit'))
# print(rollingNodes)
KB = []
G = dag.initGraph(rollingNodes)
# index stores lists of nodes that satisfy a certain predicate pattern
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
# Refd[o] = True <=> o is an observable; do I need this tho
Refd = dict()
for o in rollingNodes:
    Refd[o] = False

# # Convert KB to a KB of Axioms
d = 1
while(d>0):
    seriesNodes = []
    # Backchaining
    for axiom in KB:
        newAxiom = dag.Node(axiom.no, 'ax')
        # print(axiom)
        # Axiom is of the form HornClause(args, args)
        # rollingNodes is the list of Nodes already explored
        # bP is a list of backchained PREDICATES
        # Need to: create nodes for predicates, THEN connect bp-axiom-up
        (bP, usedNodes) = backchain(rollingNodes, axiom) #Parse root?
        if bP:
            #Something was bchained -> create axiom node
            dag.addChildren(G, newAxiom, [usedNodes])

            for backchained in bP:
                back = dag.Node(backchained, 'lit')
                pp = lo.predPattern(backchained)
                index[pp] = [back] if pp not in index.keys() else index[pp] + [back]
                dag.addChildren(G, back, [newAxiom])
                seriesNodes.append(back)
        """
        Putting Refs in the graph
        """
        for a in axiom.conse:
            if a not in Refd.keys():
                Refd[a] = dag.Node(a, 'ref')
            dag.addChildren(G, Refd[a], [newAxiom])
    rollingNodes += seriesNodes
    """
    Unification
    Don't have num nodes yet
    

    """
    print(G)
    # pp.pprint(G)
    print("Begin unification")
    print(seriesNodes)
    for x in seriesNodes:
        # x is a node now
        print(x)
        print("index:")
        print(index)
        # For each backchained literal, try to unify it with whatever you can
        xPttn = lo.predPattern(x.arg)
        # print(xPttn)
        if xPttn in index.keys():
            for y in index[xPttn]:
                if y != x:
                    print(x,y)
                # Pair is x, y, they're Nodes
                    unified = dag.Node((x.arg, y.arg), 'uni')
                    literals = dag.Node((x.arg, y.arg), 'eq')
                    dag.addChildren(G, unified, [x,y])
                    dag.addChildren(G, literals, [unified])
                    # index[xPttn].append(y)
    d -= 1
for x in G.keys():
    print(str(x) + " --> " + str(G[x]))
