from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Minecraft").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="MultiMC").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="MultiMC").grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>')

root.mainloop()
