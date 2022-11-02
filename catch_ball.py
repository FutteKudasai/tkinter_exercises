from tkinter import *
import random
import time



def BallMove():#球移動功能
    global i, ball, stepx, stepy, TouchBottom, recket
    ballPos = canvas.coords(ball)#取得球的位置
    racketPos = canvas.coords(recket)#偵測球拍位置
    canvas.move(ball, stepx, stepy)#球移動一格
    if ballPos[0] <= 0:#判斷是否撞到左方牆壁
        stepx = 3
    if ballPos[1] <= 0:#判斷是否撞到上方牆壁
        stepy = 3
    if ballPos[2] >= WindowWidth:#判斷是否撞到右方牆壁
        stepx = -3
    if ballPos[3] >= WindowHigh:#判斷是否撞到下方牆壁
        TouchBottom = True#未接到球
    if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
        if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
            if(stepy == -3):
                pass
            else:
                i+=1#加1分
                stepy = -3

def RecketMove():
    global recket, y
    racketPos = canvas.coords(recket)#偵測球拍位置
    if racketPos[0] <= 0:#判斷是否碰到左側邊界
        canvas.move(recket, 0, 0)
    if racketPos[2] >= WindowWidth:#判斷是否碰到右側邊界
        canvas.move(recket, 0, 0)
    if racketPos[0] > 0 and y==1:#判斷是否不在邊界上 and 移動狀態
        canvas.move(recket, -3, 0)#向左移動
    if racketPos[2] < WindowWidth and y==2:#判斷是否不在邊界上 and 移動狀態
        canvas.move(recket, 3, 0)#向右移動
    canvas.bind_all('<KeyPress-Right>', MoveRight)#點擊右方向鍵
    canvas.bind_all('<KeyPress-Left>', MoveLeft)#點擊左方向鍵
    
def MoveLeft(x):
    global y
    y=1
def MoveRight(x):
    global y
    y=2


WindowWidth = 640#定義畫布寬度
WindowHigh = 480#定義畫布高度
stepx = -3#定義速度可想成位移步伐
stepy = -3#定義速度可想成位移步伐
speed = 0.01#設定畫面速度(每0.01秒換)
radi = 20#球半徑

x=0#控制球拍水平位置
TouchBottom = False#定義球是否落地
i=0#分數初始值
y=0#控制球拍方向

tk = Tk()
tk.title("Bouncing Ball")#遊戲視窗標題
tk.wm_attributes('-topmost', 1)#確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=WindowWidth, height=WindowHigh)
canvas.pack()
ball = canvas.create_oval(0, 0, radi*2, radi*2, fill="yellow")#建立球物件
canvas.move(ball, random.randint(0, WindowWidth), random.randint(0, WindowHigh/2))#設定球最初位置+隨機
recket = canvas.create_rectangle(0,0,100,15, fill="purple")#建立球拍物件
canvas.move(recket, 270, 400)#設定球拍最初位置
score = Label(tk, text="分數"+str(i))#建立分數物件
score.pack()

while(1):
    BallMove()#球移動
    RecketMove()#球拍移動
    tk.update()#更新畫面，沒有此行，沒有畫面
    score["text"]= "分數"+str(i)#更改分數
    if TouchBottom == True:#判斷是否接到球
        break
    time.sleep(speed)#時間前進一格(滴答)

tk.mainloop()