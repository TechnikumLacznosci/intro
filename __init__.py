from Tkinter import *
from SimpleTable import *
from TaskDownloader import Task
import json
import tkFileDialog
import urllib2

window = Tk()
window.title("ToDo list app")

json_file_uri = "https://raw.githubusercontent.com/TechnikumLacznosci/intro/master/files/tasks.json"

def instantiate_table(data_list):
    # Define number of columns
    column_count = len(data_list[0])
    # Define number of rows
    row_count = len(data_list)
    # Empty table object with size row_count x column_count
    table = SimpleTable(window, row_count, column_count)
    table.grid(row='0', column='0')

    def get_from_table(i, j, tab):
        return data_list[i][data_list[i].keys()[j]]

    # Fill table with values
    for i in range(0, row_count):
        for j in range(0, column_count):
            table.set(i, j, get_from_table(i, j, table))

# Add file dialog button
def call_file_dialog():
    file_extensions = [("JSON File", '*.json'), ("All files", '*')]
    window.filename = tkFileDialog.askopenfilename(initialdir = 'C:\\',
        title="Select file: ", filetypes = file_extensions)
    with open(window.filename, 'r') as json_file:
        data_list = json.load(json_file)
        # remove previous table
        window.nametowidget('tableWithTasks').grid_forget()
        instantiate_table(data_list)

def get_data_from_internet():
    try:
        task = Task(json_file_uri)
        task_list = task.get_all()
        instantiate_table(task_list)
    except urllib2.URLError:
        print("Failed to load the given URL")

def frame_with_buttons():
    button_frame = Frame(window)
    button_frame.grid(row='1', column='0')

    button_call_file_dialog = Button(button_frame, text="Choose file", command=call_file_dialog)
    button_call_file_dialog.grid(row='0', column='0')


# Fill table with the data from the internet
get_data_from_internet()
# Add buttons below the table
frame_with_buttons()

# Run app
window.mainloop()
