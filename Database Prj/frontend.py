import tkinter as tk
from tkinter import *
import backend


def get_selected_row(event):
    global selected_row
    index = listbox.curselection()[0]
    selected_row = listbox.get(index)

    e1.delete(0, END)
    e1.insert(END, selected_row[1])
    e2.delete(0, END)
    e2.insert(END, selected_row[2])
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    e4.delete(0, END)
    e4.insert(END, selected_row[4])
    e5.delete(0, END)
    e5.insert(END, selected_row[5])
    e6.delete(0, END)
    e6.insert(END, selected_row[6])


def view_command():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)


def search_command():
    listbox.delete(0, END)
    for row in backend.search(date_text.get(), earnings_text.get(), exercise_text.get(), diet_text.get(), study_text.get(), python_text.get()):
        listbox.insert(END, row)


def add_command():
    backend.insert(date_text.get(), earnings_text.get(), exercise_text.get(), diet_text.get(), study_text.get(), python_text.get())
    view_command()
    clear_entries()


def delete_command():
    backend.delete(selected_row[0])
    view_command()


def clear_entries():
    date_text.set('')
    earnings_text.set('')
    exercise_text.set('')
    diet_text.set('')
    study_text.set('')
    python_text.set('')


win = Tk()
win.wm_title('Database Project')
win.geometry("700x300")

l1 = Label(win, text='Date')
l1.grid(row=0, column=0)
l2 = Label(win, text='Exercise')
l2.grid(row=1, column=0)
l3 = Label(win, text='Diet')
l3.grid(row=2, column=0)
l4 = Label(win, text='Study')
l4.grid(row=0, column=2)
l5 = Label(win, text='Python')
l5.grid(row=1, column=2)
l6 = Label(win, text='Earnings')
l6.grid(row=2, column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

exercise_text = StringVar()
e2 = Entry(win, textvariable=exercise_text)
e2.grid(row=1, column=1)

diet_text = StringVar()
e3 = Entry(win, textvariable=diet_text)
e3.grid(row=2, column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=0, column=3)

python_text = StringVar()
e5 = Entry(win, textvariable=python_text)
e5.grid(row=1, column=3)

earnings_text = StringVar()
e6 = Entry(win, textvariable=earnings_text)
e6.grid(row=2, column=3)

b1 = Button(win, text='Add', width=16, pady=5, command=add_command)
b1.grid(row=4, column=3)
b2 = Button(win, text='Search', width=16, pady=5, command=search_command)
b2.grid(row=5, column=3)
b3 = Button(win, text='Delete Date', width=16, pady=5, command=delete_command)
b3.grid(row=6, column=3)
b4 = Button(win, text='View All', width=16, pady=5, command=view_command)
b4.grid(row=7, column=3)
b5 = Button(win, text='Close', width=16, pady=5, command=win.destroy)
b5.grid(row=8, column=3)

scrollbar = Scrollbar(win)
scrollbar.grid(row=3, column=0, rowspan=8)

listbox = Listbox(win, yscrollcommand=scrollbar.set)
listbox.grid(row=3, column=1, rowspan=8)

listbox.bind('<<ListboxSelect>>', get_selected_row)

win.mainloop()