
import os
import csv
import rate_system
import data


data_list = data.data_list

#初期rate生成
rate = {}
member = set([])


for i in data_list:
	member = rate_system.member_make(i,member)

rate = rate_system.make_rate(member,rate)

print("係数を入力")
K = int(input())
A = ""

x = 100
while x != "1" and x != "2":
	print("1:レート表示　2:対戦予想 (半角で入力)")
	x = input()
if x == "1":
	print("選手のグラフを見たい場合は選手名を入力。そうでない場合はEnter")
	A = input()
#rateの作成
rate = rate_system.rate_all(data_list,rate,A,K)
sorted_rate = sorted(rate.items(), key=lambda x:x[1], reverse=True)


if x == "1":
	for name, point in sorted_rate:
		print(name.ljust(6,"　") + ":　" + str(point))
elif x == "2":
	print("1人目を入力")
	W = input()
	print("2人目を入力")
	X = input()
	print("3人目を入力")
	Y = input()
	print("4人目を入力")
	Z = input()
	rate_system.expect(W,X,Y,Z,rate)

