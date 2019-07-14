import aodag as dag
G = {1:[4], 2:[3], 3:[], 4:[2]}

order = []
vis = dict()
degree = dict()
for i in G.keys():
    vis[i] = False
    degree[i] = 0
for i in G:
    if not vis[i]:
        vis[i] = True
        degree = dag.dfsDegree(G, i, degree, vis)
print(degree)
#Topsort
for i in G.keys():
    vis[i] = False
for i in degree.keys():
    if degree[i] == 0 and not vis[i]:
        vis[i] = True
        dag.dfsTop(G, i, order, degree, vis)
print(order)

for i in G.keys():
    vis[i] = False

combos = [[]]
for i in order:
    if not vis[i]:
        vis[i] = True
        combos = dag.traversal(G, i, combos, vis)
