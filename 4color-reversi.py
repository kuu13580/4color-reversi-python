#Version 2.1
from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial
import numpy as np


#配列生成・変数定義
data = np.full((10,10),"black")
predata = np.full((10,10),"black")
turn = 0
nowcolor = "red"
judge = 0
button = [[0] * 10] * 10

#初期化
data[3][3:7] = ["red","white","green","blue"]
data[4][3:7] = ["blue","green","white","red"]
data[5][3:7] = ["green","blue","red","white"]
data[6][3:7] = ["white","red","blue","green"]
for i in range (10):
    for j in range (10):
        predata[i][j]=data[i][j]
#window
root1 = Tk()
root1.title("４色オセロ")
frame1 = ttk.Frame(root1,padding=20)
frame1.pack()
labelstyle = ttk.Style()
labelstyle.configure("label.TLabel",font=(10))
redcount = StringVar(root1,value="4")
bluecount = StringVar(root1,value="4")
greencount = StringVar(root1,value="4")
whitecount = StringVar(root1,value="4")
resultlabel1 = Label(frame1,text="赤の数：",font="label.TLabel")
resultlabel2 = Label(frame1,text="青の数：",font="label.TLabel")
resultlabel3 = Label(frame1,text="緑の数：",font="label.TLabel")
resultlabel4 = Label(frame1,text="白の数：",font="label.TLabel")
redresult = Label(frame1,textvariable=redcount,font="label.TLabel")
blueresult = Label(frame1,textvariable=bluecount,font="label.TLabel")
greenresult = Label(frame1,textvariable=greencount,font="label.TLabel")
whiteresult = Label(frame1,textvariable=whitecount,font="label.TLabel")
resultlabel1.grid(row=0,column=10,padx=5)
resultlabel2.grid(row=1,column=10,padx=5)
resultlabel3.grid(row=2,column=10,padx=5)
resultlabel4.grid(row=3,column=10,padx=5)
redresult.grid(row=0,column=11,)
blueresult.grid(row=1,column=11,)
greenresult.grid(row=2,column=11,)
whiteresult.grid(row=3,column=11,)

