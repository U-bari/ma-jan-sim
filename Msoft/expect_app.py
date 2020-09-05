from tkinter import *
from tkinter import ttk
import os
import csv
import rate_system
import data
from functools import partial




data_list = data.data_list

#初期rate生成
rate = {}
member = set([])

#rate生成
for i in data_list:
	member = rate_system.member_make(i,member)

rate = rate_system.make_rate(member,rate)


rate = rate_system.rate_all(data_list,rate,A="",K=4)


member_list=list(member)

root = Tk()
root.geometry("800x300")
root.title("Mリーグ予測")
frame1 = ttk.Frame(root)
frame1.grid()

#コンボボックス
A = StringVar()
cb1 = ttk.Combobox(
	frame1, textvariable=A,values=member_list
)
cb1.set("小林剛")
cb1.grid(row=0,column=1)

B = StringVar()
cb2 = ttk.Combobox(
	frame1, textvariable=B,values=member_list
)
cb2.set("多井隆晴")
cb2.grid(row=0,column=2)

C = StringVar()
cb3 = ttk.Combobox(
	frame1, textvariable=C,values=member_list
)
cb3.set("魚谷侑未")
cb3.grid(row=0,column=3)

D = StringVar()
cb4 = ttk.Combobox(
	frame1, textvariable=D,values=member_list
)
cb4.set("石橋伸洋")
cb4.grid(row=0,column=4)

#結果表示場所
cb_1_1 = StringVar()
A_1_1 = ttk.Label(frame1,textvariable=cb_1_1)
A_1_1.grid(row=1,column=1)

cb_1_2 = StringVar()
A_1_2 = ttk.Label(frame1,textvariable=cb_1_2)
A_1_2.grid(row=1,column=2)

cb_1_3 = StringVar()
A_1_3 = ttk.Label(frame1,textvariable=cb_1_3)
A_1_3.grid(row=1,column=3)

cb_1_4 = StringVar()
A_1_4 = ttk.Label(frame1,textvariable=cb_1_4)
A_1_4.grid(row=1,column=4)

cb_2_1 = StringVar()
A_2_1 = ttk.Label(frame1,textvariable=cb_2_1)
A_2_1.grid(row=2,column=1)

cb_2_2 = StringVar()
A_2_2 = ttk.Label(frame1,textvariable=cb_2_2)
A_2_2.grid(row=2,column=2)

cb_2_3 = StringVar()
A_2_3 = ttk.Label(frame1,textvariable=cb_2_3)
A_2_3.grid(row=2,column=3)

cb_2_4 = StringVar()
A_2_4 = ttk.Label(frame1,textvariable=cb_2_4)
A_2_4.grid(row=2,column=4)

cb_3_1 = StringVar()
A_3_1 = ttk.Label(frame1,textvariable=cb_3_1)
A_3_1.grid(row=3,column=1)

cb_3_2 = StringVar()
A_3_2 = ttk.Label(frame1,textvariable=cb_3_2)
A_3_2.grid(row=3,column=2)

cb_3_3 = StringVar()
A_3_3 = ttk.Label(frame1,textvariable=cb_3_3)
A_3_3.grid(row=3,column=3)

cb_3_4 = StringVar()
A_3_4 = ttk.Label(frame1,textvariable=cb_3_4)
A_3_4.grid(row=3,column=4)

cb_4_1 = StringVar()
A_4_1 = ttk.Label(frame1,textvariable=cb_4_1)
A_4_1.grid(row=4,column=1)

cb_4_2 = StringVar()
A_4_2 = ttk.Label(frame1,textvariable=cb_4_2)
A_4_2.grid(row=4,column=2)

cb_4_3 = StringVar()
A_4_3 = ttk.Label(frame1,textvariable=cb_4_3)
A_4_3.grid(row=4,column=3)

cb_4_4 = StringVar()
cb_4_4.set("aaa")
A_4_4 = ttk.Label(frame1,textvariable=cb_4_4)
A_4_4.grid(row=4,column=4)

cbs = [cb_1_1,cb_1_2,cb_1_3,cb_1_4,
	cb_2_1,cb_2_2,cb_2_3,cb_2_4,
	cb_3_1,cb_3_2,cb_3_3,cb_3_4,
	cb_4_1,cb_4_2,cb_4_3,cb_4_4]

#確率表示コマンド
def button1_command():
	for cb,i,j in zip(cbs,[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]):
		cb.set(rate_system.expect(A.get(),B.get(),C.get(),D.get(),rate)[i][j])

#確率表示ボタン
button1 = ttk.Button(
	frame1, text="ok", command=partial(button1_command)
	)
button1.grid(row=0,column=5)


rank1 = ttk.Label(frame1, text="1着"
	,width = 15)
rank1.grid(row=1,column=0)

rank2 = ttk.Label(frame1, text="2着"
	,width = 15)
rank2.grid(row=2,column=0)

rank3 = ttk.Label(frame1, text="3着"
	,width = 15)
rank3.grid(row=3,column=0)

rank4 = ttk.Label(frame1, text="4着"
	,width = 15)
rank4.grid(row=4,column=0)


root.mainloop()

