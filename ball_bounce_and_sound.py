from tkinter import *
import random
import time
import pygame


def BallMove():#ball move function
    global i, ball, stepx, stepy, TouchBottom, recket
    ballPos = canvas.coords(ball)#get ball position
    racketPos = canvas.coords(recket)#get racket position
    canvas.move(ball, stepx, stepy)#ball move
    if ballPos[0] <= 0:#if ball hit on left boundary
        stepx = 3
    if ballPos[1] <= 0:#if ball hit on up boundary
        stepy = 3
    if ballPos[2] >= WindowWidth:#if ball hit on right boundary
        stepx = -3
    if ballPos[3] >= WindowHigh:#if ball hit on down boundary
        TouchBottom = True#not catch the ball
    if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
        if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
            if(stepy == -3):
                pass
            else:
                pygame.mixer.init()
                soundObj = pygame.mixer.Sound('pingpong.wav')#create Sound object
                soundObj.play()
                i+=1#i add 1
                stepy = -3

def RecketMove():
    global recket, y
    racketPos = canvas.coords(recket)#get racket position
    if racketPos[0] <= 0:#if ball hit on left boundary
        canvas.move(recket, 0, 0)
    if racketPos[2] >= WindowWidth:#if ball hit on right boundary
        canvas.move(recket, 0, 0)
    if racketPos[0] > 0 and y==1:#Determine if it is not on the boundary and move the state
        canvas.move(recket, -3, 0)#move left
    if racketPos[2] < WindowWidth and y==2:#Determine if it is not on the boundary and move the state
        canvas.move(recket, 3, 0)#move right
    canvas.bind_all('<KeyPress-Right>', MoveRight)#cleck right mouse button
    canvas.bind_all('<KeyPress-Left>', MoveLeft)#cleck left mouse button
    
def MoveLeft(x):
    global y
    y=1
def MoveRight(x):
    global y
    y=2

WindowWidth = 640#window width
WindowHigh = 480#window high
stepx = -3#ball speed
stepy = -3#ball speed
speed = 0.01#window show speed
radi = 20#ball radius

x=0#control the horizontal position of the racket
TouchBottom = False#defines whether the ball lands
i=0#score
y=0#control the direction of the racket

tk = Tk()
tk.title("Bouncing Ball")#window title
tk.wm_attributes('-topmost', 1)#window top of the screen
canvas = Canvas(tk, width=WindowWidth, height=WindowHigh)
canvas.pack()
ball = canvas.create_oval(0, 0, radi*2, radi*2, fill="yellow")#create ball
canvas.move(ball, random.randint(0, WindowWidth), random.randint(0, WindowHigh/2))#set ball position+random
recket = canvas.create_rectangle(0,0,100,15, fill="purple")#create recket
canvas.move(recket, 270, 400)#set recket position
score = Label(tk, text="分數"+str(i))#show score
score.pack()

while(1):
    BallMove()#ball move
    RecketMove()#recket move
    tk.update()#updata screen
    score["text"]= "分數"+str(i)#score add 1
    if TouchBottom == True:#determine recket to catch the ball
        break
    time.sleep(speed)#delay time

tk.mainloop()
