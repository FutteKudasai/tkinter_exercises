from tkinter import *
from PIL import Image, ImageTk
import random
import time



def mora(event):
    global win_times, draw_times, lose_times, total_times
    times = int(c.get())
    if(times>0 and len(n.get())>0 and event<4):#
        if(bout["state"] == NORMAL):
            total_times = int(times)
        bout["state"]=player_name["state"]=DISABLED
        times -= 1
        c.set(times)
        player_select["image"] = picture[event]#顯示玩家出拳圖片
        i = random.randint(0, 2)#電腦隨機出拳
        computer_select["image"] = picture[i]#顯示電腦出拳圖片
        if(event == 0):#玩家出剪刀
            if(0 == i):#電腦出剪刀
                result["text"] = "平手"
                draw_times+=1
                d.set(draw_times)
            if(1 == i):#電腦出石頭
                result["text"] = "你輸了"
                lose_times+=1
                l.set(lose_times)
            if(2 == i):#電腦出布
                result["text"] = "你贏了"
                win_times+=1
                w.set(win_times)
        if(event == 1):#玩家出石頭
            if(0 == i):#電腦出剪刀
                result["text"] = "你贏了"
                win_times+=1
                w.set(win_times)
            if(1 == i):#電腦出石頭
                result["text"] = "平手"
                draw_times+=1
                d.set(draw_times)
            if(2 == i):#電腦出布
                result["text"] = "你輸了"
                lose_times+=1
                l.set(lose_times)
        if(event == 2):#玩家出布
            if(0 == i):#電腦出剪刀
                result["text"] = "你輸了"
                lose_times+=1
                l.set(lose_times)
            if(1 == i):#電腦出石頭
                result["text"] = "你贏了"
                win_times+=1
                w.set(win_times)
            if(2 == i):#電腦出布
                result["text"] = "平手"
                draw_times+=1
                d.set(draw_times)
        if(times<=0):
            bout["state"]=player_name["state"]=NORMAL
            if(w.get()>l.get()):
                result["text"] = "你獲勝"
            if(w.get()<l.get()):
                result["text"] = "電腦獲勝"
            if(w.get()==l.get()):
                result["text"] = "雙方平手"

def save():
    try:
        with open("data.dat", mode = "a+", encoding = "utf8") as data:#開啟檔案
            data.write(time.ctime() + " 玩家：" + str(n.get()) + " 場次：" + str(total_times) + " 你贏：" + str(w.get()) + " 平手：" + str(d.get()) + " 你輸：" + str(l.get()) + "\n")
    except:
        open("data.dat", "w+")#建立檔案
        save()
    n.set("")
    w.set(0)
    d.set(0)
    l.set(0)

def new_window():
    
    newWindow = Toplevel(window)
    #new_window_text = Text(newWindow)
    #new_window_text.pack()
    new_window_lable = Label(newWindow, text="無紀錄")
    new_window_lable.pack()
    with open("data.dat", mode = "r", encoding = "utf8") as history_data:
        #new_window_text.insert(END, history_data.read())
        new_window_lable["text"]=history_data.read()
    

window = Tk()
window.title("視窗標題")#title name
window.geometry("500x400")


#define
picture = {}
button = {}
name = ["scissors", "stone", "paper"]
win_times = draw_times = lose_times = 0
total_times=0

canvas1 = Canvas(window, width=400, height=400)#建立畫布
canvas1.grid(row=0,column=0)
player_select = Label(canvas1)#建立玩家出拳圖片
player_select.grid(row=0, column=0, padx=50, pady=25)#玩家出拳顯示位置
result = Label(canvas1)#建立結果文字
result.grid(row=0, column=1, padx=50, pady=25)#結果文字顯示位置
computer_select = Label(canvas1)#建立電腦出拳圖片
computer_select.grid(row=0, column=2, padx=50, pady=25)#電腦出拳顯示位置

for i in range(0, 3):
    picture[i] = ImageTk.PhotoImage(Image.open("mora%s.gif" %str(i+1)))#載入圖片
    button[i] = Button(canvas1, text=name[i], compound=TOP, image=picture[i], command=lambda n=i :mora(n))#建立按鈕
    button[i].grid(row=1, column=i, padx=50, pady=15)#設定按鈕位置

canvas2 = Canvas(window, width=400, height=400)#建立畫布
canvas2.place(x=0,y=220)
player_name_lable = Label(canvas2, text="姓名：")
player_name_lable.grid(row=0, column=0)
n = StringVar()
player_name = Entry(canvas2, text="", textvariable=n)
player_name.grid(row=0, column=1, padx=50, pady=25)

canvas3 = Canvas(window, width=400, height=400)#建立畫布
canvas3.place(x=0,y=270)
bout_lable = Label(canvas3, text="回合：")
bout_lable.grid(row=0, column=0, padx=0, pady=20)
c = IntVar()
bout = Entry(canvas3, text="", width=10, textvariable=c)
bout.grid(row=0, column=1, padx=0, pady=20)
w = IntVar()
win_lable = Label(canvas3, text="你贏：")
win_lable.grid(row=0, column=2, padx=0, pady=20)
win = Entry(canvas3, text=win_times, width=10, textvariable=w, state=DISABLED)
win.grid(row=0, column=3, padx=0, pady=20)
d = IntVar()
draw_lable = Label(canvas3, text="平手：")
draw_lable.grid(row=0, column=4, padx=0, pady=20)
draw = Entry(canvas3, text=draw_times, width=10, textvariable=d, state=DISABLED)
draw.grid(row=0, column=5, padx=0, pady=20)
l = IntVar()
lose_lable = Label(canvas3, text="你輸：")
lose_lable.grid(row=0, column=6, padx=0, pady=20)
lose = Entry(canvas3, text=lose_times, width=10, textvariable=l, state=DISABLED)
lose.grid(row=0, column=7, padx=0, pady=20)

canvas4 = Canvas(window, width=4000, height=4000)#建立畫布
canvas4.place(x=0,y=320)
nowtime = Label(canvas4, text=time.ctime()+" "+n.get()+" "+str(c.get()))
nowtime.grid(row=0, column=0, padx=0, pady=0)
save_button = Button(canvas4, text="存檔與重製", width=10, command=save)
save_button.grid(row=0, column=1, padx=10, pady=10)
history_button = Button(canvas4, text="檢視紀錄", width=10, command=new_window)
history_button.grid(row=1, column=1, padx=10, pady=10)

while(1):
    mora(4)
    nowtime["text"] = time.ctime() + " 玩家：" + str(n.get()) + " 場次：" + str(total_times) + " 你贏：" + str(w.get()) + " 平手：" + str(d.get()) + " 你輸：" + str(l.get())
    window.update()
    #time.sleep(0.1)

window.mainloop()