def view():
    def change(i,j):
        global turn
        global judge
        global nowcolor
        global predata
        global data
        global button
        if (i == 100)&(j == 100):#パス
            turn += 1
        elif (i == 11)&(j == 11):#ひとつ戻る
            print (predata)
            for i10 in range(10):
                for j10 in range (10):
                    button[i10][j10] = tk.Button(frame1,text = "",width=7,height=3,background=predata[i10][j10],command=partial(change,i10,j10))
                    button[i10][j10].grid(row=i10,column=j10)
            for i11 in range(10):
                for j11 in range(10):
                    data[i11][j11] = predata[i11][j11]
            judge = 0
            turn -= 1
        elif (i < 10)&(j < 10):#確認とひっくり返し
            if data[i][j] == "black":
                for i12 in range(10):
                    for j12 in range(10):
                        predata[i12][j12] = data[i12][j12]
                #↑確認
                for i1 in reversed(range(0,i)):
                    if (data[i1][j] == nowcolor)&(data[i-1][j] != nowcolor):
                        for i11 in range(i1,i):
                            data[i11][j] = nowcolor
                            button[i11][j] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i11,j))
                            button[i11][j].grid(column=j,row=i11)
                        judge = 1
                        break
                    elif data[i1][j] == "black":
                        break
                #↓確認
                for i2 in range(i+1,10):
                    if (data[i2][j] == nowcolor)&(data[i+1][j] != nowcolor):
                        for i22 in range(i,i2):
                            data[i22][j] = nowcolor
                            button[i22][j] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i22,j))
                            button[i22][j].grid(column=j,row=i22)
                        judge = 1
                        break
                    elif data[i2][j] == "black":
                        break
                #←確認
                for j3 in reversed(range(0,j)):
                    if (data[i][j3] == nowcolor)&(data[i][j-1] != nowcolor):
                        for j33 in range(j3,j):
                            data[i][j33] = nowcolor
                            button[i][j33] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i,j33))
                            button[i][j33].grid(column=j33,row=i)
                        judge = 1
                        break
                    elif data[i][j3] == "black":
                        break
                #→確認
                for j4 in range(j+1,10):
                    if (data[i][j4] == nowcolor)&(data[i][j+1] != nowcolor):
                        for j44 in range(j,j4):
                            data[i][j44] = nowcolor
                            button[i][j44] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i,j44))
                            button[i][j44].grid(column=j44,row=i)
                        judge = 1
                        break
                    elif data[i][j4] == "black":
                        break
                i5 = i 
                j5 = j 
                i6 = i 
                j6 = j 
                i7 = i 
                j7 = j 
                i8 = i 
                j8 = j 
                #↖確認
                while ((i5 != 0) & (j5 != 0)):
                    i5 -= 1
                    j5 -= 1
                    if (data[i5][j5] == nowcolor)&(data[i-1][j-1] != nowcolor):
                        for ij55 in range(i-i5):
                            data[i-ij55][j-ij55] = nowcolor
                            button[i-ij55][j-ij55] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i-ij55,j-ij55))
                            button[i-ij55][j-ij55].grid(column=j-ij55,row=i-ij55)
                        judge = 1
                        break
                    elif data[i5][j5] == "black":
                        break
                #↘確認
                while ((i6 != 9) & (j6 != 9)):
                    i6 += 1
                    j6 += 1
                    if (data[i6][j6] == nowcolor)&(data[i+1][j+1] != nowcolor):
                        for ij66 in range(i6-i):
                            data[i+ij66][j+ij66] = nowcolor
                            button[i+ij66][j+ij66] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i+ij66,j+ij66))
                            button[i+ij66][j+ij66].grid(column=j+ij66,row=i+ij66)
                        judge = 1
                        break
                    elif data[i6][j6] == "black":
                        break
                #↗確認
                while ((i7 != 0) & (j7 != 9)):
                    i7 -= 1
                    j7 += 1
                    if (data[i7][j7] == nowcolor)&(data[i-1][j+1] != nowcolor):
                        for ij77 in range(i-i7):
                            data[i-ij77][j+ij77] = nowcolor
                            button[i-ij77][j+ij77] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i-ij77,j+ij77))
                            button[i-ij77][j+ij77].grid(column=j+ij77,row=i-ij77)
                        judge = 1
                        break
                    elif data[i7][j7] == "black":
                        break
                #↙確認
                while ((i8 != 9) & (j8 != 0)):
                    i8 += 1
                    j8 -= 1
                    if (data[i8][j8] == nowcolor)&(data[i+1][j-1] != nowcolor):
                        for ij88 in range(i8-i):
                            data[i+ij88][j-ij88] = nowcolor
                            button[i+ij88][j-ij88] = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor,command=partial(change,i+ij88,j-ij88))
                            button[i+ij88][j-ij88].grid(column=j-ij88,row=i+ij88)
                        judge = 1
                        break
                    elif data[i8][j8] == "black":
                        break
                if judge == 1:#上記処理が行われているか
                    data[i][j] = nowcolor
                    button[i][j] = tk.Button(frame1,text = "",width=7,height=3,background=data[i][j],command=partial(change,i,j))
                    button[i][j].grid(column=j,row=i)
                    turn += 1
                    judge = 0
                else:
                    print("エラー")
        if turn%4 == 0:
            nowcolor = "red"
        elif turn%4 == 1:
            nowcolor = "blue"
        elif turn%4 == 2:
            nowcolor = "green"
        elif turn%4 == 3:
            nowcolor = "white"
        turnbutton = tk.Button(frame1,text = "",width=7,height=3,background=nowcolor)
        turnbutton.grid(row=10,column=0,pady=20)
        redcount.set(np.count_nonzero(data == "red"))
        bluecount.set(np.count_nonzero(data == "blue"))
        greencount.set(np.count_nonzero(data == "green"))
        whitecount.set(np.count_nonzero(data == "white"))
        root1.mainloop()
    #画面生成
    for i in range(0,10):
        for j in range (0,10):
            button[i][j] = tk.Button(frame1,text = "",width=7,height=3,background=data[i][j],command=partial(change,i,j))
            button[i][j].grid(column=j,row=i)
    turnbutton = tk.Button(frame1,text = "",width=7,height=3,background="red")
    turnlabel = Label(frame1,text="のターン")
    returnbutton = Button(frame1,text="戻る",font="label.TLabel",command=partial(change,11,11))
    finishbutton = Button(frame1,text="終了",font="label.TLabel",command=lambda : root1.destroy())
    passbutton = Button(frame1,text="パス",font="label.TLabel",command=partial(change,100,100))
    returnbutton.grid(row=10,column=7,pady=10)
    turnbutton.grid(row=10,column=0,pady=10)
    turnlabel.grid(row=10,column=1,pady=10)
    finishbutton.grid(row=10,column=9,pady=10)
    passbutton.grid(row=10,column=8,pady=10)
    root1.mainloop()

view()