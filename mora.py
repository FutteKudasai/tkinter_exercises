from tkinter import *
from PIL import Image, ImageTk
import random



def mora(event):
    player_select["image"] = picture[event]
    i = random.randint(0, 2)
    computer_select["image"] = picture[i]
    if(event == 0):
        if(0 == i):
            result["text"] = "平手"
        if(1 == i):
            result["text"] = "你輸了"
        if(2 == i):
            result["text"] = "你贏了"
    if(event == 1):
        if(0 == i):
            result["text"] = "你贏了"
        if(1 == i):
            result["text"] = "平手"
        if(2 == i):
            result["text"] = "你輸了"
    if(event == 2):
        if(0 == i):
            result["text"] = "你輸了"
        if(1 == i):
            result["text"] = "你贏了"
        if(2 == i):
            result["text"] = "平手"


window = Tk()
window.title("視窗標題")#title name

#define
picture = {}
button = {}
name = ["scissors", "stone", "paper"]

player_select = Label(window)
player_select.grid(row=0, column=0,padx=0, pady=0)
result = Label(window)
result.grid(row=0, column=1,padx=15, pady=25)
computer_select = Label(window)
computer_select.grid(row=0, column=2,padx=0, pady=0)

for i in range(0, 3):
    picture[i] = ImageTk.PhotoImage(Image.open("mora%s.gif" %str(i+1)))
    button[i] = Button(window, text=name[i], compound=TOP, image=picture[i], command=lambda n=i :mora(n))
    button[i].grid(row=1, column=i, padx=20)

window.mainloop()