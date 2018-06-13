from Tkinter import Tk
from SimpleTable import *
from TaskDownloader import Task
from TaskTable import instantiate_table
from FileDialog import Dialog

JSON_FILE_URI = "https://raw.githubusercontent.com/TechnikumLacznosci/intro/master/files/tasks.json"

window = Tk()
window.title("ToDo list app")

# Fill table with the data from the internet
task = Task(window, JSON_FILE_URI)
task.get_data_from_internet()
# Add buttons below the table
Dialog(window).frame_with_buttons()

# Run app
window.mainloop()