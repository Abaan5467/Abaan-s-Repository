from cProfile import label
from tkinter import *
from pandas import read_csv
from seaborn import countplot
from matplotlib.pyplot import show

frame = Tk()
frame.geometry('800x500')
frame.title('Data Plotter')

def data():
    df = read_csv(path_box.get())
    if hue_box.get() == 's':
        countplot(x=column_box.get(),data=df)
        show()
    else:
        countplot(x=column_box.get(),hue =hue_box.get(),data=df)
        show()

path = Label(frame,text='Enter the path of the csv file with two backslashes: ')
column = Label(frame,text='Enter the name of the colmn to be plotted: ')
hue = Label(frame,text='Enter the hue or s to skip this: ')
btn = Button(frame,text='Plot',padx=15,pady=3,fg="red",bg='orange',command=data)

path_box=Entry(frame,width=50)
column_box=Entry(frame,width=50)
hue_box=Entry(frame,width=50)

path.grid(row=0,column=0)
column.grid(row=1,column=0)
hue.grid(row=2,column=0)
btn.grid(row=3,column=0)

path_box.grid(row=0,column=1)
column_box.grid(row=1,column=1)
hue_box.grid(row=2,column=1)

frame.mainloop()
