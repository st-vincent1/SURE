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
f = open("test1.txt", "r")
obsv = f.readline().strip()
KB = []
for line in f:
    implication = line.strip().split('. ')
    print(implication)
    antecedents = implication[0].split(', ')
    consequents = implication[1].split(', ')
    antecedentsArgs, consequentsArgs = parse(antecedents), parse(consequents)
    KB.append(lo.HornClause(0, consequentsArgs, antecedentsArgs))
    print(antecedentsArgs, consequentsArgs)
print(KB)
d = 5
while(d>0):
    bP = backchain()

    d -= 1
