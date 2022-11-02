from tkinter import *
def add():#addition operation
    n3.set(n1.get()+n2.get())
def sub():#subtraction operation
    n3.set(n1.get()-n2.get())
def mul():#multiplication operation
    n3.set(n1.get()*n2.get())
def div():#division operation
    n3.set(n1.get()/n2.get())
    
window = Tk()
window.title("計算機")#window title

n1 = IntVar()                   
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window,width=8,textvariable=n1)#text box1
label = Button(window,width=3,text='+',command=add)
e2 = Entry(window,width=8,textvariable=n2)#text box2
btn = Label(window,width=5,text='=')
e3 = Entry(window,width=8,textvariable=n3)#result
label2 = Button(window,width=3,text='-',command=sub)
label2.grid(row=1,column=1,padx=5)#position subtraction

label3 = Button(window,width=3,text='*',command=mul)
label3.grid(row=2,column=1,padx=5)#position multiplication
label4 = Button(window,width=3,text='/',command=div)
label4.grid(row=3,column=1,padx=5)#position division

e1.grid(row=0,column=0)#position text box1
label.grid(row=0,column=1,padx=5)#position addition
e2.grid(row=0,column=2)#position text box2
btn.grid(row=1,column=1,pady=5)#position button
e3.grid(row=4,column=1)#position result

window.mainloop()
