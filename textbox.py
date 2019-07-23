from tkinter import *
from tkinter.scrolledtext import ScrolledText

mainwin = Tk()
Label(mainwin, text="An Entry Box:").grid(row=0, column=0)
ent = Entry(mainwin, width=70); ent.grid(row=0, column=1)
Button(mainwin, text="Print Entry", command=(lambda: print(ent.get()))).grid(row=0, column=2, sticky="EW")

Label(mainwin, text="ScrolledText Box:").grid(row=1, column=0)
st = ScrolledText(mainwin, height=5); st.grid(row=1, column=1)
Button(mainwin, text="Print Text", command=(lambda: dag.addObsv(st.get(1.0, END)))).grid(row=1, column=2, sticky="EW")

Button(mainwin, text="Exit", command=sys.exit).grid(row=2, column=0, columnspan=3, sticky="EW")
mainwin.mainloop()
