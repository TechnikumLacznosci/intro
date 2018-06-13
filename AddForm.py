from Tkinter import Tk, Entry, Label, Button
from FileDialog import call_file_dialog
from TaskDownloader import Task


# Add form
add_form = Tk()
e0 = Entry(add_form)
e1 = Entry(add_form)
e2 = Entry(add_form)
e3 = Entry(add_form)
e4 = Entry(add_form)
Label(add_form, text="Data rozpoczecia").grid(row=0)
Label(add_form, text="Data zakonczenia").grid(row=1)
Label(add_form, text="Tytul").grid(row=2)
Label(add_form, text="Opis").grid(row=3)
Label(add_form, text="Flagi").grid(row=4)
e0.grid(row=0, column=2)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
button_formularz1 = Button(add_form, text="Ok")
button_formularz1.grid(column=0, row=5)
button_formularz2 = Button(add_form, text="Anuluj")
button_formularz2.grid(column=1, row=5)

# Add 'Load tasks' button
def buttons_show(window, url):
    task = Task(window, url)
    button_call_table = Button(window, text="Zaladuj zadania", command=task.get_data_from_internet)
    button_call_table.grid(column='0', row='0')

    button_call_file_dialog = Button(window, text="Wybierz plik", command=call_file_dialog)
    button_call_file_dialog.grid(column='1', row='0')