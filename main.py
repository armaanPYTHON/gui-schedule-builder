from tkinter import *
import csv
from tkinter import filedialog
import os
from tkinter.ttk import Combobox
import pandas as pd


color='#42cbf5'
root = Tk()
root.title('Schedule Builder')
root.geometry('400x400')
root.config(bg=color)

headings = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time = []

rows=[]

for i in range(7, 23):
    time.append(str(i) + str(':00'))
    time.append(str(i) + str(':30'))
    
for i in range(len(time)):
    x = []
    x.append(time[i])
    for r in range(7):
        x.append('-')
    rows.append(x)
print(rows)


def start(e=None):

    filename = filedialog.asksaveasfilename(title='Save File', defaultextension=(
        ("CSV files", '*.csv'),
        ('All Files', '*.*')), 
        filetypes=(
            ("CSV files", '*.csv'),
            ('All Files', '*.*')))
    if '.csv' in filename:
        pass
    else:
        filename = filename + '.csv'
    
    csvfile = open(filename, 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(headings)
    for row in rows:
        writer.writerow(row)
    
    csvfile.close()



    #--------------GUI DESIGN------------------
    for widget in root.winfo_children():
        widget.destroy()

    c= {'bg':color, 'fg':'white'}
    Label(root, c, text='From: ').grid(row=0, column=0)
    Label(root, c, text='To: ').grid(row=1, column=0)
    Label(root, c, text='Day: ').grid(row=2, column=0)
    Label(root, c, text='Title: ').grid(row=3, column=0, padx=10)

    tentry = Entry(root, bd=1, width=30)
    tentry.grid(row=3, column=1)
    tcombo = Combobox(root, width=27, values=time)
    tcombo.grid(row=1, column=1, pady=5)
    fcombo = Combobox(root, values=time, width=27)
    fcombo.grid(row=0, column=1)
    dcombo = Combobox(root, values=days, width=27)
    dcombo.grid(row=2, column=1)
    fcombo.set(time[0])
    tcombo.set(time[0])
    dcombo.set(days[0])

    def view(e=None):
        os.startfile(filename)

    def sub(e=None):
        findex = time.index(fcombo.get())
        tindex = time.index(tcombo.get())

        print(findex, tindex)

        df = pd.read_csv(filename)
        for i in range(findex, tindex):
            df.loc[i, dcombo.get()] = tentry.get()
            df.to_csv(filename, index=False)

        tentry.delete(0, END)

    Button(root, text='Enter', bg='white', height=1, width=10, bd=0, cursor='hand2',
    activebackground='black', activeforeground='white', command=sub).grid(row=4, column=0, columnspan=2, pady=10)

    Button(root, text='View', bg='white', height=1, width=10, bd=0, cursor='hand2',
    activebackground='black', activeforeground='white', command=view).grid(row=5, column=0, columnspan=2, pady=10)


    root.bind('<Control-v>', view)
    root.bind('<Return>', sub)





Button(root, text='Start', bg='white', height=3, width=15, bd=0, cursor='hand2',
activebackground='black', activeforeground='white', command=start).place(rely=0.35, relx=0.35)




mainloop()