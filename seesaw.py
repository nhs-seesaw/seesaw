from Tkinter import *

class SeesawApp:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.balance = Canvas(master, width=200, height=100)
        self.balance.pack()

        self.balance.create_line(0, 0, 200, 100)
        self.balance.create_line(0, 100, 200, 0, fill='red', dash=(4,4))

        self.balance.create_rectangle(50, 25, 150, 75, fill="blue")

root = Tk()

seesaw_app = SeesawApp(root)

root.mainloop()
