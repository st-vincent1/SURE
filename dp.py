import itertools
expl = dict()
# listOfExpl = []

# def explain(node, G, dp):
#     listOfExpl = []
#     if G[node] == []:
#         return node
#     for x in G[node]:
#         listOfExpl += [explain(x, G)]
#     expl[node] = list(itertools.product(*listOfExpl))
#     return expl[node]
# def traversal(node, G, hyps):
#     if G[node] == []:
#         return hyps
#     # listOfExpl = [expl[i] for i in G[node]]
#     # expl[node] = list(itertools.product(*listOfExpl))
#     hyps += expl[node]
#     return expl[node]
def explain(node, G, revG, dp):
    listOfExpl = []
    print("I'm in " + node)
    #set current dp as product of dp's of children + myself
    if revG[node] == []:
        dp[node] = node
    else:
        for x in revG[node]:
            listOfExpl += dp[x]
        print(listOfExpl)
        # print("pre")
        expl = list(list(tup) for tup in itertools.product(*listOfExpl))
        # print(expl)
        # print(listOfExpl)
        expl.append(node)
        dp[node] = expl
    for x in G[node]:
        explain(x, G, revG, dp)
    return

graph = {'e': [],
         'b': ['e'],
         'c': ['e'],
         'a': ['b', 'c'],
         'd': ['c'],
         's': ['a'],
         'f': ['d'],
         'u': ['s','f']}

revGraph = {'e': ['b', 'c'],
         'b': ['a'],
         'c': ['a', 'd'],
         'a': ['s'],
         'd': ['f'],
         's': ['u'],
         'f': ['u'],
         'u': []}

dp = dict.fromkeys(graph.keys(),[])
for key in dp.keys():
    dp[key] = [key]
# print(graph)
# print(traversal('e', graph, []))
x = explain('u', graph, revGraph, dp)
# print(dp)
