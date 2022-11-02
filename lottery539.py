from tkinter import *
import random



def click():
    global k,random_number,choose_number
    j=0
    k=0
    if(btn["bg"] == "green"):
        for number in range(0, 5):
            number = random.randint(1, 39)
            random_number.append(number)#將1~39隨機數字放入字串
        random_number.sort()
        z=0#開獎位置
        for number in random_number:
            x = Label(window, text=number, width=15, fg="red", bg="lightyellow")#lavel內容設定
            x.grid(row=0, column=z,padx=5, pady=5)#lavel位置設定
            z=z+1
        both = set(random_number) & set(choose_number)
        for i in both:
            j=j+1
        #print("您猜中 %d 個號碼"%j)
        text["text"]=("您猜中 %d 個號碼"%j)
        random_number=[]#清空亂數，為下次開獎準備

def answer():
    global j,k,random_number
    j=0
    for test in range(0, 5):
        x = Label(window, text="", width=15, fg="red", bg="lightyellow")#lavel內容設定
        x.grid(row=0, column=j,padx=5, pady=5)#lavel位置設定
        j = j+1

def choose_button(n):
    global number, choose_number, k
    if(number[n]["bg"] == "yellow"):
        number[n]["bg"] = "red"#按鈕黃變紅
        choose_number.append(n)
    else:
        number[n]["bg"] = "yellow"#按鈕紅變黃
        delete = choose_number.index(n)#尋找該數的串列位置
        choose_number.pop(delete)#刪除該數
    if(len(choose_number) == 5):#判斷選了幾個數字
        btn["bg"] = "green"#更改btn的背景為綠色
    else:
        btn["bg"] = "blue"
    #print("選擇號碼",choose_number)

window = Tk()
window.title("視窗標題")#視窗標題
#window.geometry("800x450")#視窗大小

k=0
random_number=[]
choose_number=[]
number={}
answer()

btn = Button(window,width=15, text='開獎', bg="blue", command=click)#結算按鈕
btn.grid(row=0,column=5,padx=5, pady=5)#結算按鈕位置

text = Label(window, text="任選5個號碼，等開獎綠燈亮，然後按開獎", fg="blue")
text.grid(row=1, column=0, columnspan=11)

j=0
i=2
for num in range(1, 40):#建立選項按鈕
    number[num] = Button(window,text=num, width=15, bg="yellow", command=lambda n=num :choose_button(n))
    number[num].grid(row=i, column=j, pady=5)
    j = j+1
    if(j >= 6):#換行功能。第6格要換到下一行
        j=0
        i=i+1

window.mainloop()
'''
readme:
i,j:控制屬性位置
k:控制一開始不要直接顯示隨機數字
'''

'''
def printSelection():
    print(number[var.get()])      
    
    #relief="raised"

number = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11",12:"12",13:"13",14:"14",15:"15",16:"16",17:"17",18:"18",19:"19",20:"20",21:"21",22:"22",23:"23",24:"24",25:"25",26:"26",27:"27",28:"28",29:"29",30:"30",31:"31",32:"32",33:"33",34:"34",35:"35",36:"36",37:"37",38:"38",39:"39"}
var = IntVar()
#var.set(0)#預設按下選項
j=0
i=2
for val, num in number.items():#建立選項紐
    Radiobutton(window, text=num, indicatoron = 0, width=15, variable=var, value=val, bg="yellow", relief="raised", command=printSelection).grid(row=i,column=j,pady=5)
    j = j+1
    if(j >= 6):#換行功能。第6格要換到下一行
        j=0
        i=i+1
'''

#z["bg"] = "green"
#print(number)

#number[1]["bg"] = "red"
#number[4]["bg"] = "red"
#number[20]["bg"] = "red"
#number[36]["bg"] = "red"
#number[17]["bg"] = "red"

#for num in number:
#    if(number[num]["bg"]=="red"):
#        print(num)

