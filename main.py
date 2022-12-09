from customtkinter import *
import random
import time


def submit():
    if name1.get() == "" or name2.get() == "":
        percent.set("Please enter both names properly")
        return None

    love = random.randint(21,99)
    start = 0
    speed = 2
    lovebar.set(0)
    while start < love:
        start += speed
        lovebar.step()
        percent.set(str(f"{name1.get()} & {name2.get()} is a {int(start)}% Match!"))
        time.sleep(0.05)
        root.update_idletasks()
    percent.set(str(f"{name1.get()} & {name2.get()} is a {int(love)}% Match!"))


def change_theme():
    global theme
    if theme == 2:
        theme = 1
        set_appearance_mode("light")
    else:
        theme = 2
        set_appearance_mode("dark")

    root.update_idletasks()



theme = 2 # 1 = light, 2 = dark
root = CTk()
root.title("Love Rater")
root.geometry("360x480")
root.resizable(False, False)

frame1 = CTkFrame(root, border_width=2)

# name etc
CTkLabel(frame1, text="insert your name", font=("Consolas", 15)).pack()
name1 = CTkEntry(frame1)
name1.pack()

CTkLabel(frame1, text="Insert the desired target name", font=("Consolas", 15)).pack()
name2 = CTkEntry(frame1)
name2.pack()

CTkLabel(frame1, text="\n").pack()
submitbutton = CTkButton(frame1, text="Check your love", command=submit, fg_color="#BB0000", hover_color="#FF0000")
submitbutton.pack()
CTkLabel(frame1, text="\n").pack()

frame1.pack()

# bar title
CTkLabel(root, text="Love meter", font=("Consolas", 20)).pack()

# The lovebar
lovebar = CTkProgressBar(root, orientation=VERTICAL, height=200, progress_color="red")
lovebar.set(0)
lovebar.pack()
percent = StringVar()
CTkLabel(root, textvariable=percent).pack()

# Theme
themebutton = CTkButton(root, text="Change theme", command=change_theme, fg_color="#BB00BB", width=50,
                        hover_color="#FF00FF")
themebutton.pack(side=BOTTOM, anchor=SW, padx=10, pady=5, ipadx=10, ipady=5)

root.mainloop()
