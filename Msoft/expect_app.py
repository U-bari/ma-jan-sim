from tkinter import *
from tkinter import ttk
import os
import csv
import rate_system
import data
from functools import partial
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




#プロット
def plot_rate(data_list_, member_, k_, player_1,player_2,player_3,player_4,frame_):

	fig = plt.Figure(figsize=(6,4))
	fig.subplots_adjust(hspace=0.6, wspace=0.4)
	ax1 = fig.add_subplot(2,2,1,ylim=[1400,1600])
	ax1.set_title("1")
	ax2 = fig.add_subplot(2,2,2,ylim=[1400,1600])
	ax2.set_title("2")
	ax3 = fig.add_subplot(2,2,3,ylim=[1400,1600])
	ax3.set_title("3")
	ax4 = fig.add_subplot(2,2,4,ylim=[1400,1600])
	ax4.set_title("4")
	histroy1 = rate_system.make_rate(member_,{})
	histroy2 = rate_system.make_rate(member_,{})
	histroy3 = rate_system.make_rate(member_,{})
	histroy4 = rate_system.make_rate(member_,{})
	rate_history1 = [1500]
	rate_history2 = [1500]
	rate_history3 = [1500]
	rate_history4 = [1500]
	for data in data_list_:
		histroy1 = rate_system.rating(data,histroy1,K=k_)
		rate_history1.append(histroy1[player_1])

	for data in data_list_:
		histroy2 = rate_system.rating(data,histroy2,K=k_)
		rate_history2.append(histroy2[player_2])

	for data in data_list_:
		histroy3 = rate_system.rating(data,histroy3,K=k_)
		rate_history3.append(histroy3[player_3])

	for data in data_list_:
		histroy4 = rate_system.rating(data,histroy4,K=k_)
		rate_history4.append(histroy4[player_4])

	ax1.plot(list(range(len(data_list_)+1)), rate_history1)
	ax2.plot(list(range(len(data_list_)+1)), rate_history2)
	ax3.plot(list(range(len(data_list_)+1)), rate_history3)
	ax4.plot(list(range(len(data_list_)+1)), rate_history4)
	canvas = FigureCanvasTkAgg(fig, frame_)
	canvas.get_tk_widget().grid(row=0, column=0)
	canvas.draw()


#データ読み込み
data_list = data.data_list
member = set([])

#出場選手リスト作成
for i in data_list:
	member = rate_system.member_make(i,member)

member_list=list(member)

#GUI作成

#ウィンドウ作成
root = Tk()
root.geometry("700x600")
root.title("Mリーグ予測")
frame1 = ttk.Frame(root)
frame1.grid(row=0,column=0)
frame2 = ttk.Frame(root)
frame2.grid(row=1,column=0)

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

#結果表示場所label配置確率
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

#平均着順
A_6_1 = Labels(6,1)
A_6_2 = Labels(6,2)
A_6_3 = Labels(6,3)
A_6_4 = Labels(6,4)


#結果表示ラベルのテキストのリスト
cbs_rank = [A_2_1.text,A_2_2.text,A_2_3.text,A_2_4.text,
	A_3_1.text,A_3_2.text,A_3_3.text,A_3_4.text,
	A_4_1.text,A_4_2.text,A_4_3.text,A_4_4.text,
	A_5_1.text,A_5_2.text,A_5_3.text,A_5_4.text]

cbs_ave = [A_6_1.text,A_6_2.text,A_6_3.text,A_6_4.text]

#確率表示コマンド button1を押すと実行される
def button1_command():
	rate_origin = rate_system.make_rate(member,{})

	rate = rate_system.rate_all(data_list,rate_origin,A="",K=int(selected_k.get()))
	rate_origin2 = rate_system.make_rate(member,{})

	for cb,i,j in zip(cbs_rank,[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]):
		cb.set(rate_system.expect(cb1.name.get(),cb2.name.get(),cb3.name.get(),cb4.name.get(),rate)[i][j])
	for label, i in zip(cbs_ave,[0,1,2,3]):
		label.set(rate_system.expect_ave(cb1.name.get(),cb2.name.get(),cb3.name.get(),cb4.name.get(),rate)[i])
	plot_rate(data_list,member,int(selected_k.get()),cb1.name.get(),cb2.name.get(),cb3.name.get(),cb4.name.get(),frame2)


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
rank_ave = Just_label(6,0,"平均着順")

#コンボボックス説明ラベル
select_k_label = Just_label(0,0,"係数指定")
cb1_label = Just_label(0,1,"選手１")
cb2_label = Just_label(0,2,"選手２")
cb3_label = Just_label(0,3,"選手３")
cb4_label = Just_label(0,4,"選手４")


root.mainloop()

rate_origin = rate_system.make_rate(member,{})
rate = rate_system.rate_all(data_list,rate_origin,A="",K=4)


