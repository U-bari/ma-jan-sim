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
class Select_player:
	def __init__(self,x,y):
		self.name = StringVar()
		self.box = ttk.Combobox(frame1, textvariable=self.name,values=member_list)
		self.box.grid(row=x,column=y)

cb1 = Select_player(0,1)

cb2 = Select_player(0,2)

cb3 = Select_player(0,3)

cb4 = Select_player(0,4)

#結果表示場所
class Labels:
	def __init__(self,x,y):
		self.text = StringVar()
		self.label = ttk.Label(frame1,textvariable=self.text)
		self.label.grid(row = x, column=y)

A_1_1 = Labels(1,1)

A_1_2 = Labels(1,2)

A_1_3 = Labels(1,3)

A_1_4 = Labels(1,4)

A_2_1 = Labels(2,1)

A_2_2 = Labels(2,2)

A_2_3 = Labels(2,3)

A_2_4 = Labels(2,4)

A_3_1 = Labels(3,1)

A_3_2 = Labels(3,2)

A_3_3 = Labels(3,3)

A_3_4 = Labels(3,4)

A_4_1 = Labels(4,1)

A_4_2 = Labels(4,2)

A_4_3 = Labels(4,3)

A_4_4 = Labels(4,4)



cbs = [A_1_1.text,A_1_2.text,A_1_3.text,A_1_4.text,
	A_2_1.text,A_2_2.text,A_2_3.text,A_2_4.text,
	A_3_1.text,A_3_2.text,A_3_3.text,A_3_4.text,
	A_4_1.text,A_4_2.text,A_4_3.text,A_4_4.text]

#確率表示コマンド
def button1_command():
	for cb,i,j in zip(cbs,[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]):
		cb.set(rate_system.expect(cb1.name.get(),cb2.name.get(),cb3.name.get(),cb4.name.get(),rate)[i][j])

#確率表示ボタン
button1 = ttk.Button(
	frame1, text="ok", command=partial(button1_command)
	)
button1.grid(row=0,column=5)

class Just_label:
	def __init__(self, x, y, A):
		self.sentence = A
		self.label = ttk.Label(frame1, text=self.sentence, width = 15)
		self.label.grid(row=x, column=y)
		

rank1 = Just_label(1,0,"一着率")
rank2 = Just_label(2,0,"二着率")
rank3 = Just_label(3,0,"三着率")
rank4 = Just_label(4,0,"四着率")

root.mainloop()