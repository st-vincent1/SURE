import aodag as dag
G = {1:[4], 2:[3], 3:[], 4:[2]}

degreeTable = dag.degree(G,1)
print(degreeTable)
print(dag.topSort(G, degreeTable))
