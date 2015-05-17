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

        self.number_of_groups = 5
        self.groups = []


        l1 = Label(master, text="Goal").grid(row=0, column=0)
        l2 = Label(master, text="Importance").grid(row=0, column=1)
        l3 = Label(master, text="Probability A").grid(row=0, column=2)
        l4 = Label(master, text="Probability B").grid(row=0, column=3)

        for group_number in range(0, self.number_of_groups):
            self.groups.append(GroupEntry(frame, group_number))

        b = Button(frame, text="Draw", command=self.button_callback)
        b.pack()



    def button_callback(self):
        treatment_a_name = "Treatment A"
        treatment_b_name = "Treatment B"

        goal_list = []
        for group_number in range(0, self.number_of_groups):
            group_entry = self.groups[group_number]
            name = group_entry.e1.get()
            importance = group_entry.importance_slider.get()
            probability_a = group_entry.prob_a_slider.get()
            probability_b = group_entry.prob_b_slider.get()
            goal_list.append(Goal(name, importance, probability_a, probability_b))

        decision = Decision(treatment_a_name, treatment_b_name, goal_list)
        self.draw_decision(decision)


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
        row_number = group_number + 1

        label = Label(master, text="Goal " + str(group_number+1)).grid(row=group_number)

        self.e1 = Entry(master)
        self.e1.grid(row=row_number, column=1)

        self.importance_slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
        self.importance_slider.grid(row=row_number, column=2)

        self.prob_a_slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
        self.prob_a_slider.grid(row=row_number, column=3)

        self.prob_b_slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
        self.prob_b_slider.grid(row=row_number, column=4)


example_decision = Decision("Dialysis", "Not dialysis", [
    Goal("Live as long as possible", 0.6, 0.5, 0),
    Goal("Feel well day-to-day", 0.9, 0.3, 0.4),
    Goal("Minimise symptoms", 0.8, 0.4, 0.4)])

root = Tk()

seesaw_app = SeesawApp(root)
# seesaw_app.draw_decision(example_decision)

root.mainloop()
        
