import itertools

def traversal(G, hyps):
    




# graph = {'e': [''],
#          'b': ['e'],
#          'c': ['e'],
#          'a': ['b', 'c'],
#          'd': ['c'],
#          's1': ['a'],
#          's2': ['d'],
#          's1=s2': ['s1','s2']}

graph = {'e': ['b', 'c'],
         'b': ['a'],
         'c': ['a', 'd'],
         'a': ['s1'],
         'd': ['s2'],
         's1': ['s1=s2'],
         's2': ['s1=s2'],
         's1=s2': []}
print(graph)
