from tkinter import *
from PIL import Image, ImageTk
import time



def click():
    global stop
    if btn["text"] == "停止":
        btn["text"] = "繼續跑步"
        stop = True
    else:
        btn["text"] = "停止"
        stop = False

def change_direction(void):
    global i, k
    if k==0:
        k=1
        if i<4:
            i=4
    else:
        k=0
        if i>4:
            i=0

def leave(void):
    global exit
    exit = True

tk = Tk()
tk.title("來回跑步")#遊戲視窗標題
tk.geometry("600x200")#視窗大小

#定義區
stop = True
image={}

for i in range(0, 7):
    image[i] = ImageTk.PhotoImage(Image.open("man%s.gif" %str(i+1)))#loading 8 picture to dict

canvas = Canvas(tk, width=600,height=88)
x = canvas.create_image(512,0,anchor=NW,image=image[0])
canvas.pack()

btn = Button(tk, width=10, height=3, text='開始', bg="white", command=click)#create button
btn.pack(side=RIGHT)

#定義區
i=0#顯示那張圖片
k=0
exit=False
while(1):
    if stop==False:
        image_coordinate = canvas.coords(x)#取得圖片的位
        if image_coordinate[0] < 20:
            k=1
            if i<4:
                i=4
        if image_coordinate[0] > 500:
            k=0
            if i>4:
                i=0
        canvas.bind('<Button-3>', change_direction)#點擊滑鼠右鍵
        canvas.bind_all('<KeyPress-q>', leave)#點擊q鍵離開
        if image_coordinate[0] > 20 and k==0:
            canvas.delete(x)
            x = canvas.create_image(512,0,anchor=NW,image=image[i])
            canvas.move(x, image_coordinate[0]-532, 0)
            i+=1
            if i>=4:
                i=0
        if image_coordinate[0] < 500 and k==1:
            canvas.delete(x)
            x = canvas.create_image(512,0,anchor=NW,image=image[i])
            canvas.move(x, image_coordinate[0]-492, 0)
            i+=1
            if i>=7:
                i=4
    
    if exit==True:
        break
    tk.update()
    time.sleep(0.1)



tk.mainloop()