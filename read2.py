from tkinter import *
from tkinter.filedialog import askopenfilename
global a
def browse():
    a.set(askopenfilename(title='select new file'))
def browse_json():
    x.set(askopenfilename(title='select new file'))
def done():
    print(e1.get())
    print(e.get())
root = Tk()

a = StringVar()
x= StringVar()
l = Label(root, text="new file: ")
l.pack()

e = Entry(root, width=25, textvariable=a)
e.pack()

b = Button(root, text="Browse", command=browse)
b.pack()
l1=Label(root,text="new file:")
l1.pack()
e1 = Entry(root, width=25, textvariable=x)
e1.pack()
b1 = Button(root, text="Browse", command=browse_json)
b1.pack()
b2 = Button(root, text="OK!", command=done)
b2.pack()
root.mainloop()