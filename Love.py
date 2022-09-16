from cProfile import label
from gc import DEBUG_STATS
from logging import RootLogger, root
from tkinter import font, messagebox
from tkinter import *
import random

def ovbio():
    messagebox.showinfo(message="Lo sabía", title="Te Amo")

def no():
    messagebox.showinfo(message="El dispositivo ha sido bloqueado y todos los estan siendo cifrados", title="Ransomware Attack... ") 

def button_hover(event):
    x = random.randint(10, 400)
    y = random.randint(10, 400)
    my_button_2.place(x=x, y=y)

def exit_(event):
    x = random.randint(10, 400)
    y = random.randint(10, 400)
    my_button_2.place(x=x, y=y)

root = Tk()
root.geometry("600x400")
root.iconbitmap('/love.ico')
root.configure(background= '#ff05e2')
root.title('RESPONDEME')

label_0 = Label(root, text="Quieres ser mi NOVIA?", bg='#ff05e2',fg="black", width=0, font=("BubbleGum", 30))
label_0.place(x=90, y=60)

my_button_1 = Button(root, text="SI", width=5, height=1, font=("BubbleGum", 30), bg='#ff0505', fg="white", command = ovbio)
my_button_1.place(x=100, y=220)

my_button_2 = Button(root, text="NO", width=5, height=1, font=("bubbleGum", 30), bg='#ff0505', fg="white", command = no)
my_button_2.place(x=350, y=220)

my_button_2.bind("<Enter>", button_hover)
my_button_2.bind("<Leave>", exit_)

root.mainloop()
