import tkinter.messagebox
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from functools import partial
"""
        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()
"""

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Student Register Manager')
        self.geometry('600x600')


        # buttons
        self.button = ttk.Button(self, text='Add')
        self.button['command'] = self.create_buttons_for_add
        self.button.place(x = 10, y = 110)

        self.button = ttk.Button(self, text="Remove")
        self.button['command'] = self.button_clicked
        self.button.place(x = 10, y = 300)

        self.button = ttk.Button(self, text="Update")
        self.button['command'] = self.button_clicked
        self.button.place(x = 10, y = 260)

        self.button = ttk.Button(self, text="List")
        self.button['command'] = self.button_clicked
        self.button.place(x = 10, y = 360)

        self.button = ttk.Button(self, text="Grade")
        self.button['command'] = self.button_clicked
        self.button.place(x = 10, y = 460)

        self.button = ttk.Button(self, text="Search")
        self.button['command'] = self.button_clicked
        self.button.place(x = 10, y = 560)

    def create_buttons_for_add(self):
        self.button = ttk.Button(self, text='Student')
        self.button['command'] = self.create_labels_for_add_student
        self.button.place(x = 90, y = 60)

        self.button = ttk.Button(self, text='Discipline')
        self.button['command'] = self.create_labels_for_add_discipline
        self.button.place(x = 90, y = 160)


    def submit_for_student_id_in_add(self):
        # the_student_id = self.entry_student_id.get()
        # print(the_student_id)
        submit = "It worked."
        self.label = ttk.Label(self, text = submit).place( x = 530, y = 20)

    def submit_for_student_name_in_add(self):
        submit = "It worked."
        self.label = ttk.Label(self, text = submit).place( x = 530, y = 100)

    def create_labels_for_add_student(self):

        student_id = tk.StringVar()

        self.label_student_id = ttk.Label(self, text='Student id: ').place(x = 170, y = 20)
        self.entry_student_id = tk.Entry(self, width = 30, textvariable = student_id)
        self.entry_student_id.place(x = 260, y = 20)
        student_id = self.entry_student_id.get() # in student id is the id taken from the entry.
        self.button = ttk.Button(self, text="submit", command = self.submit_for_student_id_in_add).place(x = 450, y = 20)

        student_name = tk.StringVar()

        self.label_student_name = ttk.Label(self, text = "Student name: ").place(x = 170, y = 100)
        self.entry_student_name = tk.Entry(self, width = 30, textvariable = student_name)
        self.entry_student_name.place(x = 260, y = 100)
        student_name = self.entry_student_name.get() # in student name is the student name taken from the entry.
        self.button = ttk.Button(self, text="submit", command = self.submit_for_student_name_in_add).place(x = 450, y = 100)

    def submit_for_discipline_id_in_add(self):
        submit = "It worked."
        self.label = ttk.Label(self, text = submit).place(x = 530, y = 130)

    def submit_for_discipline_name_in_add(self):
        submit = "It worked."
        self.label = ttk.Label(self, text = submit).place(x = 530, y = 210)

    def create_labels_for_add_discipline(self):
        discipline_id = tk.StringVar()
        self.label_discipline_id = ttk.Label(self, text = "Discipline id: ").place( x = 170, y = 130)
        self.entry_discipline_id = tk.Entry(self, width = 30, textvariable = discipline_id)
        self.entry_discipline_id.place(x = 260, y = 130)
        discipline_id = self.entry_discipline_id.get()
        self.button = ttk.Button(self, text="submit", command = self.submit_for_discipline_id_in_add).place(x = 450, y = 130)

        discipline_name = tk.StringVar()
        self.label_discipline_name = ttk.Label(self, text = "Discipline name: ").place( x = 170, y = 210)
        self.entry_discipline_name = tk.Entry(self, width = 30, textvariable = discipline_name)
        self.entry_discipline_name.place(x = 260, y = 210)
        discipline_name = self.entry_discipline_name.get()
        self.button = ttk.Button(self, text="submit", command = self.submit_for_discipline_name_in_add).place(x = 450, y = 210)



    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')


if __name__ == "__main__":
    app = App()
    app.mainloop()