from Tkinter import *
from SimpleTable import *
from TaskDownloader import Task

# Instantiate window
task = Task("https://raw.githubusercontent.com/TechnikumLacznosci/intro/master/files/tasks.json")
task_list = task.get_all()

window = Tk()
window.title("ToDo list app")

# Define number of columns
column_count =
# Define number of rows
row_count =
# Empty table object with size row_count x column_count
table = SimpleTable(window, row_count, column_count)
table.pack(side='top', fill='x')

# Fill table with values
table.set(0, 0, task_list[0]['title'])






# Run app
window.mainloop()