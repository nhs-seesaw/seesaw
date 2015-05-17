#!/usr/bin/python

from Tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SeesawApp:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.graph_w = 200
        self.graph_h = 120

        number_of_groups = 5
        groups = []

        for group_number in range(0, number_of_groups):
            groups.append(GroupEntry(frame, group_number))


        goal_list = []



    def draw_decision(self, decision):
        x = [goal.prob_a - goal.prob_b for goal in decision.goals]
        y = [goal.importance for goal in decision.goals]
        p = plt.bar(x, y,width = 0.1)
        p = plt.show()

        canvas = FigureCanvasTkAgg(p.figure, master=self.frame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

class Decision:
    def __init__(self, treatment_a, treatment_b, goals):
        self.treatment_a = treatment_a
        self.treatment_b = treatment_b
        self.goals = goals
        
class Goal:
    def __init__(self, name, importance, probability_a, probability_b):
        self.name = name
        self.importance = importance
        self.prob_a = probability_a
        self.prob_b = probability_b

class GroupEntry:
	def __init__(self, master, group_number):
		listbox = Listbox(master)

		label = Label(master, text="Group " + str(group_number+1)).grid(row=group_number)

		e1 = Entry(master)
		e1.grid(row=group_number, column=1)

		w = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
		w.grid(row=group_number, column=2)

		v = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
		v.grid(row=group_number, column=3)


example_decision = Decision("Dialysis", "Not dialysis", [
    Goal("Live as long as possible", 0.6, 0.5, 0),
    Goal("Feel well day-to-day", 0.9, 0.3, 0.4),
    Goal("Minimise symptoms", 0.8, 0.4, 0.4)])

root = Tk()

seesaw_app = SeesawApp(root)
seesaw_app.draw_decision(example_decision)

root.mainloop()
        
