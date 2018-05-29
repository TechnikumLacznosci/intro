from Tkinter import *
from SimpleTable import *
from TaskDownloader import Task

# Instantiate window
task = Task("https://raw.githubusercontent.com/TechnikumLacznosci/intro/master/files/tasks.json")
task_list = task.get_all()

window = Tk()
window.title("ToDo list app")

# Define number of columns
column_count = len(task_list[0])
# Define number of rows
row_count = len(task_list)
# Empty table object with size row_count x column_count
table = SimpleTable(window, row_count, column_count)
table.pack(side='top', fill='x')

# Fill table with values
for i in range(0, row_count):
    for j in range(0, column_count):
        table.set(i, j, get_from_table(i, j, table))
        #table.set(i, j, task_list[i][task_list[i].keys()[j]])


def get_from_table(i, j, tab):
    return 0


# Run app
window.mainloop()