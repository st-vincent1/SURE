import tkinter as tk

obsvs = 3
def abduce():
    # s = inputBox.get()
    pass

def extendObsv(pos):
    Entry(main, width = 20, bg = "white").grid(row = pos, column = 0, sticky = W)

# Add centered label at top
#Split the pane in 2
"""
North: name

Column 0: inputs
Label: Observables:
Text field: to add observables line by line
Label: Rules:
Text field: to add rules line by line
Button: Run abduction

Column 1: outputs
Label: Hypotheses:
Text field: all hypotheses
Label: MPH:
Entry field: one hypothesis

South: panel which shows what has been interpreted from input and general works (print graph)
South: Examples
Add buttons to produce examples - automatic inputs
"""
root = tk.Tk()
lab = tk.Label(root, width=22, text="Abduction engine: ", anchor='w')
lab.grid(padx = row = 0, column = 0, sticky = W)

# ent = tk.Entry(row)
# ent.insert(0, "0")
row.pack(side=tk.TOP,
         fill=tk.X,
         padx=5,
         pady=5)
lab.pack(side=tk.TOP)
# ent.pack(side=tk.RIGHT,
         # expand=tk.YES,
         # fill=tk.X)
root.mainloop()

# for i in range(3):
    inputBox = Entry(main, width = 20, bg = "white")
    inputBox.grid(row = i, column = 0, sticky = W)
Button(main, width = 20, text = "Add more observations...", command = extendObsv(4)).grid(row = 3, column = 0)
#Button
Button(main, width = 20, height = 5, text = "Run abduction!", command = abduce).grid(row = 5, column = 0, sticky = W)
# Label Rules:
Rules - same; text box, line by line
# 2nd Pane
#Output box
outputHyp = Text(main, width = 20, height = 5, background = "white")
outputHyp.grid(row = 1, column = 1, sticky = E)

outputMPH = Text(main, width = 20, height = 5, background = "white")
outputMPH.grid(row = 2, column = 1, sticky = E)


########


# def makeform(root, fields):
#     entries = {}
#     for i in obsvs:
#         row = tk.Frame(root)
#         lab = tk.Label(row, width=22, text="Observation #" + str(i) + ": ", anchor='w')
#         ent = tk.Entry(row)
#         ent.insert(0, "0")
#         row.pack(side=tk.TOP,
#                  fill=tk.X,
#                  padx=5,
#                  pady=5)
#         lab.pack(side=tk.LEFT)
#         ent.pack(side=tk.RIGHT,
#                  expand=tk.YES,
#                  fill=tk.X)
#         entries[line] = ent
#     return entries
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     ents = makeform(root, fields)
#     b1 = tk.Button(root, text='Final Balance',
#            command=(lambda e=ents: final_balance(e)))
#     b1.pack(side=tk.LEFT, padx=5, pady=5)
#     b2 = tk.Button(root, text='Monthly Payment',
#            command=(lambda e=ents: monthly_payment(e)))
#     b2.pack(side=tk.LEFT, padx=5, pady=5)
#     b3 = tk.Button(root, text='Quit', command=root.quit)
#     b3.pack(side=tk.LEFT, padx=5, pady=5)
#     root.mainloop()
