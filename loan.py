import tkinter as tk

fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')

def abduce():
    pass
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

def makeObsv(root):
    lab = tk.Label(root,  font = ("Times", 16), text="Observables: ", anchor='w')
    inp = tk.Text(root, width = 40, height = 10, bg = "white")
    lab.pack(side = tk.TOP,
             fill = tk.BOTH,
             padx = 10)
    inp.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    return inp

def makeRules(root):
    lab = tk.Label(root, font = ("Times", 16), text="Rules: ", anchor='w')
    inp = tk.Text(root, width = 40, height = 10, bg = "white")
    btn = tk.Button(root, width = 10, height = 2, text = "Run abduction!", command = abduce)
    lab.pack(side = tk.TOP,
             fill = tk.BOTH,
             padx = 10)
    inp.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    btn.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    return inp

def makeOutput(root):
    lab = tk.Label(root, font = ("Times", 16), text="Hypotheses: ", anchor='w')
    out = tk.Text(root, width = 60, height = 20, bg = "white")
    btn = tk.Button(root, text='Quit', command=root.quit)
    lab.pack(side = tk.TOP,
             fill = tk.BOTH,
             padx = 10)
    out.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    btn.pack(side=tk.TOP,
             padx=5,
             pady=5)
    return inp
if __name__ == '__main__':
    root = tk.Tk()
    entryFrame = tk.Frame(root)
    ents = makeObsv(entryFrame)
    entryFrame.grid(column = 0, row = 0)

    # b2 = tk.Button(root, text='Monthly Payment',
    #        command=(lambda e=ents: monthly_payment(e)))
    # b2.grid(column = 0, row = 1, padx=5, pady=5)

    rulesFrame = tk.Frame(root)
    ents = makeRules(rulesFrame)
    rulesFrame.grid(column = 0, row = 1)

    consoleFrame = tk.Frame(root)
    inp = tk.Text(consoleFrame, width = 60, height = 20, bg = "black")
    inp.pack(side = tk.TOP,
             fill = tk.X,
             padx = 5,
             pady = 5)
    consoleFrame.grid(column = 1, row = 0)

    outputFrame = tk.Frame(root)
    ents = makeOutput(outputFrame)
    outputFrame.grid(column = 1, row = 1)

    root.mainloop()
