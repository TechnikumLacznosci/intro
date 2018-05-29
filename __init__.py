from Tkinter import *
from SimpleTable import *
from TaskDownloader import Task
import json
import tkFileDialog

window = Tk()
window.title("ToDo list app")
window.geometry('500x300')

json_file_uri = "httpss://raw.githubusercontent.com/TechnikumLacznosci/intro/master/files/tasks.json"

def instantiate_table(data_list):
    # Define number of columns
    column_count = len(data_list[0])
    # Define number of rows
    row_count = len(data_list)
    # Empty table object with size row_count x column_count
    table = SimpleTable(window, row_count, column_count)
    table.pack(side='top', fill='x')
    
    def get_from_table(i, j, tab):
        return data_list[i][data_list[i].keys()[j]]
    
    # Fill table with values
    for i in range(0, row_count):
        for j in range(0, column_count):
            table.set(i, j, get_from_table(i, j, table))

# Add file dialog button
def data_call_file_dialog():
    window.filename = tkFileDialog.askopenfilename(initialdir = 'C:\\',title="Select file: ", filetypes= (("JSON File",'*.json'), ("All files", '*')))
    print(window.filename)
    with open(window.filename, 'r') as json_file:
        Data_list = json.load(json_file)
        instantiate_table(Data_list)

def data_get_from_internet():
    while True:
        try:
            task = Task(json_file_uri)
            task_list = task.get_all()
            instantiate_table(task_list)
            break
        except Exception as e:
            print(e.message)

# Add 'Load tasks' button
button_call_table = Button(window, text="Load tasks", command=data_get_from_internet)
button_call_table.grid(column='0',row='0')

button_call_file_dialog = Button(window, text="Choose file", command=data_call_file_dialog)
button_call_file_dialog.grid(column='1',row='0')

# Run app
window.mainloop()