import tkinter as tk
import recurrence as r
KB = []
obsv = []
rules = []

def abduce(obs, rul, con, hyps):
    d = 5
    obsv = obs.get("1.0", "end-1c").split("\n")[:-1]
    rules = rul.get("1.0", "end-1c").split("\n")[:-1]
    print(obsv)
    print(rules)
    KB, Litd, rollingNodes, G, index, obsvNodes = r.parseInput(obsv, rules)
    """
    Assumption: KB is filtered so that each rule is going to be useful for backchaining.
    Not necessary, though speeds up inference. Will do if time allows, it can be done with just input.
    """
    # This goes in the work in progress field
    con.insert(tk.END, r.printKB(KB))
    Refd, Axd, Numd, uniPair, uniPredicate = r.backchainAndUnify(KB, rollingNodes, G, Litd, index, obsvNodes, d)
    # Work in progress field
    con.insert(tk.END, r.printGraph(G))
    # Calculate topological order for nodes
    order = r.topSort(G)
    """
    Now on to creating hypotheses
    each node is given a number depending on its order from topsort
    order is the topological order of nodes
    orderIndex is a dictionary node : number
    par is a reverse order graph computed on those numbers
    combo is a list of all possible combinations of truth/false assignments to nodes in graph
    """
    # Compute par, children and orderIndex
    par, children, orderIndex = r.computePar(order, G)
    # Compute combo
    combo = r.computeCombo(order, par, children, orderIndex, G)
    # Create a list of hypotheses
    hyp = r.computeHyp(combo, order, par)
    # Print out all hypotheses
    hyps.insert(tk.END, r.printHyp(hyp))
    return

def fill(stro, strr, obs, rul):
    o = open(stro, "r")
    r = open(strr, "r")
    for line in o:
        obs.insert(tk.END, line)
    for line in r:
        rul.insert(tk.END, line)
    return
def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries

def makeLeft(root, con, hyp):
    # Obsv
    lab = tk.Label(root,  font = ("Times", 16), text="Observables: ", anchor='w')
    obs = tk.Text(root, width = 40, height = 10, bg = "white")
    #insert
    lab.pack(side = tk.TOP,
             fill = tk.BOTH,
             padx = 10)
    obs.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    #Rules
    lab = tk.Label(root, font = ("Times", 16), text="Rules: ", anchor='w')
    rul = tk.Text(root, width = 40, height = 10, bg = "white")
    run = tk.Button(root, width = 10, height = 2, text = "Run abduction!", command = lambda: abduce(obs, rul, con, hyp))
    lab.pack(side = tk.TOP,
             fill = tk.BOTH,
             padx = 10)
    rul.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    btnPanel = tk.Frame(root)
    tk.Button(btnPanel, text = f'Ex. 1', command = lambda: fill(f'test1o.txt', f'test1r.txt', obs, rul)).pack(side = tk.LEFT)
    tk.Button(btnPanel, text = f'Ex. 2', command = lambda: fill(f'test2o.txt', f'test2r.txt', obs, rul)).pack(side = tk.LEFT)
    tk.Button(btnPanel, text = f'Ex. 3', command = lambda: fill(f'test3o.txt', f'test3r.txt', obs, rul)).pack(side = tk.LEFT)
    tk.Button(btnPanel, text = f'Ex. 4', command = lambda: fill(f'test4o.txt', f'test4r.txt', obs, rul)).pack(side = tk.LEFT)
    tk.Button(btnPanel, text = f'Ex. 5', command = lambda: fill(f'test5o.txt', f'test5r.txt', obs, rul)).pack(side = tk.LEFT)
    tk.Button(btnPanel, text = f'Ex. 6', command = lambda: fill(f'test6o.txt', f'test6r.txt', obs, rul)).pack(side = tk.LEFT)
    btnPanel.pack(side = tk.TOP)
    # add examples to fill the blanks
    run.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    return

def makeMiddle(root):
    lab = tk.Label(root, font = ("Times", 16), text="Works: ", anchor='w')
    inp = tk.Text(root, width = 60, height = 30, bg = "light gray")
    lab.pack(side = tk.TOP,
            fill = tk.BOTH,
            padx = 10)
    inp.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    return inp
def makeRight(root):
    lab = tk.Label(root, font = ("Times", 16), text="Hypotheses: ", anchor='w')
    out = tk.Text(root, width = 60, height = 28, bg = "white")
    btn = tk.Button(root, text='Quit', command=root.quit)
    lab.pack(side = tk.TOP,
             fill = tk.BOTH,
             padx = 10)
    out.pack(side = tk.TOP,
             fill = tk.Y,
             padx = 5,
             pady = 5)
    btn.pack(side=tk.RIGHT,
             padx=10,
             pady=5)
    return out
if __name__ == '__main__':
    root = tk.Tk()

    titleFrame = tk.Frame(root)
    tk.Label(titleFrame, font = ("Times", 24), text = "Abduction engine", anchor = 'n').pack(side = tk.LEFT, fill = tk.X)
    titleFrame.grid(column = 0, row = 0, columnspan = 3)

    # b2 = tk.Button(root, text='Monthly Payment',
    #        command=(lambda e=ents: monthly_payment(e)))
    # b2.grid(column = 0, row = 1, padx=5, pady=5)
    middleFrame = tk.Frame(root)
    console = makeMiddle(middleFrame)

    rightFrame = tk.Frame(root)
    hyps = makeRight(rightFrame)

    leftFrame = tk.Frame(root)
    makeLeft(leftFrame, console, hyps)

    middleFrame.grid(column = 1, row = 1)
    rightFrame.grid(column = 2, row = 1)
    leftFrame.grid(column = 0, row = 1)

    root.mainloop()
