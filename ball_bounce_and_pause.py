from tkinter import *
import random
import time



def game_stop(x):
    global leave
    while(leave == False):
        tk.update()
        canvas.bind('<Button-1>', leave1)#cleck left mouse button
    leave = False

def leave1(x):
    global leave
    leave = True

WindowWidth = 640#window width
WindowHigh = 480#window high
stepx = -3#ball speed
stepy = -3#ball speed
speed = 0.01#window show speed
radi = 20#ball radius

leave = False

tk = Tk()
tk.title("Bouncing Ball")#window title
tk.wm_attributes('-topmost', 1)#window top of the screen
canvas = Canvas(tk, width=WindowWidth, height=WindowHigh)
canvas.pack()
ball = canvas.create_oval(0, 0, radi*2, radi*2, fill="yellow")#create ball
canvas.move(ball, random.randint(0, WindowWidth), random.randint(0, WindowHigh/2))#set ball position+random

while(1):
    ballPos = canvas.coords(ball)#catch ball position
    canvas.move(ball, stepx, stepy)#move the ball
    if ballPos[0] <= 0:#if ball hit on left boundary
        stepx = 3
    if ballPos[1] <= 0:#if ball hit on up boundary
        stepy = 3
    if ballPos[2] >= WindowWidth:#if ball hit on right boundary
        stepx = -3
    if ballPos[3] >= WindowHigh:#if ball hit on down boundary
        stepy = -3
    canvas.bind('<Button-1>', game_stop)#cleck left mouse button
    tk.update()#update screen
    time.sleep(speed)#delay time

tk.mainloop()
