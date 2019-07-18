import logic as lo
import aodag as dag
import itertools
import pprint as pp
import copy
"""
Satisfied if all consequents in rule are among nodes
"""
def satisfied(rule, nodes):
    nodesArgs = [node.arg for node in nodes]
    sat = True
    for n in rule.conse:
        if n not in nodesArgs:
            sat = False
    return sat

"""
Pattern matching
"""
def backchain(rollingNodes, rule):
    print(rule)
    print(rollingNodes)
    usedNodes = []
    bP = []
    if satisfied(rule, rollingNodes):
        usedNodes += [node for node in rollingNodes if node.arg in rule.conse]
        bP += rule.ante
    print(usedNodes)
    return (bP, usedNodes)

def indexUpdate(index, rollingNodes):
    for o in rollingNodes:
        if lo.predPattern(o.arg) not in index.keys():
            index[lo.predPattern(o.arg)] = [o]
        else:
            index[lo.predPattern(o.arg)].append(o)
    return index

def parse(varList):
    args = [varList[i].split(' ') for i in range(len(varList))]
    args = [lo.Form(args[i][0], args[i][1:]) for i in range(len(args))]
    return args

################### MAIN
Litd = dict()
Refd = dict()
Axd = dict()
Numd = dict()
uniPair = dict()
uniPredicate = dict()
f = open("test1.txt", "r")
obsv = f.readline().strip()
obsvNodes = obsv.split(', ')
obsvNodes = [x.split(' ') for x in obsvNodes]
# convert obsv to Nodes
rollingNodes = []
for i in obsvNodes:
    a = lo.Form(i[0], i[1:])
    aNode = dag.Node(a, 'lit', True)
    Litd[a] = aNode
    rollingNodes.append(aNode)

obsvNodes = copy.deepcopy(rollingNodes)
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
# KB filter consequents in rolling nodes
# KB = [rule if any i in rule.conse in x.arg for x in rollingNodes for rule in KB]

"""
Assume KB filtered
"""
# Convert KB to a KB of Axioms
d = 5
while(d>0):
    seriesNodes = []
    # Backchaining
    for axiom in KB:
        if axiom.no not in Axd.keys():
            Axd[axiom.no] = dag.Node(axiom.no, 'ax')
            Numd[axiom.no] = dag.Node(axiom.no, 'num')
            dag.addChildren(G, Numd[axiom.no], [Axd[axiom.no]])
        # print(axiom)
        # Axiom is of the form HornClause(args, args)
        # rollingNodes is the list of Nodes already explored
        # bP is a list of backchained PREDICATES
        # Need to: create nodes for predicates, THEN connect bp-axiom-up
        (bP, usedNodes) = backchain(rollingNodes, axiom) #Parse root?
        if bP:
            #Something was bchained -> create axiom node
            dag.addChildren(G, Axd[axiom.no], usedNodes)
            for b in bP:
                if b not in Litd.keys():
                    Litd[b] = dag.Node(b, 'lit')
                pp = lo.predPattern(b)
                index[pp] = [Litd[b]] if pp not in index.keys() else index[pp] + [Litd[b]]
                dag.addChildren(G, Litd[b], [Axd[axiom.no]])
                seriesNodes.append(Litd[b])
        """
        Putting Refs in the graph
        """
        for a in axiom.conse:
            if a not in Refd.keys():
                Refd[a] = dag.Node(a, 'ref', False, True if Litd[a] in obsvNodes else False)
            dag.addChildren(G, Refd[a], [Axd[axiom.no]])
    rollingNodes += seriesNodes

    for x in seriesNodes:
        # For each backchained literal, try to unify it with whatever you can
        xPttn = lo.predPattern(x.arg) # can only unify literals of same pattern
        if xPttn in index.keys(): # if not in index then there's nothing to unify
            for y in index[xPttn]: # try to unify against every literal in index
                # Now I'm at the pair. want to know if these are unifiable [also no if theta empty]
                theta = lo.unifyTerms(x.arg,y.arg)
                if not theta:
                    break # to avoid (x=y,y=x)
                for pair in theta.items():
                    if pair not in uniPair.keys(): # if no x=y node in graph
                        uniPair[pair] = dag.Node(pair, 'eq') #create node
                    if xPttn not in uniPredicate.keys():
                        uniPredicate[xPttn] = dag.Node(xPttn, 'uni')
                        dag.addChildren(G, uniPredicate[xPttn], [x,y])
                        if not x.obsv:
                            dag.addChildren(G, uniPredicate[xPttn], [Numd[G[x][0].arg]])
                        if not y.obsv:
                            dag.addChildren(G, uniPredicate[xPttn], [Numd[G[y][0].arg]])
                    if uniPair[pair] not in G.keys() or G[uniPair[pair]] != uniPredicate[xPttn]: # if the child of unif
                        dag.addChildren(G, uniPair[pair], [uniPredicate[xPttn]])
    d -= 1
for x in G.keys():
    print(str(x) + " --> " + str(G[x]))
#make a loop which goes over nodes and sttarts degree on those unvisited

# Calculate topological order for nodes
# Degree is a list of topologically sorted nodes
order = []
vis = dict()
degree = dict()
for i in G.keys():
    vis[i] = False if i.family not in ['num', 'ref'] else True
    degree[i] = 0
for i in G:
    if not vis[i]:
        vis[i] = True
        degree = dag.dfsDegree(G, i, degree, vis)
# print(degree)
#Topsort
for i in G.keys():
    vis[i] = False if i.family not in ['num', 'ref'] else True
for i in degree.keys():
    if degree[i] == 0 and not vis[i]:
        vis[i] = True
        dag.dfsTop(G, i, order, degree, vis)
# print(order)
"""
Now on to creating hypotheses
each node is given a number depending on its order from topsort
order is the topological order of nodes
orderIndex is a dictionary node : number
par is a reverse order graph computed on those numbers
combo is a list of all possible combinations of truth/false assignments to nodes in graph
"""

par = [x[:] for x in [[]]*(len(order))]
# Compute orderIndex
orderIndex = dict()
for i in range(len(order)):
    orderIndex[order[i]] = i

# Compute par
for node in order:
    for child in G[node]:
        if child.family not in ['ref', 'num']:
            par[orderIndex[child]].append(orderIndex[node])

# Compute combo
combo = [[]]
for i in order:
    combo = dag.traversal(G, i, combo, par, orderIndex)
# Delete useless combinations (those which have false observables)
obsvNodes = [orderIndex[i] for i in order if i.obsv == True]
combo = dag.checkObsv(combo, obsvNodes)
combo = dag.usefulCombo(combo)
# Create a list of hypotheses
hypo = [x[:] for x in [[]]*(len(combo))]

# for c in combo:
#     print("Good Combooo:")
#     for c1 in range(len(c)):
#         print(order[c1], c[c1])

for j in range(len(combo)):
    for i in range(len(combo[j])):
        if combo[j][i] == True:
            noTrueParents = False
            for p in par[i]:
                if combo[j][p] == True and order[p].family != 'uni':
                    noTrueParents = True
                    break
            if noTrueParents == False:
                hypo[j].append(order[i])
# Check that hypotheses containing useless variables are deleted
# Print out all hypotheses
for i in hypo:
    print(i)

# Delete useless hypotheses
#update ref and num
# Update NumbU
# From now on work on G.. or incorporate num and ref into the previous representation
