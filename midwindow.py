import tkinter as tk

master = tk.Tk()
master.title('Test')
master.geometry("100x100+700+350")

b1 = tk.Button(text='1')
b1.grid(row=0, column=0)

b2 = tk.Button(text='2')
b2.grid(row=0, column=1)

b3 = tk.Button(text='3')
b3.grid(row=1, column=0)

b4 = tk.Button(text='4')
b4.grid(row=1, column=1)

b5 = tk.Button(text='5')
b5.grid(row=2, columnspan=2)

tk.mainloop()
