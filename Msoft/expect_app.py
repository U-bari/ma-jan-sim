from tkinter import *
from tkinter import ttk
import os
import csv
import rate_system
import data
from functools import partial


data_list = data.data_list

member = set([])

#出場選手リスト作成
for i in data_list:
	member = rate_system.member_make(i,member)

member_list=list(member)

#GUI作成

#ウィンドウ作成
root = Tk()
root.geometry("800x300")
root.title("Mリーグ予測")
frame1 = ttk.Frame(root)
frame1.grid()

#選手選択コンボボックス
class Select_player:
	def __init__(self,x,y):
		self.name = StringVar()
		self.box = ttk.Combobox(frame1, textvariable=self.name,values=member_list,width=15,justify=RIGHT)
		self.box.grid(row=x,column=y,padx=5)

#選手選択コンボボックス配置
cb1 = Select_player(1,1)
cb2 = Select_player(1,2)
cb3 = Select_player(1,3)
cb4 = Select_player(1,4)

#係数K選択コンボボックス配置
selected_k = StringVar()
select_k = ttk.Combobox(frame1, textvariable=selected_k,values=[1,2,3,4,5,6,7,8],width=10,justify=RIGHT)
select_k.set(4)
select_k.grid(row=1,column=0,padx=5)

#結果表示場所label
class Labels:
	def __init__(self,x,y):
		self.text = StringVar()
		self.label = ttk.Label(frame1,textvariable=self.text)
		self.label.grid(row = x, column=y)

#結果表示場所label配置
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
A_5_1 = Labels(5,1)
A_5_2 = Labels(5,2)
A_5_3 = Labels(5,3)
A_5_4 = Labels(5,4)


#結果表示ラベルのテキストのリスト
cbs = [A_2_1.text,A_2_2.text,A_2_3.text,A_2_4.text,
	A_3_1.text,A_3_2.text,A_3_3.text,A_3_4.text,
	A_4_1.text,A_4_2.text,A_4_3.text,A_4_4.text,
	A_5_1.text,A_5_2.text,A_5_3.text,A_5_4.text]



#確率表示コマンド button1を押すと実行される
def button1_command():
	rate_origin = rate_system.make_rate(member,{})
	rate = rate_system.rate_all(data_list,rate_origin,A="",K=int(selected_k.get()))
	for cb,i,j in zip(cbs,[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]):
		cb.set(rate_system.expect(cb1.name.get(),cb2.name.get(),cb3.name.get(),cb4.name.get(),rate)[i][j])

#確率表示ボタン1
button1 = ttk.Button(
	frame1, text="ok", command=partial(button1_command)
	)
button1.grid(row=1,column=5)

#ただのラベル　x,yはグリッドによる位置指定　Aは表示するテキスト
class Just_label:
	def __init__(self, x, y, A):
		self.sentence = A
		self.label = ttk.Label(frame1, text=self.sentence)
		self.label.grid(row=x, column=y,padx=5,pady=5)

#着順ラベル
rank1 = Just_label(2,0,"一着率")
rank2 = Just_label(3,0,"二着率")
rank3 = Just_label(4,0,"三着率")
rank4 = Just_label(5,0,"四着率")

#コンボボックス説明ラベル
select_k_label = Just_label(0,0,"係数指定")
cb1_label = Just_label(0,1,"選手１")
cb2_label = Just_label(0,2,"選手２")
cb3_label = Just_label(0,3,"選手３")
cb4_label = Just_label(0,4,"選手４")


root.mainloop()