import tkinter


import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir = tkinter.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
if len(tempdir) > 0:
    print("You chose %s" % tempdir)