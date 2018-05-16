from Tkinter import *
from SimpleTable import *
from TaskDownloader import Task

# Instantiate window
task = Task("https://raw.githubusercontent.com/TechnikumLacznosci/intro/master/files/tasks.json")
task_list = task.get_all()

window = Tk()
window.title("ToDo list app")

t = SimpleTable(window, len(task_list), 8)
t.pack(side='top', fill='x')

t.set(0, 0, task_list[0]['title'])


# Run app
window.mainloop()