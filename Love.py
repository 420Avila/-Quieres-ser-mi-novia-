
from cProfile import label
from gc import DEBUG_STATS
from logging import RootLogger, root
from tkinter import font, messagebox
from tkinter import *
import random

def ovbio():
    messagebox.showinfo(message="I KNEW IT", title="I LOVE")

def no():
    messagebox.showinfo(message="The device has been locked and all files are being encrypted.", title="Ransomware Attack... ") 

def button_hover(event):
    x = random.randint(1, 250)
    y = random.randint(1, 250)
    my_button_2.place(x=x, y=y)

def exit_(event):
    x = random.randint(1, 250)
    y = random.randint(1, 250)
    my_button_2.place(x=x, y=y)

root = Tk()
root.geometry("800x300")
root.iconbitmap('C:/Users/420avila/Desktop/GitHub/pruebas tecnicas/queires ser mi novia/love.ico')
root.configure(background= '#ff05e2')
root.title('I LOVE YOU')

label_0 = Label(root, text="Do you want to be my girlfriend?", bg='#ff05e2',fg="black", width=0, font=("BubbleGum", 30))
label_0.place(x=90, y=60)

my_button_1 = Button(root, text="YES", width=5, height=1, font=("BubbleGum", 30), bg='#ff0505', fg="white", command = ovbio)
my_button_1.place(x=200, y=150)

my_button_2 = Button(root, text="NO", width=5, height=1, font=("bubbleGum", 30), bg='#ff0505', fg="white", command = no)
my_button_2.place(x=500, y=150)

my_button_2.bind("<Enter>", button_hover)
my_button_2.bind("<Leave>", exit_)

root.mainloop()
