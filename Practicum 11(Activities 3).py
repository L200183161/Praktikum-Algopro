from tkinter import *

my_app = Tk(className='Geometry')

L1 = Label(my_app, text='Geometry', font=('Comic Sans MS', 24, 'bold'))
L1.grid(row=0, column=0, sticky=W)
L2 = Label(my_app)
L2.grid(row=1, column=0, sticky=W)
L3 = Label(my_app, text='')
L3.grid(row=2, column=0, sticky=W)
L4 = Label(my_app, text='')
L4.grid(row=3, column=0, sticky=W)
L5 = Label(my_app, text='', font=('Comic Sans MS', 12, 'bold'))
L5.grid(row=4, column=0, sticky=W)
L6 = Label(my_app, text='Base: ')
L6.grid(row=5, column=0, sticky=W)
e1 = Entry(my_app)
e1.grid(row=6, column=0, sticky=W)
L7 = Label(my_app, text='Height: ')
L7.grid(row=7, column=0, sticky=W)
e2 = Entry(my_app)
e2.grid(row=8, column=0, sticky=W)

def luas():
    a = float(e1.get())
    t = float(e2.get())
    hasil = 0.5*a*t
    L9.config(text=hasil)

b1 = Button(my_app, text='Determine Area', command=luas)
b1.grid(row=9, column=0, sticky=W)
L8 = Label(my_app, text='Area =', font=('Comic Sans MS', 12, 'bold'))
L9 = Label(my_app, text='0', font=('Comic Sans MS', 12,'bold'))

my_app.mainloop()
