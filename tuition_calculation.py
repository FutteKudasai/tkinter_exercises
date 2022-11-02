from tkinter import *



def cal():
    total=0
    selection=''
    studentID_get = studentID.get()
    daynight_get = daynight.get()
    department_get =  department.get()
    if var1.get():
        selection += "住宿"
    if var2.get():
        selection += "機車停車"
    if var3.get():
        selection += "汽車停車"
    if daynight_get=="日間部" and department_get == "工科":
        total+=53000
    elif daynight_get=="日間部" and department_get == "商科":
        total+=47000
    elif daynight_get=="夜間部" and department_get == "工科":
        total+=48000
    elif daynight_get=="夜間部" and department_get == "商科":
        total+=46000
    print(total)
    msg1 = "同學學號:" + studentID_get+ " " + daynight_get + " " + department_get + " " + selection + " 總計:" + str(total)
    msg.set(msg1)



window = Tk()
window.title("學雜費計算")#視窗標題
#window.geometry("800x450")#視窗大小
#window.maxsize(1920, 1080)#視窗最大



text1 = Label(window,text="學號",width=15)
text1.grid(row=0,column=0,padx=5)#定位學號

studentID = StringVar()                   
student_ID = Entry(window,width=8,textvariable=studentID)#文字方塊
student_ID.grid(row=0,column=1)
#lab1.place(x=0,y=0)#直接定位



text2 = Label(window,text="日夜間部",width=15)
text2.grid(row=1,column=0,padx=5)#定位日夜間部

daynight = StringVar()
daynight.set("日間部")
rb1 = Radiobutton(window,text="日間部",variable=daynight,value='日間部')
rb1.grid(row=1,column=1)
rb2 = Radiobutton(window,text="夜間部",variable=daynight,value='夜間部')
rb2.grid(row=1,column=2)



text3 = Label(window,text="工科或商科",width=15)
text3.grid(row=2,column=0,padx=5)#定位日夜間部

department = StringVar()
department.set("工科")
rb1 = Radiobutton(window,text="工科",variable=department,value='工科')
rb1.grid(row=2,column=1)
rb2 = Radiobutton(window,text="商科",variable=department,value='商科')
rb2.grid(row=2,column=2)



text3 = Label(window,text="任選下列選項:",width=15)
text3.grid(row=3,column=1,padx=5)#定位任選下列選項:

var1 = StringVar()                      
Checkbutton(window,text="住宿",variable=var1).grid(row=4,column=1)
var2 = StringVar()
Checkbutton(window,text="機車停車",variable=var2).grid(row=5,column=1)                
var3 = StringVar()
Checkbutton(window,text="汽車停車", variable=var3).grid(row=6,column=1)   

btn = Button(window,width=5,text='結算',command=cal)#結算按鈕
btn.grid(row=7,column=1,pady=5)#結算按鈕

msg = StringVar()
msg.set("")
text4 = Label(window,textvariable = msg,bg="lightblue")
text4.grid(row=8,column=1)

exitbtn = Button(window,text="離開",command=window.destroy)
exitbtn.grid(row=9,column=1)




window.mainloop()
