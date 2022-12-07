from tkinter import *
from tkinter.ttk import *
import random
import time


def submit():
    love = random.randint(21,99)
    start = 0
    speed = 2
    lovebar['value'] = 0
    # print(f"{name1.get()} & {name2.get()} is a {love}% match!")
    while start < love:
        start += speed
        lovebar['value'] += speed
        percent.set(str(f"{int(start)}% Match!"))
        time.sleep(0.05)
        root.update_idletasks()

    # if it overfills, this piece of code will stop it
    if start > love:
        lovebar['value'] = love
        percent.set(str(f"{love}% Match!"))


root = Tk()
root.title("Love Rater")
root.geometry("360x480")

frame1 = Frame(root, relief=SUNKEN, borderwidth=10)

Label(frame1, text="insert your name", font=("Consolas", 10)).pack()
name1 = Entry(frame1)
name1.pack()

Label(frame1, text="Insert the desired target name", font=("Consolas", 10)).pack()
name2 = Entry(frame1)
name2.pack()

Label(frame1).pack()
submitbutton = Button(frame1, text="Check your love", command=submit)
submitbutton.pack()
Label(frame1).pack()

frame1.pack()

Label(root, text="Love meter", font=("Consolas", 20)).pack()

lovebar = Progressbar(root, orient=VERTICAL, length=200)
lovebar.pack()
percent = StringVar()
Label(textvariable=percent).pack()

root.mainloop()
