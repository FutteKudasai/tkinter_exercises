from tkinter import *
# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3, no0):
    if order == 0:      # 階級數為0
        # 將3個點連接繪製成三角形
        drawLine(p1, p2, no0)
        drawLine(p2, p3, no0)
        drawLine(p3, p1, no0)
    else:
        # 取得三角形各邊長的中點
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        # 遞迴呼叫處理繪製三角形
        sierpinski(order - 1, p1, p12, p31, no0)
        sierpinski(order - 1, p12, p2, p23, no0)
        sierpinski(order - 1, p31, p23, p3, no0)
# 繪製p1和p2之間的線條
def drawLine(p1,p2, no0):
    if no0 == 0:
        canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline")
    else:
        canvas2.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline2")
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                                   # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p
# 顯示
def show(no0):
    p1 = [200, 20]
    p2 = [20, 380]
    p3 = [380,380]
    if no0 == 0:
        canvas.delete("myline")
        sierpinski(order.get(), p1, p2, p3, no0)
    else:
        canvas2.delete("myline")
        sierpinski(order2.get(), p1, p2, p3, no0)    

# main
tk = Tk()
canvas = Canvas(tk, width=400, height=400)      # 建立畫布
canvas.grid(row=1,column=1)
frame = Frame(tk)                   # 建立框架
frame.grid(row=2,column=1)

# 在框架Frame內建立標籤Label, 輸入階乘數Entry, 按鈕Button
Label(frame, text="輸入階數 : ").pack(side=LEFT)
order = IntVar()
order.set(0)
entry = Entry(frame, textvariable=order).pack(side=LEFT,padx=3)
Button(frame, text="顯示Sierpinski三角形", command=lambda: show(0)).pack(side=LEFT)

canvas2 = Canvas(tk, width=400, height=400)      # 建立畫布
canvas2.grid(row=1,column=2)
frame2 = Frame(tk)                   # 建立框架
frame2.grid(row=2,column=2)

# 在框架Frame內建立標籤Label, 輸入階乘數Entry, 按鈕Button
Label(frame2, text="輸入階數 : ").pack(side=LEFT)
order2 = IntVar()
order2.set(0)
entry2 = Entry(frame2, textvariable=order2).pack(side=LEFT,padx=3)
Button(frame2, text="顯示Sierpinski三角形", command=lambda: show(1)).pack(side=LEFT)

tk.mainloop()
