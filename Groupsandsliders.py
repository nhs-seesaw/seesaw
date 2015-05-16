#!/usr/bin/python


from tkinter import *

class GroupEntry:
	def __init__(self, group_number, group_label):
		listbox = Listbox(master)

		label = Label(master, text=group_label).grid(row=group_number)


		#This bit is broken

		e1 = Entry(master)


		e1.grid(row=group_number, column=1)


		#listbox.insert(END, "a list entry")

		#listbox.insert(END, "nhs")

		#for item in ["one", "two", "three", "four"]:
		#    listbox.insert(END, item)



		w = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
		w.grid(row=group_number, column=2)

		v = Scale(master, from_=0, to=100, orient=HORIZONTAL, show=0)
		v.grid(row=group_number, column=3)






master = Tk()

number_of_groups = 5

for group_number in range(0, number_of_groups):

	group = GroupEntry(group_number, "Group " + str(group_number+1))

mainloop()