import PyPDF2
import os
from fdfgen import forge_fdf
import json
from tkinter import *
from tkinter.filedialog import askopenfilename
global a,x,j_file,pdf_file
def browse():
    a.set(askopenfilename(title='select PDF file'))
def browse_json():
    x.set(askopenfilename(title='select JSON file'))
def done():
    pdf_file=e.get()
    j_file=e1.get()
    json_data = json.loads(open(j_file).read())
    python_obj = json_data
    r2 = python_obj
    print(python_obj['address']['streetAddress'])
    print(r2)
    pr = PyPDF2.PdfFileReader(open(pdf_file, 'rb'), strict=False)
    dict = pr.getFields()
    print(dict)
    r1 = list(dict.keys())
    i = 0
    print(r1)
    for r in r1:
        print(str(i) + " " + r)
        i += 1
    fields = [(r1[0], r2['lastName']), (r1[1], r2['firstName']), (r1[2], r2['date']), (r1[4], 'Yes'), (r1[5], 'Yes'),
              (r1[3], 'Yes')]
    fdf = forge_fdf("", fields, [], [], [], [])
    fdf_file = open("data.fdf", "wb")
    fdf_file.write(fdf)
    fdf_file.close()
    os.system('pdftk "input2.pdf" fill_form "data.fdf" output "output.pdf" flatten')
    print("done")
    json_data = json.loads(open(j_file).read())
    python_obj = json_data
    r2 = python_obj
    print(python_obj['address']['streetAddress'])
    print(r2)
    pr = PyPDF2.PdfFileReader(open(pdf_file, 'rb'), strict=False)
    dict = pr.getFields()
    print(dict)
    r1 = list(dict.keys())
    i = 0
    print(r1)
    for r in r1:
        print(str(i) + " " + r)
        i += 1
    fields = [(r1[0], r2['lastName']), (r1[1], r2['firstName']), (r1[2], r2['date']), (r1[4], 'Yes'), (r1[5], 'Yes'),
              (r1[3], 'Yes')]
    fdf = forge_fdf("", fields, [], [], [], [])
    fdf_file = open("data.fdf", "wb")
    fdf_file.write(fdf)
    fdf_file.close()
    os.system('pdftk "' + pdf_file + '" fill_form "data.fdf" output "output.pdf" flatten')
    print("done")
    exit()
root = Tk()
a = StringVar()
x = StringVar()
l = Label(root, text="pdf file: ")
l.pack()

e = Entry(root, width=25, textvariable=a)
e.pack()

b = Button(root, text="Browse", command=browse)
b.pack()
l1=Label(root,text="json file:")
l1.pack()
e1 = Entry(root, width=25, textvariable=x)
e1.pack()
b1 = Button(root, text="Browse", command=browse_json)
b1.pack()
b2 = Button(root, text="OK!", command=done)
b2.pack()
root.mainloop()
