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

    def draw_decision(self, decision):
        x = [goal.prob_a - goal.prob_b for goal in decision.goals]
        y = [goal.importance for goal in decision.goals]
        p, = plt.plot(x, y)

        canvas = FigureCanvasTkAgg(p.figure, master=root)
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
        
example_decision = Decision("Dialysis", "Not dialysis", [
    Goal("Live as long as possible", 0.6, 0.5, 0),
    Goal("Feel well day-to-day", 0.9, 0.3, 0.4),
    Goal("Minimise symptoms", 0.8, 0.4, 0.4)])

root = Tk()

seesaw_app = SeesawApp(root)
seesaw_app.draw_decision(example_decision)

root.mainloop()
        
