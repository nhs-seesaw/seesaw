#!/usr/bin/python

from Tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SeesawApp:

    def __init__(self, master, decision):
        self.frame = Frame(master)
        self.frame.pack()

        self.graph_w = 200
        self.graph_h = 120

        number_of_groups = 5
        groups = []

        for group_number in range(0, number_of_groups):
            label = Label(self.frame, text="Group " + str(group_number+1))
            label.grid(row=group_number, column=0)
            
            e1 = Entry(self.frame)
            e1.grid(row=group_number, column=1)
            
            w = Scale(self.frame, from_=0, to=100, orient=HORIZONTAL, show=0)
            w.grid(row=group_number, column=2)
            
            v = Scale(self.frame, from_=0, to=100, orient=HORIZONTAL, show=0)
            v.grid(row=group_number, column=3)
        
        x = [goal.prob_a - goal.prob_b for goal in decision.goals]
        y = [goal.importance for goal in decision.goals]

        # create figure instance
        p = plt.figure()
        
        # remove axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)

        # plot bar chart
        barlist = plt.bar(x, y,width = 0.2,align='center')
        bar_col = ['b','g','r','c','m','y']
        i=0
        for cs in barlist:
            cs.set_color(bar_col[i])
            i=i+1

        # plot vertical line
        plt.vlines(0,0,1,lw=5)

        # set axis
        plt.axis([-2,2,0,1])

        # pass figure to tk and render
        canvas = FigureCanvasTkAgg(p, master=self.frame)
        canvas.show()
        canvas.get_tk_widget().grid(row=number_of_groups, columnspan=4)
        
        goal_list = []

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

example_decision = Decision("Dialysis", "Not dialysis", [
    Goal("Live as long as possible", 0.6, 0.5, 0),
    Goal("Feel well day-to-day", 0.9, 0.3, 0.4),
    Goal("Minimise symptoms", 0.8, 0.4, 0.4)])

root = Tk()

seesaw_app = SeesawApp(root, example_decision)

root.mainloop()
        
