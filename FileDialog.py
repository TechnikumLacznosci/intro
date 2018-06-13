import json
import tkFileDialog
from TaskTable import instantiate_table
from Tkinter import Frame, Button


class Dialog(object):
    
    def __init__(self, window):
        self.window = window
        
    def call_file_dialog(self):
        file_extensions = [("JSON File", '*.json'), ("All files", '*')]
        self.window.filename = tkFileDialog.askopenfilename(initialdir = 'C:\\',
            title="Select file: ", filetypes = file_extensions)
        with open(self.window.filename, 'r') as json_file:
            data_list = json.load(json_file)
            # remove previous table
            self.window.nametowidget('tableWithTasks').grid_forget()
            instantiate_table(self.window, data_list)
        
    def frame_with_buttons(self):
        button_frame = Frame(self.window)
        button_frame.grid(row='1', column='0')
    
        button_call_file_dialog = Button(button_frame, text="Choose file", command=self.call_file_dialog)
        button_call_file_dialog.grid(row='0', column='0')